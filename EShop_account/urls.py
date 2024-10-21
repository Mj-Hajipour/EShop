from django.urls import path

from .views import Login,register

urlpatterns=[
    path('login',Login,name='login'),
    path('register',register,name='register'),
]