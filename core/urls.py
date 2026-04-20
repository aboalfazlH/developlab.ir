from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.MainPageView.as_view(template_name='index.html'),name='home'),
    path('',views.HomeRedirectView.as_view()),
]