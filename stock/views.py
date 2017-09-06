from django.shortcuts import render
from stock.models import Inventory
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'stock/Stock.html')


def available(request):
    return render(request, 'stock/all_available.html', {'available': Inventory.objects.all()})
