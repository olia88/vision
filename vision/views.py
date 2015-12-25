from django.shortcuts import render
from blog.models import Blog

def main(request):
	#blogs = Blog.objects.all()
	return render(request, 'main.html')