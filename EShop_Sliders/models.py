import os

from django.db import models

from common.utils import get_file_ext, delete_old_image


# Create your models here.



def upload_image_path(instance, filename):
    name, ext = get_file_ext(filename)
    filename_name=f"{instance.id}_{instance.title}{ext}"
    return f"sliders/{filename_name}"

class Slider(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان')
    link=models.URLField(max_length=100,verbose_name='آدرس')
    description=models.TextField(verbose_name='توضیحات')
    image=models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name='تصویر')

    class Meta:
       verbose_name = 'اسلایدر'
       verbose_name_plural = "اسلاید ها"
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
            delete_old_image(self)
            super().save(*args, **kwargs)