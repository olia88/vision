from django.contrib import admin
from country.models import Country, City

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
	list_display = ['name']

class CityAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Country, CountryAdmin)

admin.site.register(City, CityAdmin)