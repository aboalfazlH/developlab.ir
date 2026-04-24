from django.shortcuts import render
from django.views.generic import *
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post-list.html"
    context_object_name = "posts"