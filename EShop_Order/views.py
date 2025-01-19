from itertools import product
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from EShop_Order.form import UserNewOrderForm
from EShop_Order.models import  Order
from EShop_Product.models import Product





#Views====>

@login_required(login_url='/login')
def add_user_order(request):
    new_order_form=UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order=Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
        if order is None:
            order=Order.objects.create(owner_id=request.user.id,is_paid=False)
        product_id=new_order_form.cleaned_data['product_id']
        count=new_order_form.cleaned_data['count']
        if count<0 :
            count=1
        product = Product.objects.get_by_id(product_id=product_id)
        order.orderdetails_set.create(product_id=product_id,price=product.price,count=count)

         #best
        return redirect(f'/products/{product.id}')

    return redirect('/')


@login_required(login_url='/login')
def user_open_order(request):
    context={
        'order':None,
         'details':None,
    }
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context['order']= open_order
        context['details']=open_order.orderdetails_set.all()
    return render(request,'order/user_open_order.html',context)

############################################Zarin Pal############################
import logging
from django.urls import reverse
from azbankgateways import (
    bankfactories,
    models as bank_models,
    default_settings as settings,
)
from azbankgateways.exceptions import AZBankGatewaysException


def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 50000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = "+989112221234"  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = (
            factory.create()
        )  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url("/callback-gateway")
        bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # redirect to failed page.
        raise e




