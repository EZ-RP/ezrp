from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='base_Main'),
    url(r'^main/$', views.splash, name='base_Splash'),
    url(r'^general/$', views.general, name='base_General'),
    url(r'^about/$', views.about, name='about'),
    url(r'^all_addresses/$', views.all_addresses, name='all_addresses'),
    url(r'^all_paydetails/$', views.all_paydetails, name='all_paydetails'),
    url(r'^paydetails-new/$', views.pay_details_new, name='pay_details_new'),
    url(r'^delete_pay_details/(?P<id>\w+)/$', views.pay_details_delete, name='pay_details_delete'),
    url(r'^address-new/$', views.address_new, name='address_new'),
    url(r'^all_parameters/$', views.all_parameters, name='all_parameters'),
    url(r'^parameters-new/$', views.parameters_new, name='parameters_new')
]