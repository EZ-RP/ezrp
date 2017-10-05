from django.shortcuts import render
from human_resources.models import Employee
from human_resources.models import Leave
from human_resources.models import Roles
from .modelforms import EmployeeForm
from .modelforms import RoleForm
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'human_resources/humanResources.html')


def employees(request):
    return render(request, 'human_resources/all_employees.html', {'employees': Employee.objects.all()})


def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = EmployeeForm()
    else:
        form = EmployeeForm
    return render(request, 'human_resources/employee_new.html', {'form': form})


def leave(request):
    return render(request, 'human_resources/all_leave.html', {'leave': Leave.objects.all()})


def roles(request):
    return render(request, 'human_resources/all_roles.html', {'roles': Roles.objects.all()})


def role_new(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = RoleForm()
    else:
        form = RoleForm
    return render(request, 'human_resources/role_new.html', {'form': form})


