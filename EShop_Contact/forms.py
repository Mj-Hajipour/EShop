from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name= forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='نام و نام خانوادگی:',
        validators=[
            validators.MaxLengthValidator(150,'نام و نام خانوادگی شما باید کمتر از 150 کارکتر باشد')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control'}),
        label='ایمیل:',
        validators=[
            validators.MaxLengthValidator(100,'ایمیل شما نمی تواند بیشتر از 100 کارتر باشد')
        ]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='عنوان:',
        validators=[
            validators.MaxLengthValidator(200, 'عنوان پیام شما نمی تواند بیشتر از 100 کارتر باشد')
        ]
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class':'form-control'
            ,'rows':8,
            'style':'height:auto;'
        }),
        label='متن پیام:'
    )
