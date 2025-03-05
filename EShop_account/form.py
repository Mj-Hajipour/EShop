
from django import forms
from django.contrib.auth.models import User
from django.core import validators



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا کلمه عبور خود را وارد نمایید'}),
        label='کلمه ی عبور'
    )
    def clean_username(self):
        username = self.cleaned_data['username']
        is_exist_user = User.objects.filter(username=username).exists()
        if not  is_exist_user:
            raise  forms.ValidationError('نام کاربری یا کلمه عبور اشتباه است')
        return username
class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری',
        validators=[
            validators.MinLengthValidator(limit_value=10,message="تعداد کارکتر نمی تواند کمتراز 10 کارکتر باشد"),
            validators.MaxLengthValidator(limit_value=100,message="تعداد کارکتر نمی تواند بیشتر از100 کارکتر باشد")
        ]
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا ایمیل خود را وارد کنید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمی باشد')
        ]

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا کلمه عبور خود را وارد کنید'}),
        label='کلمه عبور'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد کنید'}),
        label=' تکرار کلمه عبور'
    )
    def clean_username(self):
        username = self.cleaned_data['username']
        is_exist_user_by_username = User.objects.filter(username=username).exists()
        if is_exist_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام را انجام داده است')
        return username

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if  password != re_password:
           raise forms.ValidationError("کلمات عبور با هم مغابرتی ندارند")
        return password
    def clean_email(self):
        email = self.cleaned_data['email']
        is_exist_email = User.objects.filter(email=email).exists()
        if  is_exist_email:
            raise forms.ValidationError("با این ایمیل قبلا ثبت نام انجام شده است")
        return email


class EditUserForm(forms.Form):
    FirstName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'لطفا نام کاربری خود را وارد کنید'}),
        label='نام :'
    )
    LastName = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':"لطفا نام خانوداگی خود را وارد کنید"}),
        label='نام خانوادگی :'
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید'}),
        label='ایمیل :',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمی باشد')
        ]
    )
    profile_pic = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': False,'accept': 'image/*','placeholder':'یک عکس برای پروفایل خود انتخاب کنید'}),
        label='عکس پروفایل :',
        required=False,
    )

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address', 'postal_code', 'city', 'province', 'mobile', 'Emergency_call')
        labels = {
            'address': 'آدرس :',
            'postal_code': 'کدپستی :',
            'city': 'شهر :',
            'province': 'استان :',
            'mobile': 'شماره موبایل :',
            'Emergency_call': 'شماره تماس اضطراری :',
        }
        widgets = {
            'address': forms.Textarea(attrs={'rows': 6, 'cols': 30,'placeholder':'*آدرس :'}),
            'postal_code': forms.NumberInput(attrs={'placeholder': '*کدپستی :'}),
            'city': forms.TextInput(attrs={'placeholder': '*شهر :'}),
            'province': forms.TextInput(attrs={'placeholder': "*استان :"}),
            'mobile': forms.TextInput(attrs={'placeholder': '*شمارتماس :'}),
            'Emergency_call': forms.TextInput(attrs={'placeholder': '*شماره تماس اضطراری :'}),
        }

class AdditionalForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}),
        required=True,
        max_length=100,
        label='نام و نام خانوادگی :'
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'شماره موبایل'}),
        required=True,
        max_length=15,
        label='شماره موبایل :'
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'آدرس'}),
        required=True,
        label='آدرس :'
    )
    postal_code = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'کد پستی'}),
        required=True,
        max_length=10,
        label='کد پستی :'
    )


