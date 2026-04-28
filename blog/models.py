from django.db import models


class Post(models.Model):
    # Text
    title = models.CharField(verbose_name="موضوع",max_length=200)
    summary = models.TextField(verbose_name="خلاصه متن",blank=True,null=True)
    description = models.TextField(verbose_name="متن اصلی",blank=True,null=True)
    # Files
    thumbnail = models.ImageField(verbose_name="تصویر شاخص",blank=True,null=True)
    # Booleans
    is_active = models.BooleanField(verbose_name="فعال",default=True)
    is_verify = models.BooleanField(verbose_name="مورد تایید",default=False)
    is_pin = models.BooleanField(verbose_name="سنجاق شده",default=False)
    # Relationships
    author = models.ForeignKey("accounts.Account",on_delete=models.CASCADE)
    # DateTimes
    write_date = models.DateTimeField(verbose_name="تاریخ نوشتن",auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="تاریخ آخرین تغییر",auto_now=True)
    
    class Meta:
        db_table = "posts"
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
        ordering = ["-write_date"]
    
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("blog:post-detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.title