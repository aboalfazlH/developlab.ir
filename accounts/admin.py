from django.contrib import admin
from .models import Account
from .forms import AccountChangeForm, AccountCreationForm
from django.contrib.auth.admin import UserAdmin


@admin.register(Account)
class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('تاریخ ها', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        }),
    )

    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('username',)
