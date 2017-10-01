from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^purchases/$', views.purchases, name='purchases'),
    url(r'^orderSetup/$', views.setup, name='setup'),
    url(r'^sales/all_sales/$', views.all_sales, name='all_sales'),
    url(r'^purchases/all_purchases/$', views.all_purchases, name='all_purchases')
    #url(r'^sales/$', views.test(), name='test')
]