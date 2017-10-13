from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^purchases/$', views.purchases, name='purchases'),
    url(r'^orderSetup/$', views.setup, name='setup'),
    url(r'^sales/all_sales/$', views.all_sales, name='all_sales'),
    url(r'^purchases/all_purchases/$', views.all_purchases, name='all_purchases'),
    url(r'^sales/sale-new/$', views.sale_new, name='sale_new'),
    url(r'^sales/sale-view/$', views.sale_view, name='sale_view'),
    url(r'^sales/single_salesOrders$', views.single_sales, name='single_sales'),
    url(r'^sales/all_saleslines/$', views.all_saleslines, name='all_saleslines'),
    url(r'^sales/saleline-new/$', views.saleline_new, name='saleline_new'),
    url(r'^customers/(?P<order_number>\w+)/$', views.sale, name='sale')

]