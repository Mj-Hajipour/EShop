from django.urls import path

from EShop_Order.views import add_user_order, user_open_order

urlpatterns=[
   path('add-user-order',add_user_order),
   path('user-open-order',user_open_order),
]
