from django import forms
from human_resources.models import *


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('start_date', 'first_name', 'middle_name', 'last_name', 'date_of_birth',
                  'phone_number', 'employment_status', 'role_id', 'payroll_type', 'pay_rate')


class RoleForm(forms.ModelForm):

            class Meta:
                model = Roles
                fields = ('role_name', 'role_description',)


class PayForm(forms.ModelForm):
    class Meta:
        model = Payday
        fields = ('employee_id', 'start_pay_date', 'end_pay_date', 'hours')
