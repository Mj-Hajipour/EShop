from django.urls import path

from .models import Product
from .views import ProductsList, product_detail, SearchProductsView, ProductsListByCategory, products_categories_partial

urlpatterns=[
    path('products',ProductsList.as_view()),
    path('products/<int:productId>',product_detail),
    path('products/search',SearchProductsView.as_view()),
    path('products/<str:category_name>',ProductsListByCategory.as_view()),
    path('products_categories_partial',products_categories_partial,name='products_categories_partial')
]