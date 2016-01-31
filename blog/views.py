from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Blog
# Create your views here.


class BlogList(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    ordering = '-date_published'
    paginate_by = 10