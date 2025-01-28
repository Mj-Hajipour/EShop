from azbankgateways.urls import az_bank_gateways_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home_page, header, footer, about_page, _404_view
from EShop import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('header',header,name="header"),
    path('footer',footer,name="footer"),
    path('', home_page,name="home"),
    path('about-us',about_page),
    path('',include('EShop_account.urls')),
    path('',include('EShop_Product.urls')),
    path('',include('EShop_Contact.urls')),

    path('',include('EShop_Order.urls')),

    path("bankgateways/", az_bank_gateways_urls()),

    path("_404_view",_404_view)


]
if settings.DEBUG:
    #add root static files
      urlpatterns=urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #add media static files
      urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
