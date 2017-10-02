from django.shortcuts import render
from party.models import Party
from django.http import HttpResponse
from .forms import PartyForm


def all_customers(request):
    return render(request, 'party/customer/all_customers.html', {'customers': Party.objects.all()})


def customers(request):
    return render(request, 'party/customer/customers.html')


def customer_new(request):
    if request.method == "POST":
        form = PartyForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.party_type = 'C'
            party.save()
    else:
        form = PartyForm()
    return render(request, 'party/customer/customer_new.html', {'form': form})


def vendors(request):
    return render(request, 'party/customer/customers.html')



