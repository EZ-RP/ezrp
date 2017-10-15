from django.conf.urls import url
from . import views

urlpatterns = [
    # sales urls
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^sales/all_sales/$', views.all_sales, name='all_sales'),
    url(r'^sales/sale-new/$', views.sale_new, name='sale_new'),
    url(r'^sales/sale-view/$', views.sale_view, name='sale_view'),
    url(r'^sales/single_salesOrders$', views.single_sales, name='single_sales'),
    url(r'^sales/all_saleslines/$', views.all_saleslines, name='all_saleslines'),
    url(r'^sales/saleline-new/$', views.saleline_new, name='saleline_new'),
    url(r'^sales/(?P<order_number>\w+)/$', views.sale, name='sale'),
    url(r'sales/edit/(?P<order_number>\d+)/', views.sale_edit, name='sale_edit'),
    url(r'sales/delete/(?P<order_number>\d+)/', views.sale_delete, name='sale_delete'),

    # Purchase urls
    url(r'^purchases/$', views.purchases, name='purchases'),
    url(r'^purchases/all_purchases/$', views.all_purchases, name='all_purchases'),

    # Discount urls
    url(r'^orderSetup/$', views.setup, name='setup'),
    url(r'^sales/all_discounts/$', views.all_discounts, name='all_discounts'),
    url(r'^sales/new-discount/$', views.new_discount, name='new_discount')
]
