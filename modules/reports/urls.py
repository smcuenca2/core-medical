from django.conf.urls import *
from modules.reports import views

urlpatterns = [
    url(r'cnmb$', views.generate_report_cnmb, name='cnmb'),
    url(r'umls$', views.generate_report_umls, name='umls'),
]
