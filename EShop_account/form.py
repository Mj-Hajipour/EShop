from cProfile import label


from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


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
        user_name = self.cleaned_data['username']
        is_exist_user=User.objects.filter(username=user_name).exists()
        if not is_exist_user:
            raise forms.ValidationError('رمز عبور یا نام کاربری اشتباه است')
        return  user_name
class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'لطفا ایمیل خود را وارد کنید'}),
        label='ایمیل'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا کلمه عبور خود را وارد کنید'}),
        label='کلمه عبور'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا کلمه عبور خود را تکرار کنید'}),
        label='تکرار کلمه عبور'
    )
    def clean_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            raise  forms.ValidationError('کلمه های عبور به هم متفاوت هستند')
        return password