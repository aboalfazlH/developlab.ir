from django.contrib import messages as message
from django.views.generic import *
from .forms import AccountCreationForm,LoginForm
from .models import Account
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth import login,authenticate


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


class LoginView(FormView):
    form_class = LoginForm
    template_name = "auth/login.html"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        account = Account.objects.filter(username=username).first()

        if not account:
            form.add_error(None, "نام کاربری یا رمز عبور اشتباه است.")
            return self.form_invalid(form)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            message.success(self.request, f"چه خوب شد برگشتی {user}")
            return super().form_valid(form)
        form.add_error(None, "نام کاربری یا رمز عبور اشتباه است.")
        return self.form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            message.warning(request, "شما اکنون احراز هویت کردید")
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
