from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission


class Account(AbstractUser):

    def avatar_upload_path(instance,filename):
        username = instance.username or "new"
        return f"avatars/{username}/{filename}"

    email = models.EmailField(unique=True,)
    bio = models.TextField(blank=True,null=True)
    avatar = models.ImageField(default="avatars/devlab.jpg",upload_to=avatar_upload_path)
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
    def __str__(self):
        if self.get_full_name() == "":
            return self.username
        return self.get_full_name()
    
    class Meta:
        db_table = "accounts"
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"

    REQUIRED_FIELDS = ["email","first_name","last_name"]