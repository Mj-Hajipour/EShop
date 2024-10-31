from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

def products(request):
    context={}
    return render(request,'products_list.html',context)

class ProductsList(ListView):
    template_name='products_list.html'

    def get_queryset(self):
         return  Product.objects.get_active_products()



