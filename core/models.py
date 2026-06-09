from django.db import models


class BaseComment(models.Model):
    user = models.ForeignKey("accounts.Account",on_delete=models.CASCADE,verbose_name="نویسنده نظر")
    reply_to = models.ForeignKey("self",blank=True,null=True,on_delete=models.CASCADE,verbose_name="پاسخ به")
    content = models.TextField(verbose_name="محتوا",max_length=2000)
    write_date = models.DateTimeField(verbose_name="تاریخ نوشته شدن",auto_now_add=True)
    old_content = models.TextField(verbose_name="محتوا قبل ویرایش",blank=True,null=True)
    edited = models.BooleanField(verbose_name="تغییر یافته",default=False)
    is_active = models.BooleanField(verbose_name="فعال",default=True)
    is_verify = models.BooleanField(verbose_name="تایید",default=False)

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        abstract = True
        ordering = ["-write_date"]
