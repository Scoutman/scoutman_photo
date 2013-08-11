# encoding: utf-8
import os
from django.shortcuts import render, get_object_or_404
from django.conf import settings

def index(request):

	slider_dir = "%s/slider" % (settings.MEDIA_ROOT)

	os.chdir(slider_dir)
	i = 0
	img_list = {}
	
	for file in os.listdir("."):
		if file.split('.')[-1].lower() in ["png", "jpg", "jpeg"] :
			img_list[i] = "slider/%s" % file
			i += 1
	
	return render(request, 'home/home.html', {'img_list' : img_list})