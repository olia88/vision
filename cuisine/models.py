from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
	title = models.CharField(max_length = 250)
	category = models.CharField(max_length = 150, choices = food)
	ingredients = models.TextField()
	main_pic = models.FileField()

	def __unicode__(self):
		return self.name