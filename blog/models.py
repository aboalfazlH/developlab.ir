from django.db import models


class Post(models.Model):
    # متنی
    title = models.CharField(verbose_name="موضوع",max_length=200)
    summary = models.TextField(verbose_name="خلاصه متن")
    description = models.TextField(verbose_name="متن اصلی")
    # آپلود
    thumbnail = models.ImageField(verbose_name="تصویر شاخص")
    # بولین ها
    is_active = models.BooleanField(verbose_name="فعال",default=True)
    is_verify = models.BooleanField(verbose_name="مورد تایید",default=False)
    is_pin = models.BooleanField(verbose_name="سنجاق شده",default=False)
    # روابط
    author = models.ForeignKey("accounts.Account",on_delete=models.CASCADE)
    # زمان ها
    write_date = models.DateTimeField(verbose_name="تاریخ نوشتن",auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="تاریخ آخرین تغییر",auto_now=True)
    
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
        ordering = ["-write_date"]
    
    def __str__(self):
        return self.title