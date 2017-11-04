from django.shortcuts import render
from stock.models import Inventory
from .forms import InvForm
from django_tables2 import RequestConfig
from stock.tables import StockTable
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'stock/Stock.html')


def available(request):
    items = StockTable(Inventory.objects.all())
    RequestConfig(request).configure(items)
    return render(request, 'stock/all_available.html', {'available': items})
    # return render(request, 'stock/all_available.html', {'available': Inventory.objects.all()})


def stockform(request):
    if request.method == "POST":
        form = InvForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InvForm()
    return render(request, 'stock/stock_form.html', {'form': form})


def stock_delete(request, item_id):
    Inventory.objects.get(item_id=item_id).delete()
    items = StockTable(Inventory.objects.all())
    RequestConfig(request).configure(items)
    return render(request, 'stock/all_available.html', {'available': items})


