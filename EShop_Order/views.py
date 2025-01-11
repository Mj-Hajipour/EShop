from itertools import product

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from EShop_Order.form import UserNewOrderForm
from EShop_Order.models import  Order
from EShop_Product.models import Product


# Create your views here.

@login_required(login_url='/login')
def add_user_order(request):
    new_order_form=UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order=Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
        if order is None:
            order=Order.objects.create(owner_id=request.user.id,is_paid=False)
        product_id=new_order_form.cleaned_data['product_id']
        count=new_order_form.cleaned_data['count']
        if count<0 :
            count=1
        product = Product.objects.get_by_id(product_id=product_id)
        order.orderdetails_set.create(product_id=product_id,price=product.price,count=count)

         #best
        return redirect(f'/products/{product.id}')

    return redirect('/')