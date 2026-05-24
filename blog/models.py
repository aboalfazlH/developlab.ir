from django.db import models
from core.models import BaseComment
from core import string_smaller


class Post(models.Model):
    def thumbnail_upload_path(instance,filename):
        pk = instance.pk or "new"
        return f"thumbnails/{pk}/{filename}"
    
    # Text
    title = models.CharField(verbose_name="موضوع",max_length=200)
    summary = models.TextField(verbose_name="خلاصه متن",blank=True,null=True)
    description = models.TextField(verbose_name="متن اصلی",blank=True,null=True)
    # Files
    thumbnail = models.ImageField(verbose_name="تصویر شاخص",blank=True,null=True,upload_to=thumbnail_upload_path)
    # Booleans
    is_active = models.BooleanField(verbose_name="فعال",default=True)
    is_verify = models.BooleanField(verbose_name="مورد تایید",default=False)
    is_pin = models.BooleanField(verbose_name="سنجاق شده",default=False)
    # Relationships
    author = models.ForeignKey("accounts.Account",on_delete=models.CASCADE)
    # DateTimes
    write_date = models.DateTimeField(verbose_name="تاریخ نوشتن",auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="تاریخ آخرین تغییر",auto_now=True)

    views = models.IntegerField(verbose_name="بازدید ها",default=0)
    
    class Meta:
        db_table = "posts"
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
        ordering = ["-write_date"]
    
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("blog:post-detail", kwargs={"pk": self.id})

    
    @classmethod
    def get_total_views(cls, author):
        total_views = cls.objects.filter(author=author).aggregate(models.Sum('views'))['views__sum']
        return total_views or 0

    def __str__(self):
        return self.title

class PostComment(BaseComment):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return string_smaller(self.content)