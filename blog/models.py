from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from cities.models import Country, City

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 250)
	short_desription = models.CharField(max_length = 255)
	description = models.TextField()
	main_pic = models.FileField(upload_to = 'blog')
	author = models.ForeignKey(User)
	#country = models.ForeignKey(Country)
	date_published = models.DateField(auto_now_add = True)
	city = models.ForeignKey(City)

	def __unicode__(self):
		return self.title

	#def city(self):
	#	city = Country.objects.filter(id = country)
	#	return self.city
		
	class Meta():
		ordering = ['title']

	