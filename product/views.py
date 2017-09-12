from django.shortcuts import render
from product.models import Item
from django.http import HttpResponse
# Create your views here.


def product(request):
    return render(request, 'product/product.html', {'product': Item.objects.all()})
