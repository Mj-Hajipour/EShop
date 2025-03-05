from django.db import models
from django.contrib.auth.models import  User

from EShop_Order.models import Order, OrderDetails
from common.utils import get_file_ext, delete_old_image


def upload_profile_pic_path(instance, filename):
    name, ext = get_file_ext(filename)
    final_name=f"{instance.user.id}_{instance.user.username}{ext}"
    return f"profile_pictures/{final_name}"



# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_profile_pic_path, blank=True, null=True,verbose_name="عکس پروفایل")
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name="عکس پروفایل"
        verbose_name_plural="عکس پروفایل کاربران"
    def save(self,*args, **kwargs):
       delete_old_image(self)
       super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address= models.TextField(verbose_name='آدرس اول')
    postal_code = models.CharField(max_length=10,verbose_name='کدپستی', blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name='شهر',blank=True, null=True)
    province = models.CharField(max_length=50, verbose_name='استان',blank=True, null=True)
    mobile = models.CharField(max_length=15, verbose_name='شماره موبایل',blank=True, null=True)
    Emergency_call = models.CharField(max_length=15, verbose_name='شماره تماس اضطراری',blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name="اطلاعات پروفایل"
        verbose_name_plural="اطلاعات پروفایل کاربران"

class  OrderItem(models.Manager):
    def get_by_id(self,userId):
        qs=self.get_queryset().filter(user_id=userId)
        return qs

class Invoice(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
      order=models.ForeignKey(Order,on_delete=models.CASCADE)
      Shipping_FullName=models.CharField(max_length=150,verbose_name="نام و نام خانوادگی گیرنده:",null=True,blank=True)
      Shipping_Address=models.TextField(verbose_name="آدرس گیرنده:",null=True,blank=True)
      Shipping_Mobile=models.CharField(max_length=15,verbose_name="موبایل گیرنده :",blank=True, null=True)
      Shipping_PostalCode=models.CharField(max_length=10,verbose_name="کد پستی گیرنده :",null=True,blank=True)
      Is_send=models.BooleanField(verbose_name="ارسال شده/نشده",default=False)
      objects=models.Manager()
      order_item=OrderItem()

      def __int__(self):
          return self.id

      class Meta:
          verbose_name="فاکتور"
          verbose_name_plural="فاکتور های موجود"