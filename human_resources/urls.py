from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='humanResources_Main'),
    url(r'^all_employees/$', views.employees, name='all_employees'),
]
