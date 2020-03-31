from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class BlogListViews(ListView):
    model = Post
    template_name = 'home.html'
