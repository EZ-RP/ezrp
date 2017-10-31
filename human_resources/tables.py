from django_tables2.utils import A  # alias for Accessor
# from django_tables2 import tables
import django_tables2 as tables
from human_resources.models import Employee

# Employees custom tables


class EmployeeTable(tables.Table):
    #Employee = tables.LinkColumn('employee,);

    class Meta:
        attrs = {'class': 'paleblue'}
        model = Employee

