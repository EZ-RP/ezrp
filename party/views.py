from django.db import transaction
from django.shortcuts import render
from party.models import Party, PartyAddress
from party.tables import *
from .forms import PartyForm
from base.modelforms import AddressForm
from django_tables2 import RequestConfig
from party.filters import PartyFilter


def all_customers(request):
    """
    Display all customers`.

    ``filter``
        filter used to filter customers

    ''customers''
        query set of parties, filtered to show customers

    **Template:**

    :template:`party/customer/all_customers.html`
    """
    filter = PartyFilter(request.GET, Party.objects.filter(party_type='C'))
    customers = CustomerTable(filter.qs)
    RequestConfig(request).configure(customers)
    return render(request, 'party/customer/all_customers.html', {'customers': customers,
                                                                 'filter': filter})


def customers(request):
    """
        Display the customer menu

        **Template:**

        :template:`party/customer/customers.html`
    """
    return render(request, 'party/customer/customers.html')

def partyMain(request):
    """
            Display the party menu

            **Template:**

            :template:`party/partyMain.html`
    """

    return render(request, 'party/partyMain.html')

@transaction.atomic
def customer_new(request):
    """
        Create a new customer

        ``form_customer``
            Model form of Party, for customer.

        ``form_address``
            Model form of Address, to be linked to customer

        **Template:**

        :template:`party/customer/customer_new.html`
    """

    if request.method == "POST":
        form_customer = PartyForm(request.POST)
        form_address = AddressForm(request.POST)
        if form_customer.is_valid() and form_address.is_valid():

            party = form_customer.save(commit=False)
            party.party_type = 'C'
            party.save()

            address = form_address.save(commit=False)
            address.save()
            party_address = PartyAddress()
            PartyAddress.add_address_ref(party_address, address, party)

            return all_customers(request)


    else:
        form_customer = PartyForm()
        form_address = AddressForm()
    return render(request, 'party/customer/customer_new.html', {'form_customer': form_customer,
                                                                'form_address': form_address})


def customer(request, account_number):
    """
        View and edit a customer

        ``show_address_form``
            Boolean dictating if the new address form is displayed.

        ``customer``
            The party instance of customer.

        ``form_customer``
            Model form of Party, for customer.

        ``form_address``
            Model form of Address, linked to customer

        **Template:**

        :template:`party/customer/customer_new.html`
    """

    show_address_form = False

    customer = Party.objects.get(account_number=account_number)

    if request.GET.get('add_address'):
        show_address_form = True

    if request.method == "POST":
        form_address = AddressForm(request.POST)
        form_customer = PartyForm(request.POST, instance=customer)

        if form_address.is_valid():

            address = form_address.save()

            party_address = PartyAddress()
            party_address.account_number = Party.objects.get(account_number=account_number)
            party_address.address_id = address

            party_address.save()

            show_address_form = False

        if form_customer.is_valid():

            form_customer.save()

    address = CustomerAddress(PartyAddress.objects.filter(account_number=account_number))
    form_address = AddressForm()
    form_customer = PartyForm(instance=customer)
    return render(request, 'party/customer/customer.html', {'form_customer': form_customer,
                                                            'address': address,
                                                            'show_address_form': show_address_form,
                                                            'form_address': form_address})


def customer_delete(request, account_number):

    """
        Delete a customer.
    """

    Party.objects.get(account_number=account_number).delete()
    return all_customers(request)

def edit_address(request, id):
    """
        Edit Party address

        ``address``
            Instance of address to be edited.

        ``form_address``
            Model form of Address, linked to customer

        **Template:**

        :template:`party/party_address/edit_address.html`
    """

    address = PartyAddress.objects.get(id=id).address_id
    form_address = AddressForm(instance=address)
    return render(request, 'party/party_address/edit_address.html', {'address': address,
                                                                     'form_address': form_address})


def delete_address(request, id):
    """
        Delete a party address

        ``address``
            address to delete.
    """

    address = PartyAddress.objects.get(id=id)
    party = address.account_number
    address.delete()

    if party.party_type == "C":
        return customer(request, party.account_number)
    else :
        return vendor(request, party.account_number)


def vendors(request):
    """
        Display the customer menu

        **Template:**

        :template:`party/vendor/vendors.html`
    """

    return render(request, 'party/vendor/vendors.html')


def all_vendors(request):
    """
        Display all vendors`.

        ``filter``
            filter used to filter vendors

        ''vendors''
            query set of parties, filtered to show vendors

        **Template:**

        :template:`party/vendor/all_vendors.html`
    """

    filter = PartyFilter(request.GET, Party.objects.filter(party_type='V'))
    vendors = VendorTable(filter.qs)
    RequestConfig(request).configure(vendors)
    return render(request, 'party/vendor/all_vendors.html', {'vendors': vendors,
                                                             'filter': filter})


@transaction.atomic
def vendor_new(request):
    """
        Create a new vendor

        ``form_vendor``
            Model form of Party, for vendor.

        ``form_address``
            Model form of Address, to be linked to vendor

        **Template:**

        :template:`party/vendor/vendor_new.html`
    """

    if request.method == "POST":
        form_vendor = PartyForm(request.POST)
        form_address = AddressForm(request.POST)
        if form_vendor.is_valid() and form_address.is_valid():

            party = form_vendor.save(commit=False)
            party.party_type = 'V'
            party.save()

            address = form_address.save(commit=False)
            address.save()
            party_address = PartyAddress()
            PartyAddress.add_address_ref(party_address, address, party)

            return all_vendors(request)

    else:
        form_vendor = PartyForm()
        form_address = AddressForm()
    return render(request, 'party/vendor/vendor_new.html', {'form_vendor': form_vendor,
                                                            'form_address': form_address})


def vendor(request, account_number):
    """
            View and edit a vendor

            ``show_address_form``
                Boolean dictating if the new address form is displayed.

            ``vendor``
                The party instance of vendor.

            ``form_vendor``
                Model form of Party, for vendor.

            ``form_address``
                Model form of Address, linked to vendor

            **Template:**

            :template:`party/vendor/vendor.html`
    """

    show_address_form = False

    vendor = Party.objects.get(account_number=account_number)

    if request.GET.get('add_address'):
        show_address_form = True

    if request.method == "POST":
        form_address = AddressForm(request.POST)
        form_vendor = PartyForm(request.POST, instance=vendor)

        if form_address.is_valid():

            address = form_address.save()

            party_address = PartyAddress()
            party_address.account_number = Party.objects.get(account_number=account_number)
            party_address.address_id = address

            party_address.save()

            show_address_form = False

        if form_vendor.is_valid():
            form_vendor.save()

    address = CustomerAddress(PartyAddress.objects.filter(account_number=account_number))
    form_vendor = PartyForm(instance=vendor)
    form_address = AddressForm()
    return render(request, 'party/vendor/vendor.html', {'form_vendor': form_vendor,
                                                            'address': address,
                                                            'show_address_form': show_address_form,
                                                            'form_address': form_address})


def vendor_delete(request, account_number):

    """
        Delete a customer.
    """

    Party.objects.get(account_number=account_number).delete()
    return all_vendors(request)


