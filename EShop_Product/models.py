import os
from tabnanny import verbose

from django.db import models

# Create your models here.
class ProductsManager(models.Manager):
     def  get_active_products(self):
          return  self.get_queryset().filter(active=True)


def get_file_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_file_ext(filename)
    final_name=f"{instance.id}_{instance.title}{ext}"
    return f"products/{final_name}"

class Product(models.Model):
    title=models.CharField(max_length=150,verbose_name="عنوان")
    description=models.TextField()
    price=models.IntegerField(verbose_name="قیمت")
    image=models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name="تصویر")
    active=models.BooleanField(default=True,verbose_name="وضعیت فعال بودن")

    objects=ProductsManager()

    class Meta:
        verbose_name='محصول'
        verbose_name_plural="محصولات"

    def __str__(self):
        return self.title