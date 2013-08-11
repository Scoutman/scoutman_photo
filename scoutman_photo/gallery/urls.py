# encoding: utf-8
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns('',
	url(r'^(?P<slug>[-_\w]+)/$', views.DetailView.as_view(), name='category'),
)