from django.http import Http404
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView
from .models import Product

# Create your views here.

def products(request):
    context={}
    return render(request,'products_list.html',context)

class ProductsList(ListView):
    template_name='products_list.html'
    paginate_by = 2

    def get_queryset(self):
         return  Product.objects.get_active_products()




def product_detail(request,*args,**kwargs):
    product_id=kwargs['productId']
    product=Product.objects.get_by_id(product_id)

    if  product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
    context={
          'product':product,
    }
    return render(request,'product_detail.html',context)

class SearchProductsView(ListView):
    template_name='products_list.html'
    paginate_by = 6
    def get_queryset(self):
        request=self.request
        query=request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active_products()

'''
   __icontains =>this contains this 
   __iexact => field is exactly this
'''