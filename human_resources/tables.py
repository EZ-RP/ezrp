from django_tables2.utils import A  # alias for Accessor
# from django_tables2 import tables
import django_tables2 as tables
from human_resources.models import Employee, Leave

# Employees custom tables


class EmployeeTable(tables.Table):
    edit_link = tables.LinkColumn('employee_edit', args=[A('pk')],
                                  verbose_name='Edit Employee', text='Edit', accessor='pk',
                                  attrs={'class': 'edit_link'})
    delete_link = tables.LinkColumn('employee_delete', args=[A('pk')],
                                    verbose_name='Delete Employee', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_link'})
    class Meta:
        attrs = {'class': 'tableStyle'}
        model = Employee


class LeaveTable(tables.Table):
    edit_link = tables.LinkColumn('leave_edit', args=[A('pk')],
                                  verbose_name='Edit Leave', text='Edit', accessor='pk',
                                  attrs={'class': 'edit_link'})

    class Meta:
        attrs = {'class': 'tableStyle'}
        model = Leave
