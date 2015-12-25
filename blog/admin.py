from django.contrib import admin
from django.contrib.auth.models import User

from blog.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(Blog, BlogAdmin)