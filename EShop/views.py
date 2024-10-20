from lib2to3.fixes.fix_input import context

from django.shortcuts import render,redirect

def home_page(request):
    context={
        'data':'new data'
    }
    return render(request,"home_page.html",context)