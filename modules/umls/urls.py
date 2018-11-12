from django.conf.urls import *
from modules.umls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.process_umls, name='process'),
]
