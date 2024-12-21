from django.db import models
from django.db.models.signals import post_save,pre_save

from EShop_Product.models import Product
from .Utils import unique_slug_generator


# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    slug =models.SlugField(verbose_name="عنوان جستجو")
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ثبت")
    active = models.BooleanField(default=True,verbose_name="غیر فعال")
    products=models.ManyToManyField(Product,blank=True,verbose_name="محصولات")
    class Meta:
       verbose_name='تگ/برچسب'
       verbose_name_plural='تگ ها/بر چسب ها'

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Tag)
