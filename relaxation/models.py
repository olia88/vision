from __future__ import unicode_literals

from django.db import models

from cities.models import Country, City
#from country.models import Country, City

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length = 250)
	address = models.CharField(max_length = 250)
	pic = models.FileField(upload_to = 'restaurant')
	description = models.TextField()
	web_site = models.URLField()
	city = models.ForeignKey(City)

	def __unicode__(self):
		return self.name

	#def city(self):
	#	return self.city.name

class Theatre(models.Model):
	name = models.CharField(max_length = 250)
	address = models.CharField(max_length = 250)
	pic = models.FileField(upload_to = 'restaurant')
	description = models.TextField()
	web_site = models.URLField()
	city = models.ForeignKey(City)

	def __unicode__(self):
		return self.name

class Bar(models.Model):
	name = models.CharField(max_length = 250)
	address = models.CharField(max_length = 250)
	pic = models.FileField(upload_to = 'restaurant')
	description = models.TextField()
	web_site = models.URLField()
	city = models.ForeignKey(City)

	def __unicode__(self):
		return self.name