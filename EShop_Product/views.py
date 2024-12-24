import itertools

from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from EShop_products_category.models import ProductCategory
from .models import Product, ProductGallery


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

def my_grouper(n,iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))



def product_detail(request,*args,**kwargs):
    selected_product_id=kwargs['productId']
    product=Product.objects.get_by_id(selected_product_id)

    if  product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')

    related_products=Product.objects.get_queryset().filter(categories__product=product).distinct()

    grouped_related_products=my_grouper(3,related_products)

    galleries=ProductGallery.objects.filter(product_id=selected_product_id)

    grouped_galleries=list(my_grouper(3,galleries))

    context={
        'product':product,
        'galleries':grouped_galleries,
        'related_products':grouped_related_products,
    }
    # tag=Tag.objects.first()
    # print(tag.products.all())

    #دسترسی به مجموع تگ ها
    # print(product.tag_set.all())
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