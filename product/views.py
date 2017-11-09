from django.shortcuts import render
from product.models import Item
from django.http import HttpResponse
from django_tables2 import RequestConfig
from .forms import ProductForm
from product.tables import ProductTable
from stock.models import *
from product.models import *
from product.filters import ProductFilter
# Create your views here.


def product_new(request):
    if request.method == "POST":
        form_product = ProductForm(request.POST)
        if form_product.is_valid():
            prod = form_product.save(commit=False)
            prod.item_number = 1
            prod.save()
            stck = Inventory(item_id=prod, available_qty=0,reserved_qty=0, ordered_qty=0)
            stck.save()

            #return all_product(request)
    else:
        form_product = ProductForm()
    return render(request, 'product/product_new.html', {'form_product': form_product})


def product(request):
    filter = ProductFilter(request.GET, Item.objects.all())
    prod = ProductTable(filter.qs)
    RequestConfig(request).configure(prod)
    return render(request, 'product/product.html', {'prodtable': prod, 'filter': filter})


def edit_product(request, lineid):
    if request.method == "POST":
        prod = Item.objects.get(id=lineid)
        form_prods = ProductForm(request.POST, instance= prod)

        if form_prods.is_valid():

            form_prods.save(commit=True)

            return all_product(request)
    else:
        single_prod = Item.objects.get(id=lineid)

        form_prod = ProductForm(instance=single_prod)

    return render(request, 'product/edit_product.html', {'form_prod': form_prod})


def all_product(request):
    filter = ProductFilter(request.GET, Item.objects.all())
    product = ProductTable(filter.qs)
    RequestConfig(request).configure(product)
    return render(request, 'product/product.html', {'prodtable': product, 'filter': filter})


