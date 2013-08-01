from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
	url(r'^blog/$', TemplateView.as_view(template_name='blog/blog.html'), name='blog'),
	url(r'^upload/', include('upload.urls', namespace='upload')),
	url(r'^gallery/', include('gallery.urls', namespace='gallery')),
	url(r'^admin/', include(admin.site.urls)),
)
