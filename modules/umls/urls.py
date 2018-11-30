from django.conf.urls import *
from modules.umls import views

urlpatterns = [
    url(r'^process$', views.process, name='process'),
]
