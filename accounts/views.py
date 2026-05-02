from django.contrib import messages as message
from django.views.generic import *
from .forms import AccountCreationForm,LoginForm,ProfileForm
from .models import Account
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from rest_framework.generics import RetrieveAPIView
from .serializer import AccountSerializer

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

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"auth/logout.html")
    
    def post(self,request,*args,**kwargs):
        logout(request)
        message.success(request,"خروج موفقیت آمیز بود")
        return redirect("core:home")
    

class UserDetailView(DetailView):
    model = Account
    template_name = "auth/profile.html"
    context_object_name = "profile"
    slug_field = "username"
    slug_url_kwarg = "username"

class UserUpdateView(UpdateView):
    model = Account
    form_class = ProfileForm
    template_name = "auth/profile-edit.html"
    context_object_name = "profile"
    slug_field = "username"
    slug_url_kwarg = "username"

    def dispatch(self, request, *args, **kwargs):
        username = self.kwargs.get(self.slug_url_kwarg)
        if username == request.user.username:
            return super().dispatch(request, *args, **kwargs)
        message.error(request,"شما به این حساب کاربری دسترسی ندارید")
        return redirect("accounts:profile",username)
    
    def get_success_url(self):
        username = self.kwargs.get(self.slug_url_kwarg)
        return reverse("accounts:profile", kwargs={'username': username})

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = Account.objects.filter(is_active=True).order_by("id")
    serializer_class = AccountSerializer