# encoding: utf-8
from django.contrib.sitemaps import Sitemap
from gallery.models import Entry

class GallerySitemap(Sitemap):
	changefreq = "never"
	priority = 0.5

	def items(self):
		return Entry.objects.filter(is_draft=False)

	def lastmod(self, obj):
		return obj.pub_date