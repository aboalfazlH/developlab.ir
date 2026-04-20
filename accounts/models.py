from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission


class Account(AbstractUser):
    email = models.EmailField(unique=True,)
    groups = models.ManyToManyField(
        Group,
        related_name="account_set",
        blank=True,
        help_text='گروه بندی کاربران را انجام دهید',
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="account_set_permissions",
        blank=True,
        help_text='اجازه کاربران را بدهید',
        related_query_name="user",
    )