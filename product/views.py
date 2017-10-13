from django.shortcuts import render
from product.models import Item
from django.http import HttpResponse
from .forms import ProductForm
# Create your views here.

def product_new(request):
    if request.method == "POST":
        form_product = ProductForm(request.POST)
        if form_product.is_valid():
            prod = form_product.save(commit=False)
            prod.save()
    else:
        form_product = ProductForm()
    return render(request, 'product/product_new.html', {'form_product': form_product})

def product(request):
    return render(request, 'product/product.html', {'product': Item.objects.all()})
