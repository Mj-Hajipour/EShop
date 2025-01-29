import json
from datetime import datetime
from itertools import product

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from EShop_Order.form import UserNewOrderForm
from EShop_Order.models import Order, OrderDetails
from EShop_Product.models import Product
from azbankgateways.models import banks
from common.utils import format_currency



### payment package###
from django.http import HttpResponse, Http404, JsonResponse
import logging
from django.urls import reverse
from azbankgateways import (
    bankfactories,
    models as bank_models,
    default_settings as settings,
)
from azbankgateways.exceptions import AZBankGatewaysException





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
        'total':0,
    }

    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context['order']= open_order
        order_details=open_order.orderdetails_set.all()
        grouped_details={}
        for detail in order_details:
            Product_id=detail.product_id
            if Product_id not in grouped_details:
                grouped_details[Product_id] = {
                    'product': detail.product,
                    'quantity': detail.count,
                }
            else:
                grouped_details[Product_id]['quantity'] += detail.count

        context['details'] = list(grouped_details.values())
        Total=open_order.get_total_price()
        context['total']=format_currency(Total)
    return render(request,'order/user_open_order.html',context)


@login_required(login_url='/login')
def remove_order_detail(request,*args,**kwargs):
    product_id=kwargs.get('detail_id')
    owner_id=request.user.id
    if product_id is not None:
         order_detail_product=OrderDetails.objects.filter(product_id=product_id , order__owner_id=owner_id)
         if order_detail_product.exists():
          order_detail_product.delete()
          return redirect('/open-order')
    return redirect('/_404_view')




############################################Zarin Pal############################



def go_to_gateway_view(request,*args,**kwargs):
    total_price=0
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
            total_price=open_order.get_total_price()
            # خواندن مبلغ از هر جایی که مد نظر است
            amount = total_price
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
                bank.set_client_callback_url(f"/callback-gateway/{open_order.id}")
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
    raise Http404('Page not found')


def callback_gateway_view(request,*args,**kwargs):
    order_id = kwargs.get('order_id')
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        user_order=Order.objects.get_queryset().get(id=order_id)
        user_order.is_paid=True
        user_order.payment_date=datetime.now()
        user_order.Trc=tracking_code
        value=banks.Bank.objects.get(tracking_code=tracking_code)
        user_order.GateWay_name=value.bank_type
        ext_info=value.extra_information
        responses_dict=json.loads(ext_info)
        user_order.status=responses_dict['message']
        user_order.cartNumber=responses_dict['cardNumber']
        user_order.save()
        return HttpResponse(f"پرداخت شماره {order_id} با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse(
        f"پرداخت با شمار {order_id} با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت."
    )


