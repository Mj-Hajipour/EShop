from django.contrib import admin
from django.contrib.auth.models import User

from EShop_account.models import Profile, UserProfile, Invoice

admin.site.register(Profile)
admin.site.register(UserProfile)
admin.site.register(Invoice)