from django.contrib import admin
from .models import Product,ProductGallery

# Register your models here.

class AdminProducts(admin.ModelAdmin):
     list_display = ['__str__','title','price','active']
     class Meta:
         model = Product

admin.site.register(Product,AdminProducts)
admin.site.register(ProductGallery)
