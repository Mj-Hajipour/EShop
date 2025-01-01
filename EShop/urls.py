
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home_page,header,footer
from EShop import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('header',header,name="header"),
    path('footer',footer,name="footer"),
    path('', home_page,name="home"),
    path('',include('EShop_account.urls')),
    path('',include('EShop_Product.urls')),
    path('',include('EShop_Contact.urls')),

]
if settings.DEBUG:
    #add root static files
      urlpatterns=urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #add media static files
      urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
