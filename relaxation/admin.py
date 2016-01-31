from django.contrib import admin

from relaxation.models import Restaurant, Theatre, Bar

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Restaurant, RestaurantAdmin)


class TheatreAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Theatre, TheatreAdmin)


class BarAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Bar, BarAdmin)