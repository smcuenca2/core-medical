from django.conf.urls import *
from modules.edge import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.process, name='process'),
    url(r'^process_umls$', views.process_umls, name='process_umls'),
    url(r'^process_cnmb$', views.process_cnmb, name='process_cnmb'),
    url(r'^upload_csv_umls$', views.upload_csv_umls, name='upload_csv_umls'),
    url(r'^upload_csv_cnmb$', views.upload_csv_cnmb, name='upload_csv_cnmb'),
]
