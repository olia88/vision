from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from country.models import Country, City

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 250)
	short_desription = models.CharField(max_length = 255)
	description = models.TextField()
	main_pic = models.FileField(upload_to = 'blog')
	author = models.ForeignKey(User)
	city = models.ForeignKey(City)
	date_published = models.DateField(auto_now_add = True)

	def __unicode__(self):
		return self.title
		
	class Meta():
		ordering = ['-date_published']

	