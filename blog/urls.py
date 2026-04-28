from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("",views.BlogTemplateView.as_view(),name="blog"),
    path("post/",views.PostListView.as_view(),name="post-list"),
    path("post/write/",views.PostCreateView.as_view(),name="post-create"),
    path("post/<int:pk>/",views.PostDetailView.as_view(),name="post-detail"),
    path("post/<int:pk>/edit/",views.PostUpdateView.as_view(),name="post-update"),
    path("api/post-list/",views.PostsJsonListView.as_view(),name="api-post-list"),
]