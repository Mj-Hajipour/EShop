from django.urls import path

from .models import Product
from .views import ProductsList, product_detail

urlpatterns=[
    path('products',ProductsList.as_view()),
    path('products/<productId>',product_detail)

]