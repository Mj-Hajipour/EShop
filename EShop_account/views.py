
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from EShop_Order.models import Order, OrderDetails
from EShop_Product.models import Product
from EShop_account.form import LoginForm, RegisterForm, EditUserForm, UserProfileForm, AdditionalForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from EShop_account.models import Profile, UserProfile, Invoice


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
                return redirect('/admin/')
            else:
                return redirect('/')
        else:
            login_form.add_error('username', 'رمز عبور یا نام کاربری اشتباه است')

    context = {
        'login_form': login_form
    }
    return render(request, 'account/Login.html', context)


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

    context = {
        'register_form': register_form
    }
    return render(request, 'account/Register.html', context)


@login_required(login_url='login')
def user_account_main_page(request):
    return render(request, 'account/user_account_main.html', {})


@login_required(login_url='login')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    profile = Profile.objects.get(user_id=user_id)
    edit_user_profile = EditUserForm(request.POST or None,
                                     initial={'FirstName': user.first_name, 'LastName': user.last_name,
                                              'email': user.email, 'profile_pic': profile.image})
    if edit_user_profile.is_valid():
        first_name = edit_user_profile.cleaned_data.get('FirstName')
        last_name = edit_user_profile.cleaned_data.get('LastName')
        email = edit_user_profile.cleaned_data.get('email')
        profile_pic = edit_user_profile.cleaned_data.get('profile_pic')
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        profile.image = profile_pic
        user.is_active = True
        user.Is_staff = False
        user.Is_superuser = False
        user.save()
        profile.save()
    context = {
        'edit_form': edit_user_profile
    }
    return render(request, 'account/edit_account.html', context)


@login_required(login_url='login')
def user_panel(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    profile = Profile.objects.get(user_id=user_id)
    try:
        userprofile = UserProfile.objects.get(user_id=user_id)
    except userprofile.DoesNotExist:
        userprofile = UserProfile(user_id=user_id)
        userprofile.save()
    profile_pic = profile.image
    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, instance=userprofile)
        if profile_form.is_valid():
            userprofile.address = profile_form.cleaned_data.get('address')
            userprofile.postal_code = profile_form.cleaned_data.get('postal_code')
            userprofile.city = profile_form.cleaned_data.get('city')
            userprofile.mobile = profile_form.cleaned_data.get('mobile')
            userprofile.Emergency_call = profile_form.cleaned_data.get('Emergency_call')
            userprofile.province = profile_form.cleaned_data.get('province')
            userprofile.save()
    else:
        profile_form = UserProfileForm(instance=userprofile)
    AddForm = AdditionalForm(request.POST or None)

    context = {
        'user': user,
        'profile_pic': profile_pic,
        'profile_form': profile_form,
        'AddForm': AddForm,
    }
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
       factor = Invoice.objects.filter(order_id=open_order.id).first()
       if factor is None:
           context['factor'] = False
       else:
           context['factor'] = True



    return render(request, 'account/user_panel.html', context)




@login_required(login_url='login')
def invoice_create(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    open_order = Order.objects.get(owner_id=user_id, is_paid=False)
    order_details = open_order.orderdetails_set.all()
    userprofile = UserProfile.objects.get(user_id=user_id)
    if not Invoice.objects.filter(order_id=open_order.id).exists():
         Ivoice = Invoice.objects.create(order_id=open_order.id, user_id=user_id, UserProfile_id=userprofile.id)
         Ivoice.save()
    if request.method == "POST":
         if request.POST.get('options')=='option1':
             Ivoice = Invoice.objects.get(order_id=open_order.id)
             Ivoice.Shipping_FullName = user.first_name + " " + user.last_name
             Ivoice.Shipping_Address = userprofile.province + " " + userprofile.city + " " + userprofile.address
             Ivoice.Shipping_PostalCode = userprofile.postal_code
             Ivoice.Shipping_Mobile = userprofile.mobile
             Ivoice.save()
         elif request.POST.get('options')=='option2':
             addForm = AdditionalForm(request.POST or None)
             if addForm.is_valid():
                 fullname_form = addForm.cleaned_data.get('full_name')
                 address_form = addForm.cleaned_data.get('address')
                 postal_form = addForm.cleaned_data.get('postal_code')
                 mobile_form = addForm.cleaned_data.get('mobile')
                 Ivoice.Shipping_FullName = fullname_form
                 Ivoice.Shipping_Address = address_form
                 Ivoice.Shipping_PostalCode = postal_form
                 Ivoice.Shipping_Mobile = mobile_form
                 Ivoice.save()

    return redirect("/open-order")

@login_required(login_url='login')
def order_history(request):
    user_id = request.user.id
    Ivoices=Invoice.order_item.get_by_id(user_id).prefetch_related(
        'order__orderdetails_set__product')
    context = {
        'Ivoices': Ivoices,
    }
    return render(request, 'account/user_history_orders.html', context)


def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})
