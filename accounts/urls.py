from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("auth/register",views.RegisterView.as_view(),name="register"),
    path("auth/login/",views.LoginView.as_view(),name="login"),
    path("auth/logout/",views.LogoutView.as_view(),name="logout"),
    path("me/",views.MyDetailView.as_view(),name="me"),
    path("<str:username>/",views.UserDetailView.as_view(),name="profile"),
    path("<str:username>/edit/",views.UserUpdateView.as_view(),name="profile-edit"),
    path("api/users/<int:pk>/",views.UserRetrieveAPIView.as_view(),name="detail-api"),
    path("api/users/is_exist/",views.UsernameOrEmailExistedView.as_view(),name="exist-api")
]