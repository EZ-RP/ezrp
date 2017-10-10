from django.http import HttpResponse
from django.shortcuts import render
from base.models import Address
from base.models import PayDetails
from base.models import AttributeType
from base.models import AttributeValue
from base.models import SystemParameters
from .modelforms import AddressForm
from .modelforms import SysParamForm


def main(request):
    return render(request, 'base/main.html')


def general(request):
    return render(request, 'base/general.html')


def about(request):
    return render(request, 'base/about.html')


def all_addresses(request):
    return render(request, 'base/all_addresses.html', {'addresses': Address.objects.all()})


def all_paydetails(request):
    return render(request, 'base/all_payDetails.html', {'paydetails': PayDetails.objects.all()})

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


# DS: removed until post release upgrade
def all_attributetypes(request):
    return render(request, 'base/all_attributeTypes.html', {'attributetypes': AttributeType.objects.all()})


def all_attributevalues(request):
    return render(request, 'base/all_attributeValues.html', {'attributevalues': AttributeValue.objects.all()})


def parameters_new(request):
    if request.method == "POST":
        form = SysParamForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = SysParamForm()
    else:
        form = SysParamForm
    return render(request, 'base/parameters_new.html', {'form': form})
