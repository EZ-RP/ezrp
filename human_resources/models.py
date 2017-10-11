from django.db import models
from base.models import Address
from base.models import PayDetails

"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Roles(models.Model):
    role_name = models.CharField(max_length=10, default='default')
    role_description = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.role_name,)


class Employee(models.Model):
    PAYROLL_TYPE = (
        ('F', 'Full-Time'),
        ('P', 'Part-time'),
        ('S', 'Salary')
    )
    STATUS_TYPE = (
        ('O', 'Ongoing'),
        ('T', 'Temporary')
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField()
    role_id = models.ForeignKey(Roles)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    payroll_type = models.CharField(max_length=1, choices=PAYROLL_TYPE, default='F')
    pay_rate = models.IntegerField(blank=True)
    phone_number = models.IntegerField(blank=True)
    employment_status = models.CharField(max_length=1, choices=STATUS_TYPE, default='O')

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name,)


class EmployeeAddress(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Related account')
    address_id = models.ForeignKey(Address, verbose_name='Related address')

    def add_address_ref(self, address: Address, employee: Employee):
        self.employee_id = employee
        self.address_id = address
        self.save()


class EmployeePayDetails(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Related account')
    pay_details_id = models.ForeignKey(PayDetails, verbose_name='Related pay_details')

    def add_address_ref(self, pay_details: PayDetails, employee: Employee):
        self.employee_id = employee
        self.pay_details_id = pay_details
        self.save()


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
