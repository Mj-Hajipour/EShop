from django.urls import path

from .models import Product
from .views import ProductsList, product_detail,SearchProductsView

urlpatterns=[
    path('products',ProductsList.as_view()),
    path('products/<int:productId>',product_detail),
    path('products/search',SearchProductsView.as_view()),

]