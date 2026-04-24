from django.shortcuts import render
from django.views.generic import *
from .models import Post
from .forms import PostCreateForm
from django.urls import reverse_lazy
from django.contrib import messages as message


class PostListView(ListView):
    model = Post
    template_name = "blog/post-list.html"
    context_object_name = "posts"

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "blog/post-create.html"
    success_url = reverse_lazy("blog:post-list")
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        message.success(request=self.request,message="پست شما ثبت شد")
        return super().form_valid(form)