from django.db import transaction
from django.shortcuts import render
from human_resources.models import Employee, Leave, Roles, Payday, EmployeeAddress, EmployeePayDetails
from .forms import EmployeeForm, RoleForm, PayForm, LeaveForm
from base.modelforms import AddressForm, PayDetailsForm
from django.http import HttpResponse
from django_tables2 import RequestConfig
from human_resources.tables import *

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

            leave = Leave()
            leave.employee_id = employee
            leave.save()
    else:
        form_employee = EmployeeForm()
        form_address = AddressForm()
        form_pay_details = PayDetailsForm()
    return render(request, 'human_resources/Employee/employee_new.html', {'form_employee': form_employee,
                                                                 'form_address': form_address,
                                                                 'form_pay_details': form_pay_details})


def employee(request, id):
    single_employee = Employee.objects.get(id=id)
    form_employee = EmployeeForm(instance=single_employee)
    return render(request, 'human_resources/Employee/employee.html', {'form_employee': form_employee})


def employee_edit(request, id):

    if request.method == "POST":

        form_employees = EmployeeForm(request.POST)

        if form_employees.is_valid():

            employee_line = form_employees.save(commit=False)
            employee_line.pk = id
            employee_line.save()

            form_employee = EmployeeForm(instance=employee_line)
    else:
        single_employee = Employee.objects.get(id=id)

        form_employee = EmployeeForm(instance=single_employee)

    return render(request, 'human_resources/Employee/employee.html', {'form_employee': form_employee})


def employee_delete(request, id):
    Employee.objects.get(id=id).delete()
    single_employee = EmployeeTable(Employee.objects.all())
    RequestConfig(request).configure(single_employee)
    return render(request, 'human_resources/Employee/all_employees.html', {'employees': single_employee})


def pay(request):
    pay = PayTable(Payday.objects.all())
    return render(request, 'human_resources/Pay/all_pay.html', {'pay': pay})


@transaction.atomic
def pay_new(request):
    if request.method == "POST":
        form_pay = PayForm(request.POST)
        if form_pay.is_valid():
            new_pay = form_pay.save(commit=False)

            eid = new_pay.employee_id.id
            emp = Employee.objects.get(id=eid)
            rate = emp.pay_rate
            hours = new_pay.hours
            new_pay.cost = hours * rate

            new_pay.save()

            #update Leave Acurrual collumns
            full_time_weekly_hours_constant = 38
            annual_leave_constant = 2.923
            sick_leave_constant = 1.461
            service_leave_constant = 0.8667

            emp_leave = Leave.objects.get(employee_id=new_pay.employee_id)
            emp_leave.total_weeks_worked = emp_leave.total_weeks_worked + 1
            num_completed_weeks = emp_leave.total_weeks_worked
            emp_leave.total_hours_worked = emp_leave.total_hours_worked + hours
            total_hours_worked = emp_leave.total_hours_worked

            total_hours_sick_leave = 0
            total_hours_annual_leave = 0

            if(emp.payroll_type == "F"):
                total_hours_sick_leave = num_completed_weeks * sick_leave_constant
                total_hours_annual_leave = num_completed_weeks * annual_leave_constant
                total_service_leave = 0
                if(num_completed_weeks / 52 > 7.00 and num_completed_weeks / 52 < 10.00 ):
                    total_service_leave = num_completed_weeks * service_leave_constant
                elif(num_completed_weeks / 52 > 10.00):
                    total_service_leave = (num_completed_weeks / 52) * service_leave_constant
                emp_leave.service_leave_accrued = total_service_leave
            elif(emp.payroll_type == "P"):
                avg_hours_worked_per_week = total_hours_worked / num_completed_weeks

                total_hours_worked_per_week_sick_leave = avg_hours_worked_per_week / full_time_weekly_hours_constant * sick_leave_constant
                total_hours_worked_per_week_annual_leave = avg_hours_worked_per_week / full_time_weekly_hours_constant * sick_leave_constant

                total_hours_sick_leave = total_hours_worked_per_week_sick_leave * num_completed_weeks
                total_hours_annual_leave = total_hours_worked_per_week_annual_leave * num_completed_weeks

            emp_leave.sick_leave_accrued = total_hours_sick_leave - emp_leave.sick_leave_taken
            emp_leave.annual_leave_accrued = total_hours_annual_leave - emp_leave.annual_leave_taken

            emp_leave.save()

    else:
        form_pay = PayForm()
    return render(request, 'human_resources/Pay/pay_new.html', {'form_pay': form_pay})


def leave(request):
    leaves = LeaveTable(Leave.objects.all())
    RequestConfig(request).configure(leaves)
    return render(request, 'human_resources/Leave/all_leave.html', {'leave': leaves})


def leave_edit(request, id):

    if request.method == "POST":

        form_leave = LeaveForm(request.POST)

        if form_leave.is_valid():
            leave_line = Leave.objects.get(id=id)
            add_leave_line = form_leave.save(commit=False)
            leave_line.sick_leave_taken = leave_line.sick_leave_taken + add_leave_line.sick_leave_taken
            leave_line.annual_leave_taken = leave_line.annual_leave_taken + add_leave_line.annual_leave_taken
            leave_line.sick_leave_accrued = leave_line.sick_leave_accrued - add_leave_line.sick_leave_taken
            leave_line.annual_leave_accrued = leave_line.annual_leave_accrued - add_leave_line.annual_leave_taken
            leave_line.pk = id

            leave_line.save()

            form_leave = LeaveForm(instance=leave_line)
    else:
        single_employee = Leave.objects.get(id=id)

        form_leave = LeaveForm(instance=single_employee)

    return render(request, 'human_resources/Leave/leave.html', {'form_leave': form_leave})



def roles(request):
    roles = RolesTable(Roles.objects.all())
    return render(request, 'human_resources/Role/all_roles.html', {'roles': roles})


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
