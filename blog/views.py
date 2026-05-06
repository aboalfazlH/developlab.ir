from django.shortcuts import render,redirect
from django.views.generic import *
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib import messages as message
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import PostSerializer
from django.http import HttpRequest


class PostListView(ListView):
    model = Post
    template_name = "blog/post-list.html"
    context_object_name = "posts"

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post-create.html"
    success_url = reverse_lazy("blog:post-list")
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        message.success(self.request,"پست شما ثبت شد")
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post-update.html"
    success_url = reverse_lazy("blog:post-list")
    context_object_name = "post"
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        
        post = self.get_object()
        if post.author != request.user and not request.user.is_superuser:
            message.error(request,"شما نمیتوانید این پست را تغییر دهید")
            return redirect(self.success_url)
        
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        message.success(self.request,"پست تغییر کرد")
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"

class PostDeleteView(View):
    def get(self,request:HttpRequest,id,*args,**kwargs):
        return render(request,"blog/post-delete.html")

    def post(self,request:HttpRequest,id,*args,**kwargs):
        post = Post.objects.get(id=id)
        if request.user.is_superuser or post.author == request.user:
            post.delete()
    def get_context_data(self,id,*args,**kwargs):
        context = {}
        context["post"] = Post.objects.get(id=id)

    
class BlogTemplateView(TemplateView):
    template_name = "blog/main.html"
    
class DashboardView(TemplateView):
    template_name = "blog/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(author=self.request.user)
        return

class PostsJsonListView(ListAPIView):
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostSerializer