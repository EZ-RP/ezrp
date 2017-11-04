from django.db import transaction
from django.shortcuts import render
from party.models import Party, PartyAddress
from party.tables import *
from .forms import PartyForm
from base.modelforms import AddressForm
from django_tables2 import RequestConfig
from party.filters import PartyFilter


def all_customers(request):
    filter = PartyFilter(request.GET, Party.objects.filter(party_type='C'))
    customers = CustomerTable(filter.qs)
    RequestConfig(request).configure(customers)
    return render(request, 'party/customer/all_customers.html', {'customers': customers,
                                                                 'filter': filter})


def customers(request):
    return render(request, 'party/customer/customers.html')


@transaction.atomic
def customer_new(request):
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


    else:
        form_customer = PartyForm()
        form_address = AddressForm()
    return render(request, 'party/customer/customer_new.html', {'form_customer': form_customer,
                                                                'form_address': form_address})


def customer(request, account_number):

    show_address_form = False

    if request.GET.get('add_address'):
        show_address_form = True

    if request.method == "POST":
        form_address = AddressForm(request.POST)

        if form_address.is_valid():

            address = form_address.save()

            party_address = PartyAddress()
            party_address.account_number = Party.objects.get(account_number=account_number)
            party_address.address_id = address

            party_address.save()

            show_address_form = False

    customer = Party.objects.get(account_number=account_number)
    address = CustomerAddress(PartyAddress.objects.filter(account_number=account_number))
    form_customer = PartyForm(instance=customer)
    form_address = AddressForm()
    return render(request, 'party/customer/customer.html', {'form_customer': form_customer,
                                                            'address': address,
                                                            'show_address_form': show_address_form,
                                                            'form_address': form_address})


def customer_delete(request, account_number):
    Party.objects.get(account_number=account_number).delete()
    return all_customers(request)

def edit_address(request, id):
    address = PartyAddress.objects.get(id=id).address_id
    form_address = AddressForm(instance=address)
    return render(request, 'party/customer/edit_address.html', {'address': address,
                                                                'form_address': form_address})


def delete_address(request, id):
    address = PartyAddress.objects.get(id=id)
    cust = address.account_number
    address.delete()
    return customer(request, cust.account_number)


def vendors(request):
    return render(request, 'party/customer/customers.html')



