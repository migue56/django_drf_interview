from django.urls import path
from django.conf.urls import  url
from rest_framework import routers
#from rest_framework.documentation import include_docs_urls
from api import api_views

urlpatterns = [
    path('salaries', api_views.SalariesAPIView.as_view(), name='salaries'),
    url(r'^salaries/(?P<pk>[0-9]+)/$', api_views.SalariesAPIView.as_view(), name='salaries'),
  #  url(r'^docs/', include_docs_urls(title='REST API'))
]