from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='stock_Main'),
    url(r'^all_available/$', views.available, name='all_available'),
    url(r'^stock_form/$', views.stockform, name='stock_form'),
]