#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from cities.models import Country
#from country.models import Country, City

# Create your models here.

class Cuisine(models.Model):

	meal_type = (
		('first meal', 'Первое блюдо'),
		('second meal', 'Второе блюдо'),
		('meat', 'Блюдо из мяса'),
		('fish', 'Блюдо из рыбы'),
		('baked dishes', 'Запеченные блюда'),
		('baking', 'Выпечка'),
		('Dessert', 'Десерты'),
		('Other', 'Другое'),
	)

	title = models.CharField(max_length = 250)
	category = models.CharField(max_length = 155, choices = meal_type)
	ingredients = models.TextField()
	steps = models.TextField()
	main_pic = models.FileField(upload_to = 'cuisine')
	author = models.ForeignKey(User)
	country = models.ForeignKey(Country)
	date_published = models.DateField(auto_now_add = True)

	def __unicode__(self):
		return self.title