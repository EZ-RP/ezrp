from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='base_Main'),
    url(r'^general/$', views.general, name='base_General'),
    url(r'^about/$', views.about, name='about'),
    url(r'^all_addresses/$', views.all_addresses, name='all_addresses'),
    url(r'^all_paydetails/$', views.all_paydetails, name='all_paydetails'),
    url(r'^all_attributetypes/$', views.all_attributetypes, name='all_attributetypes'),
    url(r'^all_attributevalues/$', views.all_attributevalues, name='all_attributevalues'),
    url(r'^address-new/$', views.address_new, name='address_new'),
    url(r'^all_parameters/$', views.all_parameters, name='all_parameters'),
    url(r'^parameters-new/$', views.parameters_new, name='parameters_new')
]