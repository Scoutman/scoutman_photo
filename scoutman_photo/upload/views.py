from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django import forms
from .models import Document


"""
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})
"""


def upload_file(request):
	if request.method == 'POST':
		print('POST')
		form = UploadFileForm(request.POST, request.FILES)
		print('valid')
		if form.is_valid():
			# file is saved
			print('save')
			newdoc = Document(docfile = request.FILES['file'])
			newdoc.save()			
			#form.save()
			print('return')
			return HttpResponseRedirect(reverse('upload:upload_file'))
	else:
		form = UploadFileForm()
		return render(request, 'upload/upload.html', {'form': form})	


class UploadFileForm(forms.Form):
	#title = forms.CharField(max_length=50)
	file  = forms.FileField()