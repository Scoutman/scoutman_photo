# encoding: utf-8
from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	slug = models.SlugField()
	active = models.BooleanField()

	def __unicode__(self):
		return self.name
"""	
class Picture(models.Model):
	category = models.ForeignKey(Category)
	image = models.ImageField('gallery')
	
	def __unicode__(self):
		return self.image
"""	