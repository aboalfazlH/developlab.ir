from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy


class MainPageView(TemplateView):
    template_name = "index.html"

class HomeRedirectView(RedirectView):
    url = reverse_lazy("home")