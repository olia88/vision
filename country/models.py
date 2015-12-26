from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
	name = models.CharField(max_length = 150)
	capital = models.CharField(max_length = 150)
	description = models.TextField()
	currancy = models.CharField(max_length = 10, blank =True, null = True)
	pic = models.FileField(upload_to = 'country')

	def __unicode__(self):
		return self.name

	class Meta():
		verbose_name_plural = 'Countries'

class City(models.Model):
	name = models.CharField(max_length = 150)
	description = models.TextField()
	country = models.ManyToManyField(Country)

	def __unicode__(self):
		return self.name

	class Meta():
		verbose_name_plural = 'Cities'