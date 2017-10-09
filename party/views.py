from django.db import transaction
from django.shortcuts import render
from party.models import Party, PartyAddress
from .forms import PartyForm
from base.modelforms import AddressForm


def all_customers(request):
    customers = Party.objects.filter(party_type='C')
    return render(request, 'party/customer/all_customers.html', {'customers': customers})


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
    return render(request, 'party/customer/customer_new.html', {'form_customer': form_customer, 'form_address': form_address})


def vendors(request):
    return render(request, 'party/customer/customers.html')



