from django.shortcuts import render,redirect
from EShop_Sliders.models import Slider
from EShop_Settings.models import SiteSettings
    


#header Code behind
# partial_view
def header(request, *args, **kwargs):
    Site_setting = SiteSettings.objects.first()
    context={
        "setting": Site_setting
        }
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
    context={
        'data':'این فروشگاه با فریم ورک django نوشته شده است',
        'sliders':sliders
    }
    return render(request,"home_page.html",context)

def about_page(request):
    Site_setting = SiteSettings.objects.first()
    context={
        'setting':Site_setting
    }
    return render(request,'about_page.html',context)