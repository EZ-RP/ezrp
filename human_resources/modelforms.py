from django import forms
from human_resources.models import Employee
from human_resources.models import Roles


# Create the form class.
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('start_date', 'first_name', 'middle_name', 'last_name',
                  'date_of_birth', 'role_id', 'payroll_id', 'pay_rate')


# Create the form class.
class RoleForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ('role_description',)
