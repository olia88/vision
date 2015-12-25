from django.contrib import admin
from django.contrib.auth.models import User

from cuisine.models import Cuisine

# Register your models here.
class CuisineAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(Cuisine, CuisineAdmin)