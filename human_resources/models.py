from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    role_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    payroll_id = models.IntegerField()
    pay_rate = models.IntegerField()

class Leave(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    annual_leave = models.IntegerField()
    sick_leave = models.IntegerField()
    service_leave = models.IntegerField()

class Employee_role(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Roles)

class Roles(models.Model):
    role_description = models.CharField(max_length=100)

