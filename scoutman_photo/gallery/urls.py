# encoding: utf-8
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^(?P<slug>[-_\w]+)/$', views.DetailView.as_view(), name='category'),
]