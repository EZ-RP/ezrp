from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='stock_Main'),
    url(r'^all_available/$', views.available, name='all_available'),
    url(r'^stock_form/$', views.stockform, name='stock_form'),
    url(r'^stock/delete/(?P<item_id>\d+)/$', views.stock_delete, name='stock_delete'),
    # url(r'^stock/edit/(?P<item_id>\d+)/$', views.stock_edit, name='stock_edit'),

]