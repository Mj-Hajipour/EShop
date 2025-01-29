import os
from django.db.models import Q
from django.db import models

from EShop_products_category.models import ProductCategory


# Create your models here.
class ProductsManager(models.Manager):
     def  get_active_products(self):
          return  self.get_queryset().filter(active=True)

     def get_products_by_category(self, category_name):
         return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

     def get_by_id(self,product_id):
           qs=self.get_queryset().filter(id=product_id)
           if qs.count()==1:
               return qs.first()
           else:
               return None
     def search(self,query):
         #برای پیاده سازی سرچ که داخل توضیحات نیز بگردیم
         lookup=(
                 Q(title__icontains=query) |
                 Q(description__icontains=query)|
                 Q(tag__title__contains=query)
         )
         #برای پباده سازی منطق or باید از lookupاستفاده کنیم
         return self.get_queryset().filter(lookup,active=True).distinct()



def get_file_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_file_ext(filename)
    final_name=f"{instance.id}_{instance.title}{ext}"
    return f"products/{final_name}"

def upload_gallery_image_path(instance, filename):
    name, ext = get_file_ext(filename)
    final_name=f"{instance.id}_{instance.title}{ext}"
    return f"products/galleries/{final_name}"

class Product(models.Model):
    title=models.CharField(max_length=150,verbose_name="عنوان")
    description=models.TextField()
    price=models.IntegerField(verbose_name="قیمت")
    image=models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name="تصویر")
    active=models.BooleanField(default=True,verbose_name="فعال/غیر فعال")
    categories=models.ManyToManyField(ProductCategory,blank=True,verbose_name='دسته بندی ها')
    visit_count=models.IntegerField(default=0,verbose_name='تعداد بازدید')

    objects=ProductsManager()

    class Meta:
        verbose_name='محصول'
        verbose_name_plural="محصولات"

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return  f"/products/{self.id}"

class ProductGallery(models.Model):
     title=models.CharField(max_length=150,verbose_name='عنوان')
     image=models.ImageField(upload_to=upload_gallery_image_path,blank=True,verbose_name='تصویر')
     product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='برای محصول')

     class Meta:
         verbose_name='تصویر'
         verbose_name_plural='تصاویر'
     def __str__(self):
         return self.title
