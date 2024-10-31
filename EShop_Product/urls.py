from django.urls import path

from .models import Product
from .views import products, ProductsList

urlpatterns=[
    path('products-function',products,name='products'),
    path('products',ProductsList.as_view(),name='products'),

]