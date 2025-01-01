from django.urls import path

from EShop_Contact.views import contact_page

urlpatterns = [
    path('contact-us',contact_page, name='contact' ),
]