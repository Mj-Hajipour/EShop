from django.db import models
from django.contrib.auth.models import User
from EShop_Product.models import Product


# Create your models here.
class Order(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid=models.BooleanField(verbose_name='پرداخت شده/نشده',default=False)
    payment_date=models.DateTimeField(blank=True,null=True,verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name='سبد خرید'
        verbose_name_plural='سبد های خرید کاربران'

    def __str__(self):
        return  self.owner.get_full_name()

class OrderDetails(models.Model):
      order=models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='سبد خرید')
      product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
      price=models.IntegerField(verbose_name='قیمت محصول')
      count=models.IntegerField(verbose_name='تعداد')

      class Meta:
          verbose_name='جزییات محصول'
          verbose_name_plural='اطلاعات جزییات محصولات'

      def __str__(self):
          return self.product.title


