from django.conf.urls import url
from . import views

urlpatterns = [
    # Customer URL patterns
    url(r'^customers/$', views.customers, name='customers'),
    url(r'^customers/all_customers/$', views.all_customers, name='all_customers'),
    url(r'^customers/new/$', views.customer_new, name='customer_new'),

]