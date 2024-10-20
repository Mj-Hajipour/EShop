from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.


def Login(request):
    context={}
    return  render(request,'account/Login.html',context)