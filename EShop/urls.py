from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import home_page

from EShop import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
]
if settings.DEBUG:
    #add root static files
      urlpatterns=urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #add media static files
      urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
