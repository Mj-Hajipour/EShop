from lib2to3.fixes.fix_input import context

from django.shortcuts import render,redirect

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
    context={
        'data':'این فروشگاه با فریم ورک django نوشته شده است'
    }
    return render(request,"home_page.html",context)
