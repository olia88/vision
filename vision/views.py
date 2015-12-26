from django.shortcuts import render
from blog.models import Blog
from cuisine.models import Cuisine

def main(request):
	args = {}
	blogs = Blog.objects.all()[:3]
	args['blog1'] = Blog.objects.order_by('-date_published')[0]
	args['blog2'] = Blog.objects.order_by('-date_published')[1]
	args['blog3'] = Blog.objects.order_by('-date_published')[2]
	args['cuisine1'] = Cuisine.objects.order_by('-date_published')[0]
	args['cuisine2'] = Cuisine.objects.order_by('-date_published')[1]
	return render(request, 'main.html', args)