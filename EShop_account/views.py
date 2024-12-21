from django.shortcuts import render, redirect
from EShop_account.form import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.models import User
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
        else:
            login_form.add_error('username', 'رمز عبور یا نام کاربری اشتباه است')

    context={
        'login_form':login_form
    }
    return  render(request,'account/Login.html',context)


def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        username = register_form.cleaned_data['username']
        email = register_form.cleaned_data['email']
        password = register_form.cleaned_data['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login')

    context={
        'register_form':register_form
    }
    return  render(request,'account/Register.html',context)