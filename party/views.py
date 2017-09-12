from django.shortcuts import render
from party.models import Party
from django.http import HttpResponse


def all_customers(request):
    return render(request, 'party/customer/all_customers.html', {'customers': product.objects.all()})


def customers(request):
    return render(request, 'party/customer/customers.html')


def vendors(request):
    return render(request, 'party/customer/customers.html')



