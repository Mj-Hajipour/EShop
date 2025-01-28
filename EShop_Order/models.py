from django.db import models
from django.contrib.auth.models import User
from EShop_Product.models import Product


# Create your models here.
class Order(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid=models.BooleanField(verbose_name='پرداخت شده/نشده',default=False)
    payment_date=models.DateTimeField(blank=True,null=True,verbose_name='تاریخ پرداخت')
    cartNumber=models.CharField(max_length=16,blank=True,null=True,verbose_name='شماره کارت')
    Trc=models.CharField(max_length=50,verbose_name='کد پیگری',blank=True,null=True,unique=True)
    status=models.CharField(max_length=100,blank=True,null=True,verbose_name='وضعیت پرداخت')
    GateWay_name=models.CharField(max_length=100,blank=True,null=True,verbose_name='نام درگاه پرداخت')


    class Meta:
        verbose_name='سبد خرید'
        verbose_name_plural='سبد های خرید کاربران'

    def __str__(self):
        return  self.owner.get_full_name()
    def get_total_price(self):
        amount=0
        for detail in self.orderdetails_set.all():
            amount += detail.price*detail.count
        return amount


class OrderDetails(models.Model):
      order=models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='سبد خرید')
      product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
      price=models.IntegerField(verbose_name='قیمت محصول')
      count=models.IntegerField(verbose_name='تعداد')

      def get_detail_sum(self):
          return self.count *self.price



      class Meta:
          verbose_name='جزییات محصول'
          verbose_name_plural='اطلاعات جزییات محصولات'

      def __str__(self):
          return self.product.title


