from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from .forms import AccountChangeForm,AccountCreationForm

@admin.register(Account)
class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm