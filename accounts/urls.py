from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("auth/register",views.RegisterView.as_view(),name="register"),
]