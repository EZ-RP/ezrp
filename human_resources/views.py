from django.shortcuts import render
from human_resources.models import Employee
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'human_resources/humanResources.html')


def employees(request):
    return render(request, 'human_resources/all_employees.html', {'employees': Employee.objects.all()})
