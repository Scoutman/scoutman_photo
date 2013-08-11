# encoding: utf-8
from django.contrib import admin
from .models import Category, Picture


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'active')
	
admin.site.register(Category, CategoryAdmin)

class PictureAdmin(admin.ModelAdmin):
	list_display = ('image', 'title', 'category', 'pub_date', 'thumb_path')
	list_filter = ['category']
	
admin.site.register(Picture, PictureAdmin)