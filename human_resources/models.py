from django.db import models

"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Roles(models.Model):
    role_description = models.CharField(max_length=100)


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField()
    role_id = models.ForeignKey(Roles)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    payroll_id = models.IntegerField()
    pay_rate = models.IntegerField()


class Leave(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    annual_leave = models.IntegerField()
    sick_leave = models.IntegerField()
    service_leave = models.IntegerField()


class EmployeeRole(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Roles)




