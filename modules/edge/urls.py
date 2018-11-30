from django.conf.urls import *
from modules.edge import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.process, name='process'),
    url(r'^process_umls$', views.process_umls, name='process_umls'),
]
