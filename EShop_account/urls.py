from django.urls import path
from django.views.generic import edit

from .views import  edit_user_profile
from .views import Login_user, register, logout_view, user_account_main_page

urlpatterns=[
    path('login',Login_user,name='login'),
    path('register',register,name='register'),
    path('logout',logout_view,name='logout'),
    path('user', user_account_main_page),
    path('user/edit',edit_user_profile,name='edit'),

]