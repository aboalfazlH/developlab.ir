from django.urls import path
from . import views


app_name = "core"

urlpatterns = [
    path('home/',views.MainPageView.as_view(template_name='index.html'),name='home'),
    path('',views.HomeRedirectView.as_view()),
]