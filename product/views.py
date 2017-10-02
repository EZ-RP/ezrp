from django.shortcuts import render
from product.models import Item
from django.http import HttpResponse
from .forms import ProductForm
# Create your views here.

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
    else:
        form = PartyForm()
    return render(request, 'party/customer/customer_new.html', {'form': form})
def product(request):
    return render(request, 'product/product.html', {'product': Item.objects.all()})
