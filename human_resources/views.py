from django.db import transaction
from django.shortcuts import render
from human_resources.models import Employee, Leave, Roles, Payday, EmployeeAddress, EmployeePayDetails
from .forms import EmployeeForm, RoleForm, PayForm
from base.modelforms import AddressForm, PayDetailsForm
from django.http import HttpResponse
from django_tables2 import RequestConfig
from human_resources.tables import EmployeeTable

# Create your views here.


def main(request):
    return render(request, 'human_resources/humanResources.html')


#Employees
def employees(request):
    employee = EmployeeTable(Employee.objects.all())
    RequestConfig(request).configure(employee)
    return render(request, 'human_resources/Employee/all_employees.html', {'employees': employee})

@transaction.atomic
def employee_new(request):
    if request.method == "POST":
        form_employee = EmployeeForm(request.POST)
        form_address = AddressForm(request.POST)
        form_pay_details = PayDetailsForm(request.POST)
        if form_employee.is_valid() and form_address.is_valid() and form_pay_details.is_valid():
            employee = form_employee.save(commit=False)
            employee.save()

            address = form_address.save(commit=False)
            address.save()
            employee_address = EmployeeAddress()
            EmployeeAddress.add_address_ref(employee_address, address, employee)

            pay_details = form_pay_details.save(commit=False)
            pay_details.save()
            employee_pay_details = EmployeePayDetails()
            EmployeePayDetails.add_address_ref(employee_pay_details, pay_details, employee)
    else:
        form_employee = EmployeeForm()
        form_address = AddressForm()
        form_pay_details = PayDetailsForm()
    return render(request, 'human_resources/Employee/employee_new.html', {'form_employee': form_employee,
                                                                 'form_address': form_address,
                                                                 'form_pay_details': form_pay_details})


def employee(request, first_name):
    single_employee = Employee.objects.get(first_name=first_name)
    form_employee = EmployeeForm(instance=single_employee)
    return render(request, 'human_resources/Employee/employee.html', {'form_employee': form_employee})

def employee_delete(request, first_name):
    # Order.objects.filter(order_number=order_number).delete()
    Employee.objects.get(first_name=first_name).delete()
    single_employee = EmployeeTable(Employee.objects.all())
    RequestConfig(request).configure(single_employee)
    return render(request, 'human_resources/Employee/all_employees.html', {'employee': single_employee})


def leave(request):
    return render(request, 'human_resources/all_leave.html', {'leave': Leave.objects.all()})


def roles(request):
    return render(request, 'human_resources/Role/all_roles.html', {'roles': Roles.objects.all()})


@transaction.atomic
def role_new(request):
    if request.method == "POST":
        form_role = RoleForm(request.POST)
        if form_role.is_valid():
            role = form_role.save(commit=False)
            role.save()
    else:
        form_role = RoleForm()
    return render(request, 'human_resources/Role/role_new.html', {'form_role': form_role})


def pay(request):
    return render(request, 'human_resources/Pay/all_pay.html', {'pay': Payday.objects.all()})


@transaction.atomic
def pay_new(request):
    if request.method == "POST":
        form_pay = PayForm(request.POST)
        if form_pay.is_valid():
            new_pay = form_pay.save(commit=False)
            new_pay.save()
    else:
        form_pay = PayForm()
    return render(request, 'human_resources/Pay/pay_new.html', {'form_pay': form_pay})
