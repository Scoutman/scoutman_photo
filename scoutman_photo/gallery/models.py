# encoding: utf-8
from os import remove, makedirs, rename, rmdir, listdir
from os.path import basename, exists
from PIL import Image, ImageOps
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.core.files.move import file_move_safe

class Category(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	slug = models.SlugField()
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		dir_category_root = '%s/gallery/%s' % (settings.MEDIA_ROOT, slugify(self.slug))
		if not exists(dir_category_root):
			makedirs(dir_category_root)		

		super(Category, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		dir_category_root = '%s/gallery/%s' % (settings.MEDIA_ROOT, slugify(self.slug))
		files = listdir(dir_category_root)
		
		if len(files) == 0:
			rmdir(dir_category_root)		

		super(Category, self).delete(*args, **kwargs)

		
class Picture(models.Model):

	def upload_path(self, filename):
		filename = basename(filename)
		filename = filename.split('.')
		extension = filename.pop()
		name = ''.join(filename)
		return 'gallery/%s/%s.%s' % (self.category.slug, slugify(name), extension)
	
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to=upload_path)
	thumb = models.ImageField(upload_to=upload_path, blank=True, editable=False)
	title = models.CharField(max_length=255, blank=True)
	pub_date = models.DateTimeField(auto_now = False, auto_now_add = True)
	
	class Meta:
		ordering = ['-pub_date']
		
	def __unicode__(self):
		return unicode(self.image)
	
	def create_thumbnail(self):			
		image = basename(self.image.name)
		image = image.split('.')
		extension = image.pop()
		name = ''.join(image)
		
		filename_thumb_root = '%s/gallery/%s/%s.thumb.%s' % (settings.MEDIA_ROOT, self.category.slug, slugify(name), extension)
		filename_thumb = 'gallery/%s/%s.thumb.%s' % (self.category.slug, slugify(name), extension)
		
		self.thumb = filename_thumb
		
		size = int(settings.SITE_CONFIG['thumb_width']), int(settings.SITE_CONFIG['thumb_height'])
		tmp_img = Image.open(self.image)
		thumb = ImageOps.fit(tmp_img, size, Image.ANTIALIAS)
		thumb.save(filename_thumb_root)
		
	
	def save(self, *args, **kwargs):
	
		if self.pk is not None:
			orig = Picture.objects.get(pk=self.pk)
			
			if orig.image != self.image:
				remove(orig.image.path)
				remove(orig.thumb.path)
			
			if orig.category != self.category:
				image = basename(orig.image.path)
				thumb = basename(orig.thumb.path)
				
				image_root = '%s/gallery/%s/%s' % (settings.MEDIA_ROOT, self.category.slug, image)
				thumb_root = '%s/gallery/%s/%s' % (settings.MEDIA_ROOT, self.category.slug, thumb)
				
				file_move_safe(orig.image.path, image_root)
				file_move_safe(orig.thumb.path, thumb_root)
				
				self.image = 'gallery/%s/%s' % (self.category.slug, image)
				self.thumb = 'gallery/%s/%s' % (self.category.slug, thumb)
				
		else:		
			self.create_thumbnail()
			
		super(Picture, self).save(*args, **kwargs)
		
	def delete(self, *args, **kwargs):
		remove(self.image.path)
		remove(self.thumb.path)
		super(Picture, self).delete(*args, **kwargs)
		
	def thumb_path(self):
		thumb = self.thumb.url
		return '<img width="100" height="100" src="%s" />' % (str(thumb))
	
	thumb_path.short_description = 'Thumbnail'
	thumb_path.allow_tags = True
