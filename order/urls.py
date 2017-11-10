from django.conf.urls import url
from . import views

urlpatterns = [
    # Main Page
    url(r'^orders/$', views.orders, name='orders'),

    # sales urls
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^sales/all_sales/$', views.all_sales, name='all_sales'),
    url(r'^sales/sale-new/$', views.sale_new, name='sale_new'),
    url(r'^sales/all_saleslines/$', views.all_saleslines, name='all_saleslines'),
    url(r'^sales/(?P<order_number>\w+)/$', views.sale, name='sale'),
    url(r'^sales/edit/(?P<order_number>\d+)/$', views.sale_edit, name='sale_edit'),
    url(r'^sales/all_sales/delete/(?P<order_number>\d+)/$', views.sale_delete, name='sale_delete'),
    url(r'^sales/all_saleslines/delete/(?P<sid>\d+)/$', views.salesline_delete, name='salesline_delete'),

    # Purchase urls
    url(r'^purchases/$', views.purchases, name='purchases'),
    url(r'^purchases/all_purchases/$', views.all_purchases, name='all_purchases'),
    url(r'^purchases/purch-new/$', views.purch_new, name='purch_new'),
    url(r'^purchases/all_purchlines/$', views.all_purchlines, name='all_purchlines'),
    url(r'^purchases/(?P<order_number>\w+)/$', views.purch, name='purch'),
    url(r'^purchases/edit/(?P<order_number>\d+)/$', views.purch_edit, name='purch_edit'),
    url(r'^purchases/all_purchases/delete/(?P<order_number>\d+)/$', views.purch_delete, name='purch_delete'),
    url(r'^purchases/all_purchlines/delete/(?P<pid>\d+)/$', views.purchline_delete, name='purchline_delete'),

    # Production urls
    url(r'^production/$', views.production, name='production'),
    url(r'^production/all_production/$', views.all_production, name='all_production'),
    url(r'^production/prod-new/$', views.prod_new, name='prod_new'),
    url(r'^production/all_prodlines/$', views.all_prodlines, name='all_prodlines'),
    url(r'^production/(?P<order_number>\w+)/$', views.prod, name='prod'),
    url(r'^production/edit/(?P<order_number>\d+)/$', views.prod_edit, name='prod_edit'),
    url(r'^production/all_production/delete/(?P<order_number>\d+)/$', views.prod_delete, name='prod_delete'),
    url(r'^production/all_prodlines/delete/(?P<mid>\d+)/$', views.prodline_delete, name='prodline_delete'),

    # Discount urls
    url(r'^orderSetup/$', views.setup, name='setup'),
    url(r'^orderSetup/all_discounts/$', views.all_discounts, name='all_discounts'),
    url(r'^orderSetup/new-discount/$', views.new_discount, name='new_discount'),
    url(r'^orderSetup/edit-discount/(?P<lineid>\d+)/$', views.discount_edit, name='discount_edit'),
    url(r'^orderSetup/delete-discount/(?P<lineid>\d+)/$', views.discount_delete, name='discount_delete'),
]
