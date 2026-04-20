from django.urls import path
from . import views


urlpatterns = [
    path('',views.MainPageView.as_view(template_name='index.html'),name='home'),
    path('home/',views.HomeRedirectView.as_view()),
]