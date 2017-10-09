from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.product, name='product_Main'),
    url(r'^product/product_new$', views.product_new, name='product_new')
]