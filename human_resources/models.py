from django.db import models
from base.models import Address
from base.models import PayDetails

"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Roles(models.Model):
    role_name = models.CharField(max_length=10, default='default', help_text="An Employees Role Name.")
    role_description = models.CharField(max_length=100, help_text="An Employees Role Description.")

    def __str__(self):
        return '%s' % (self.role_name,)


class Employee(models.Model):
    PAYROLL_TYPE = (
        ('F', 'Full-Time'),
        ('P', 'Part-time')
    )
    STATUS_TYPE = (
        ('O', 'Ongoing'),
        ('T', 'Temporary'),
        ('D', 'Discontinued')
    )
    first_name = models.CharField(max_length=30, help_text="An Employees First Name.")
    last_name = models.CharField(max_length=30, help_text="An Employees Last Name.")
    middle_name = models.CharField(max_length=30, blank=True, help_text="An Employees Last Name.")
    date_of_birth = models.DateField(help_text="An Employees Date of Birth.")
    role_id = models.ForeignKey(Roles, help_text="An Employees Role.")
    start_date = models.DateField(help_text="The Date An Employee Started.")
    end_date = models.DateField(null=True, blank=True, help_text="The Date An Employee Ended.")
    payroll_type = models.CharField(max_length=1, choices=PAYROLL_TYPE, default='F', help_text="An Employees Payroll Type.")
    pay_rate = models.FloatField(null=True, blank=True, help_text="An Employees Pay Rate Per Hour.")
    phone_number = models.CharField(max_length=15, null=True, blank=True, help_text="An Employees Phone Number.")
    employment_status = models.CharField(max_length=1, choices=STATUS_TYPE, default='O', help_text="An Employees Employment Status.")

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name,)


class EmployeeAddress(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Related account', help_text="An Employees ID.")
    address_id = models.ForeignKey(Address, verbose_name='Related address', help_text="An Employees Address ID.")

    def add_address_ref(self, address: Address, employee: Employee):
        self.employee_id = employee
        self.address_id = address
        self.save()


class EmployeePayDetails(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Related account', help_text="An Employees ID.")
    pay_details_id = models.ForeignKey(PayDetails, verbose_name='Related pay_details', help_text="An Employees PayDetails ID.")

    def add_pay_detail_ref(self, pay_details: PayDetails, employee: Employee):
        self.employee_id = employee
        self.pay_details_id = pay_details
        self.save()


class Leave(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, help_text="An Employees ID.")
    total_weeks_worked = models.IntegerField(default=0, help_text="An Employees Leave Total Weeks Worked.")
    total_hours_worked = models.IntegerField(default=0, help_text="An Employees Leave Total Hours Worked.")
    annual_leave_accrued = models.IntegerField(default=0, help_text="An Employees Leave Annual Leave Accrued.")
    annual_leave_taken = models.IntegerField(default=0, help_text="An Employees Leave Annual Leave Taken.")
    sick_leave_accrued = models.IntegerField(default=0, help_text="An Employees Leave Sick Leave Accrued.")
    sick_leave_taken = models.IntegerField(default=0, help_text="An Employees Leave Sick Leave Taken.")
    service_leave_accrued = models.IntegerField(default=0, help_text="An Employees Leave Service Leave Taken.")


class Payday(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, help_text="An Employees ID.")
    start_pay_date = models.DateField(help_text="An Employees Pay Week Start Date.")
    end_pay_date = models.DateField(help_text="An Employees Pay Week End Date.")
    hours = models.FloatField(help_text="An Employees Pay Week Total Hours Worked.")
    cost = models.FloatField(default=0, help_text="An Employees Pay Week Total Cost.")

