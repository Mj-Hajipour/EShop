from django.urls import path


from EShop_Order.views import add_user_order, user_open_order, go_to_gateway_view, callback_gateway_view

urlpatterns=[
   path('add-user-order',add_user_order),
   path('open-order',user_open_order),
   path('request',go_to_gateway_view),
   path('callback-gateway/<order_id>',callback_gateway_view)
]
