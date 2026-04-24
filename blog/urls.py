from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("post/",views.PostListView.as_view(),name="post-list"),
    path("post/write/",views.PostCreateView.as_view(),name="post-create"),
    path("post/<int:pk>/edit",views.PostUpdateView.as_view(),name="post-update"),
]