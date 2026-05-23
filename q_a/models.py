from django.db import models
from django.core.validators import FileExtensionValidator
from . import allowed_extensions
from accounts.models import Account


VALIDATOR = FileExtensionValidator(allowed_extensions=allowed_extensions)

def string_smaller(title,length=50):
    if len(title) >= length:
        return title[:length] + "..."
    return title

class Question(models.Model):
    title = models.CharField(verbose_name="عنوان",max_length=110)
    code_file = models.FileField(verbose_name="فایل کد",help_text="اگر کد شما خیلی طولانی است،کد را بارگذاری کنید",blank=True,null=True,validators=[VALIDATOR])
    description = models.TextField(verbose_name="توضیحات",help_text="مشکلات،توضیحات و کد را به اشتراک بگذارید")
    user = models.ForeignKey(Account,verbose_name="پرسشگر",on_delete=models.CASCADE, related_name="questions")
    ask_date = models.DateTimeField(verbose_name="تاریخ پرسش",auto_now_add=True)
    is_active = models.BooleanField(verbose_name="فعال بودن پرسش",default=True)
    is_pin = models.BooleanField(verbose_name="سنجاق کردن سوال")
    is_verify = models.BooleanField(verbose_name="مورد تایید بودن سوال")
    is_solve = models.BooleanField(verbose_name="حل شدن سوال",default=False)

    def __str__(self):
        return string_smaller(self.title)


class Answer(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="answers")
    description = models.TextField(verbose_name="توضیحات")
    is_active = models.BooleanField("فعال", default=True)
    is_best = models.BooleanField("بهترین", default=False)
    write_date = models.DateTimeField("تاریخ مطرح شدن", auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    
    def __str__(self):
        return string_smaller(self.description)