from django.shortcuts import render
from order.models import Order
from django.http import HttpResponse
# Create your views here.

def sales(request):
    return render(request, 'order/Sales/sales.html')


def purchases(request):
    return render(request, 'order/Purchases/purchases.html')


def all_sales(request):
    return render(request, 'order/Sales/all_salesOrders.html', {'sales': Order.objects.all()})


def all_purchases(request):
    return render(request, 'order/Purchases/all_purchaseOrders.html', {'purchases': Order.objects.all()})
