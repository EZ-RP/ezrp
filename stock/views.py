from django.shortcuts import render
from stock.models import Inventory
from .forms import InvForm
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'stock/Stock.html')


def available(request):
    return render(request, 'stock/all_available.html', {'available': Inventory.objects.all()})


def stockform(request):
    form = InvForm()
    return render(request, 'stock/stock_form.html', {'form': form})