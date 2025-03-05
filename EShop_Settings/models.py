from django.db import models
import os
from common.utils import get_file_ext


# Create your models here.
def upload_settings_image_path(instance, filename):
    name, ext = get_file_ext(filename)
    final_name=f"{instance.id}_{instance.Title}{ext}"
    return f"products/settings/{final_name}"

class SiteSettings(models.Model):
    Title=models.CharField(max_length=150,verbose_name="عنوان سایت")
    address=models.CharField(max_length=400,verbose_name='آدرس')
    phone=models.CharField(max_length=50,verbose_name='تلفن')
    mobile=models.CharField(max_length=50,verbose_name='تلفن همراه')
    fax=models.CharField(max_length=50,verbose_name='فکس')
    email=models.EmailField(max_length=50,verbose_name='ایمیل')
    about_us=models.TextField(verbose_name='درباره ما',null=True,blank=True)
    logo=models.ImageField(upload_to=upload_settings_image_path,null=True,blank=True,verbose_name='لوگو سایت')
    copy_right=models.CharField(verbose_name='متن کپی رایت',max_length=200,null=True,blank=True)
    About_logo=models.ImageField(upload_to=upload_settings_image_path,null=True,blank=True,verbose_name='تصویر لوگو درباره ما')


    class Meta:
        verbose_name='تنظیمات سایت'
        verbose_name_plural='مدیریت تنظیمات'
    def __str__(self):
        return self.Title
    def save(self,*args, **kwargs):
        if self.pk:
            old_instance=SiteSettings.objects.get(pk=self.pk)
            if old_instance.logo:
                if os.path.isfile(old_instance.logo.path):
                    os.remove(old_instance.logo.path)
            elif old_instance.About_logo:
                if os.path.isfile(old_instance.About_logo.path):
                    os.remove(old_instance.About_logo.path)

        super().save(*args, **kwargs)