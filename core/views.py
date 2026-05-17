from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib import messages


class MainPageView(TemplateView):
    template_name = "index.html"

class HomeRedirectView(RedirectView):
    url = reverse_lazy("core:home")