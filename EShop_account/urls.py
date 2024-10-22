from django.urls import path

from .views import Login_user,register,logout_view

urlpatterns=[
    path('login',Login_user,name='login'),
    path('register',register,name='register'),
    path('logout',logout_view,name='logout'),
]