from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product, name='product_Main'),
    url(r'^product_new/$', views.product_new, name='product_new'),
    url(r'^product_edit/(?P<id>\w+)/$', views.edit_product, name='edit_product')
]