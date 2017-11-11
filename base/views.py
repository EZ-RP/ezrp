from django.http import HttpResponse
from django.shortcuts import render
from base.models import Address
from base.models import PayDetails
from base.models import SystemParameters
from base.tables import *
from .modelforms import AddressForm
from .modelforms import SysParamForm
from base.tables import *


def main(request):
    return render(request, 'base/main.html')


def general(request):
    return render(request, 'base/general.html')


def about(request):
    return render(request, 'base/about.html')


def all_addresses(request):
    addresses = AddressTable(Address.objects.all())
    return render(request, 'base/all_addresses.html', {'addresses': addresses})


def all_paydetails(request):
    paydetails = PayDetailsTable(PayDetails.objects.all())
    return render(request, 'base/all_payDetails.html', {'paydetails': paydetails})


def pay_details_delete(request, id):
    PayDetails.objects.get(id=id).delete()
    return all_paydetails(request)


def address_new(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = AddressForm()
    else:
        form = AddressForm
    return render(request, 'base/address_new.html', {'form': form})


def all_parameters(request):
    return render(request, 'base/all_parameters.html', {'parameters': SystemParameters.objects.all()})


def parameters_new(request):
    if request.method == "POST":
        form = SysParamForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = SysParamForm()
    else:
        form = SysParamForm
    return render(request, 'base/parameters_new.html', {'form': form})

def splash(request):
    return render(request, 'base/splash.html')