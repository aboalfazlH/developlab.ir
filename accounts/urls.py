from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = "accounts"

urlpatterns = [
    path("auth/register",views.RegisterView.as_view(),name="register"),
    path("auth/login",LoginView.as_view(template_name="auth/login.html"),name="login"),
]