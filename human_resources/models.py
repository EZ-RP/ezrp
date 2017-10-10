from django.db import models
from base.models import Address
from base.models import PayDetails

"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Roles(models.Model):
    role_name = models.CharField(max_length=10)
    role_description = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.role_name,)


class Employee(models.Model):
    PAYROLL_ID = (
        ('C', 'Casual'),
        ('I', 'Independent'),
        ('S', 'Salary')
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField()
    role_id = models.ForeignKey(Roles)
    address = models.ForeignKey(Address)
    pay_details = models.ForeignKey(PayDetails)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    payroll_id = models.CharField(max_length=1, choices=PAYROLL_ID)
    pay_rate = models.IntegerField()


class Leave(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    annual_leave = models.IntegerField()
    sick_leave = models.IntegerField()
    service_leave = models.IntegerField()


class Payday(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_pay_date = models.DateField()
    end_pay_date = models.DateField()
    hours = models.FloatField()
    pay = models.FloatField()

    def pay(self):
        rate = self.employee_id.pay_rate
        return rate*self.hours
