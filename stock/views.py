from django.shortcuts import render
from stock.models import Inventory
from .forms import InvForm
from django_tables2 import RequestConfig
from stock.tables import StockTable
from stock.filters import StockFilter
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


def stock_delete(request, lineid):
    Inventory.objects.get(id=lineid).delete()
    items = StockTable(Inventory.objects.all())
    RequestConfig(request).configure(items)
    return render(request, 'stock/all_available.html', {'available': items})


def stock_edit(request, lineid):

    if request.method == "POST":
        stock = Inventory.objects.get(id=lineid)
        form_stocks = InvForm(request.POST, instance= stock)

        if form_stocks.is_valid():

            form_stocks.save(commit=True)

            form_stock = InvForm()
    else:
        single_stock = Inventory.objects.get(id=lineid)

        form_stock = InvForm(instance=single_stock)

    return render(request, 'stock/edit_stock.html', {'form_stock': form_stock})


def all_stock(request):
    filter = StockFilter(request.GET, Inventory.objects.all())
    stock = StockTable(filter.qs)
    RequestConfig(request, paginate={'per_page': 15}).configure(stock)
    return render(request, 'stock/all_available.html', {'available': stock, 'filter': filter})
