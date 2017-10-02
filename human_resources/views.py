from django.shortcuts import render
from human_resources.models import Employee
from human_resources.models import Leave
from human_resources.models import Roles
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'human_resources/humanResources.html')


def employees(request):
    return render(request, 'human_resources/all_employees.html', {'employees': Employee.objects.all()})


def leave(request):
    return render(request, 'human_resources/all_leave.html', {'leave': Leave.objects.all()})


def roles(request):
    return render(request, 'human_resources/all_roles.html', {'roles': Roles.objects.all()})
