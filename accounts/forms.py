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
        widgets = {
                "username": forms.TextInput(attrs={"placeholder": "نام کاربری"}),
                "email": forms.EmailInput(attrs={"placeholder": "ایمیل"}),
                "first_name": forms.TextInput(attrs={"placeholder": "نام"}),
                "last_name": forms.TextInput(attrs={"placeholder": "نام خانوادگی"}),
                "password1": forms.PasswordInput(),
                "password2": forms.PasswordInput(),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            field.label = ""
        self.fields["password1"].widget.attrs.update({"placeholder": "رمز عبور"})
        self.fields["password2"].widget.attrs.update({"placeholder": "تائید رمز عبور"})

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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("first_name","last_name","bio","avatar")