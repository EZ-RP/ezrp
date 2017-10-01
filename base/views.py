from django.http import HttpResponse
from django.shortcuts import render
from base.models import Address
from base.models import PayDetails
from base.models import AttributeType
from base.models import AttributeValue


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


def all_attributetypes(request):
    return render(request, 'base/all_attributeTypes.html', {'attributetypes': AttributeType.objects.all()})


def all_attributevalues(request):
    return render(request, 'base/all_attributeValues.html', {'attributevalues': AttributeValue.objects.all()})

