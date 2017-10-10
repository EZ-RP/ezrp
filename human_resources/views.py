from django.db import transaction
from django.shortcuts import render
from human_resources.models import Employee, Leave, Roles, Payday, EmployeeAddress, EmployeePayDetails
from .forms import EmployeeForm, RoleForm
from base.modelforms import AddressForm, PayDetailsForm
# Create your views here.


def main(request):
    return render(request, 'human_resources/humanResources.html')


def employees(request):
    return render(request, 'human_resources/all_employees.html', {'employees': Employee.objects.all()})


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
            EmployeePayDetails.add_address_ref(employee_pay_details, address, employee)
    else:
        form_employee = EmployeeForm()
        form_address = AddressForm()
        form_pay_details = PayDetailsForm()
    return render(request, 'human_resources/employee_new.html', {'form_employee': form_employee,
                                                                 'form_address': form_address,
                                                                'form_pay_details': form_pay_details})


def leave(request):
    return render(request, 'human_resources/all_leave.html', {'leave': Leave.objects.all()})


def roles(request):
    return render(request, 'human_resources/all_roles.html', {'roles': Roles.objects.all()})


@transaction.atomic
def role_new(request):
    if request.method == "POST":
        form_role = RoleForm(request.POST)
        if form_role.is_valid():
            role = form_role.save(commit=False)
            role.save()
    else:
        form_role = RoleForm()
    return render(request, 'human_resources/role_new.html', {'form_employee': form_role,})


def pay(request):
    return render(request, 'human_resources/all_pay.html', {'pay': Payday.objects.all()})

