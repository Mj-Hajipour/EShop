from cProfile import label
from wsgiref.validate import validator

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

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
        label='نام کاربری'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'لطفا ایمیل خود را وارد کنید'}),
        label='ایمیل',

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
        print(username)
        is_exist_user_by_username = User.objects.filter(username=username).exists()
        if is_exist_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام را انجام داده است')
        return username

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        print(password, re_password)
        if  password != re_password:
            self.add_error('re_password', 'کلمه‌های عبور باهم مطابقت ندارند')
        return cleaned_data
