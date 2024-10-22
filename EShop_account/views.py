from django.shortcuts import render, redirect
from EShop_account.form import LoginForm
from django.contrib.auth import authenticate, login, logout,get_user_model

# Create your views here.


def Login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return  redirect('/admin')

    context={
        'login_form':login_form
    }
    return  render(request,'account/Login.html',context)


def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    context={}
    return  render(request,'account/Register.html',context)