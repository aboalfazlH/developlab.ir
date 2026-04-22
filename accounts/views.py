from django.contrib import messages as message
from django.views.generic import *
from .forms import AccountCreationForm,Account
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth import login


class RegisterView(CreateView):
    model = Account
    form_class = AccountCreationForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("accounts:login")
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            message.warning(request, "شما اکنون احراز هویت کردید")
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """login user if form is valid"""
        response = super().form_valid(form)

        login(
            self.request,
            self.object,
        )
        message.success(self.request,"ثبت نام با موفقیت انجام شد")

        return response


#TODO:Custom Login