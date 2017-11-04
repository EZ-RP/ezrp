from django.conf.urls import url
from . import views

urlpatterns = [
    # Customer URL patterns
    url(r'^customers/$', views.customers, name='customers'),
    url(r'^customers/all_customers/$', views.all_customers, name='all_customers'),
    url(r'^customers/new/$', views.customer_new, name='customer_new'),
    url(r'^customers/(?P<account_number>\w+)/$', views.customer, name='customer'),
    url(r'^customers/delete/(?P<account_number>\w+)/$', views.customer_delete, name='customer_delete'),
    url(r'^customers/address/(?P<id>\w+)/$', views.edit_address, name='edit_address'),
    url(r'^customers/address/delete/(?P<id>\w+)/$', views.delete_address, name='delete_address'),

]