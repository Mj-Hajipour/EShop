from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

def products(request):
    context={}
    return render(request,'products_list.html',context)

class ProductsList(ListView):
    template_name='products_list.html'
    paginate_by = 1

    def get_queryset(self):
         return  Product.objects.get_active_products()




def product_detail(request,*args,**kwargs):
    prodcut_id=kwargs['productId']
    product=Product.objects.get_by_id(prodcut_id)

    if  product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
    context={
          'product':product,
    }
    return render(request,'product_detail.html',context)

