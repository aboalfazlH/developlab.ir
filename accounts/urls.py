from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("auth/register",views.RegisterView.as_view(),name="register"),
    path("auth/login",views.LoginView.as_view(template_name="auth/login.html"),name="login"),
]