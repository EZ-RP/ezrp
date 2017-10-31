from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='humanResources_Main'),

    #Employee
    url(r'^Employee/all_employees/$', views.employees, name='all_employees'),
    url(r'^Employee/employee_new/$', views.employee_new, name='employee_new'),
    url(r'^Employee/(?P<first_name>\w+)/$', views.employee, name='employee'),
    url(r'Employee/delete/(?P<first_name>\d+)/', views.employee_delete, name='employee_delete'),

    #Pay
    url(r'^Pay/all_pay/$', views.pay, name='all_pay'),
    url(r'^Pay/pay_new/$', views.pay_new, name='pay_new'),

    #Leave
    url(r'^all_leave/$', views.leave, name='all_leave'),

    #Roles
    url(r'^Role/role_new/$', views.role_new, name='role_new'),
    url(r'^Role/all_roles/$', views.roles, name='all_roles'),

]
