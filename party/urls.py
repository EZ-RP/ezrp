from django.conf.urls import url
from . import views

urlpatterns = [
    # Customer URL patterns
    url(r'^customers/$', views.customers, name='customers'),
    url(r'^customers/all_customers/$', views.all_customers, name='all_customers'),
    url(r'^customers/new/$', views.customer_new, name='customer_new'),
    url(r'^customers/(?P<account_number>\w+)/$', views.customer, name='customer'),
    url(r'^customers/delete/(?P<account_number>\w+)/$', views.customer_delete, name='customer_delete'),


    # Vendor URL patterns
    url(r'^vendors/$', views.vendors, name='vendors'),
    url(r'^vendors/all_vendors/$', views.all_vendors, name='all_vendors'),
    url(r'^vendors/new/$', views.vendor_new, name='vendor_new'),
    url(r'^vendors/(?P<account_number>\w+)/$', views.vendor, name='vendor'),
    url(r'^vendors/delete/(?P<account_number>\w+)/$', views.vendor_delete, name='vendor_delete'),


    # Party address URL patterns
    url(r'^address/(?P<id>\w+)/$', views.edit_address, name='edit_address'),
    url(r'^address/delete/(?P<id>\w+)/$', views.delete_address, name='delete_address'),

]