from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("post/",views.PostListView.as_view(),name="post-list"),
]