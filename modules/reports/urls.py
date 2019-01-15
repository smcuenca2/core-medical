from django.conf.urls import *
from modules.reports import views
urlpatterns = [
    url(r'cnmb$', views.report_search_cnmb, name='cnmb'),
    url(r'umls$', views.report_search_umls, name='umls'),
]
