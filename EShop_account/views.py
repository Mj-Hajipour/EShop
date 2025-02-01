from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from EShop_account.form import LoginForm, RegisterForm, EditUserForm
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.models import User



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
            if request.user.is_superuser:
                return  redirect('/admin/')
            else:
                return redirect('/')
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


@login_required(login_url='login')
def user_account_main_page(request):
    return render(request, 'account/user_account_main.html', {})


@login_required(login_url='login')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    edit_user_profile = EditUserForm(request.POST or None,
                                     initial={'FirstName':user.first_name,'LastName':user.last_name,'email':user.email})
    if edit_user_profile.is_valid():
        first_name = edit_user_profile.cleaned_data.get('FirstName')
        last_name = edit_user_profile.cleaned_data.get('LastName')
        email=edit_user_profile.cleaned_data.get('email')
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
    context = {
       'edit_form':edit_user_profile
   }
    return render(request, 'account/edit_account.html',context )


def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})