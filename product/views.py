from django.shortcuts import render
from product.models import Item
from django.http import HttpResponse
from .forms import ProductForm
from product.tables import ProductTable
from stock.models import *
from product.models import *
# Create your views here.


def product_new(request):
    if request.method == "POST":
        form_product = ProductForm(request.POST)
        if form_product.is_valid():
            prod = form_product.save(commit=False)
            prod.item_number = Item.get_next_id(prod)
            prod.save()
            stck = Inventory(item_id=prod)
            stck.save()
    else:
        form_product = ProductForm()
    return render(request, 'product/product_new.html', {'form_product': form_product})


def product(request):
    prodtable = ProductTable(Item.objects.all())

    return render(request, 'product/product.html', {
        'prodtable': prodtable
    })


def edit_product(request, id):
    product = Item.objects.get(id=id)
    form_product = ProductForm(instance=product)
    return render(request, 'product/product_new.html', {'form_product': form_product})
