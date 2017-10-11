from django import forms
from human_resources.models import *


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('start_date', 'first_name', 'middle_name', 'last_name',
                  'date_of_birth', 'role_id', 'payroll_id', 'pay_rate')


class RoleForm(forms.ModelForm):

            class Meta:
                model = Roles
                fields = ('role_name', 'role_description',)
