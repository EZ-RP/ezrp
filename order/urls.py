from django.conf.urls import url
from . import views

urlpatterns = [
    # Main Page
    url(r'^orders/$', views.orders, name='orders'),
    # sales urls
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^sales/all_sales/$', views.all_sales, name='all_sales'),
    url(r'^sales/sale-new/$', views.sale_new, name='sale_new'),
    url(r'^sales/sale-view/$', views.sale_view, name='sale_view'),
    url(r'^sales/all_saleslines/$', views.all_saleslines, name='all_saleslines'),
    url(r'^sales/saleline-new/$', views.saleline_new, name='saleline_new'),
    url(r'^sales/(?P<order_number>\w+)/$', views.sale, name='sale'),
    url(r'^sales/edit/(?P<order_number>\d+)/$', views.sale_edit, name='sale_edit'),
    url(r'^sales/delete/(?P<order_number>\d+)/$', views.sale_delete, name='sale_delete'),
    # url(r'^sales/edit/(?P<order_number>\d+)/$', views.sale_edit, name='salesline_edit'),
    url(r'^sales/delete/(?P<id>\d+)/$', views.salesline_delete, name='salesline_delete'),

    # Purchase urls
    url(r'^purchases/$', views.purchases, name='purchases'),
    url(r'^purchases/all_purchases/$', views.all_purchases, name='all_purchases'),

    # Production urls
    url(r'^production/$', views.production, name='production'),
    url(r'^production/all_production/$', views.all_production, name='all_production'),

    # Discount urls
    url(r'^orderSetup/$', views.setup, name='setup'),
    url(r'^orderSetup/all_discounts/$', views.all_discounts, name='all_discounts'),
    url(r'^orderSetup/new-discount/$', views.new_discount, name='new_discount')
]
