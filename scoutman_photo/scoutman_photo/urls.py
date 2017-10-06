# encoding: utf-8
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	url(r'^', include('home.urls', namespace='home')),
	url(r'^ueber-mich/$', TemplateView.as_view(template_name='about/about.html'), name='ueber-mich'),
	url(r'^galerie/', include('gallery.urls', namespace='gallery')),
	url(r'^intern/', include(admin.site.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)