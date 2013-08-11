# encoding: utf-8
from django.conf import settings

def config(request):
	config = settings.SITE_CONFIG
	return {'config': config}