from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
	name = models.CharField(max_length = 150)
	capital = models.CharField(max_length = 150)
	currancy = models.CharField(max_length = 10, blank =True, null = True)

	def __unicode__(self):
		return self.name