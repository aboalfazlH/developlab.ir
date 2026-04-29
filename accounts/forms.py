from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UsernameField
from .models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = "__all__"

class LoginForm(forms.Form):
    username = UsernameField(
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "نام کاربری"}),
        label="",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "رمز عبور"}),
        label="",
    )

