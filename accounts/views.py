from django.shortcuts import render
from django.views.generic import *
from .forms import AccountCreationForm,Account
from django.urls import reverse_lazy


class RegisterView(CreateView):
    model = Account
    form_class = AccountCreationForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("accounts:login")