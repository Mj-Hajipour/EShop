from django.urls import path
from django.views.generic import edit

from .views import edit_user_profile, user_panel, order_history, invoice_create
from .views import Login_user, register, logout_view, user_account_main_page

urlpatterns=[
    path('login',Login_user,name='login'),
    path('register',register,name='register'),
    path('logout',logout_view,name='logout'),
    path('user', user_account_main_page),
    path('user/edit',edit_user_profile,name='edit'),
    path('user/panel',user_panel,name='user_panel'),
    path('user/history', order_history, name='user_panel'),
    path('user/invoice',invoice_create)

]