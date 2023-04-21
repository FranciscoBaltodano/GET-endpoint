from django.conf.urls import re_path
from tutorials import views 

urlpatterns = [ 
    re_path(r'^api/tutorials$', views.tutorial_detail),
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorials_api),
]