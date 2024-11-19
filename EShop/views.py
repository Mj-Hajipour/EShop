from django.shortcuts import render,redirect
from EShop_Sliders.models import Slider
    


#header Code behind
def header(request, *args, **kwargs):
    context={

        }
    return render(request, 'Shared/Header.html', context)



def footer(request, *args, **kwargs):
    context={
        "Copy_right":"کلیه حقوق این وب سایت می رسد به",
        "author":"محمد جواد حاجی پور",
        "TID":"https://t.me/mjhajipour19"
    }
    return  render(request, 'Shared/Footer.html',context)
def home_page(request):
    sliders=Slider.objects.all()
    context={
        'data':'این فروشگاه با فریم ورک django نوشته شده است',
        'sliders':sliders
    }
    return render(request,"home_page.html",context)
