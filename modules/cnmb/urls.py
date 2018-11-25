from django.conf.urls import *
from modules.cnmb import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.process, name='process'),
]
