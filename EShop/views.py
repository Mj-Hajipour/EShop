from itertools import product
from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from EShop_Order.models import Order, OrderDetails
from EShop_Product.models import Product
from EShop_Product.views import products
from EShop_Sliders.models import Slider
from EShop_Settings.models import SiteSettings

from common.utils import my_grouper


#header Code behind
# partial_view



def header(request, *args, **kwargs):
    Site_setting = SiteSettings.objects.first()
    context={
        "setting": Site_setting,
        "OrCount":0
    }

    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is  None:
        order_details=[]
    else:
       order_details = open_order.orderdetails_set.all()
    grouped_details = {}
    for detail in order_details:
        Product_id = detail.product_id
        if Product_id not in grouped_details:
            grouped_details[Product_id] = {
                    'product': detail.product,
                    'quantity': detail.count,
            }
        else:
                grouped_details[Product_id]['quantity'] += detail.count

    Bag_items=list(grouped_details.values())
    Item=0
    for item in Bag_items:
        Item+=1
    context['OrCount']=Item

    return render(request, 'Shared/Header.html', context)



def footer(request, *args, **kwargs):
    Site_setting=SiteSettings.objects.first()
    context={
        "author":"محمد جواد حاجی پور",
        "TID":"https://t.me/mjhajipour19",
        "setting":Site_setting
    }
    return  render(request, 'Shared/Footer.html',context)
def home_page(request):
    sliders=Slider.objects.all()
    most_visit_products=Product.objects.all().order_by('-visit_count')[:8]
    last_product=Product.objects.all().order_by('-id')[:8]

    context={
        'data':'این فروشگاه با فریم ورک django نوشته شده است',
        'sliders':sliders,
        'most_visit':my_grouper(4,most_visit_products),
        'last_product':my_grouper(4,last_product),
    }
    return render(request,"home_page.html",context)

def about_page(request):
    Site_setting = SiteSettings.objects.first()
    context={
        'setting':Site_setting
    }
    return render(request,'about_page.html',context)


def _404_view(request):
    return render(request, '404.html')

@login_required(login_url='login')
def user_account_main_page(request):
    return render(request,'account/user_account_main.html',{})

@login_required(login_url='login')
def edit_user_profile(request):
    user_id=request.user.id
    return render(request,'account/edit_account.html',{})


def user_sidebar(request):
    return render(request,'account/user_sidebar.html',{})