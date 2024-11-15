from django.http import Http404
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView
from unicodedata import category
from EShop_products_category.models import ProductCategory
from .models import Product
from Eshop_tag.models import Tag

# Create your views here.

def products(request):
    context={}
    return render(request,'products_list.html',context)

class ProductsList(ListView):
    template_name='products_list.html'
    paginate_by = 6

    def get_queryset(self):
         return  Product.objects.get_active_products()

class ProductsListByCategory(ListView):
    template_name='products_list.html'
    paginate_by = 6
    def get_queryset(self):
         category_name=self.kwargs['category_name']
         category=ProductCategory.objects.filter(name__iexact=category_name).first()
         if category is None:
             raise Http404('صفحه مورد نظر یافت نشد')
         return  Product.objects.get_products_by_category(category_name)


def product_detail(request,*args,**kwargs):
    product_id=kwargs['productId']
    product=Product.objects.get_by_id(product_id)

    if  product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
    context={
          'product':product,
    }

    # tag=Tag.objects.first()
    # print(tag.products.all())

    #دسترسی به مجموع تگ ها
    print(product.tag_set.all())
    #tag_set => set به معنای جدول واسطه می باشد
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

def  products_categories_partial(request):
    categories=ProductCategory.objects.all()
    contex={
        'categories':categories,
    }
    return render(request,'products_categories_partial.html',contex)