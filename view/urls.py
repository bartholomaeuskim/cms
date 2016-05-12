# coding : utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<menu_id>.+)/$', views.index),
    url(r'^', views.index),
]
