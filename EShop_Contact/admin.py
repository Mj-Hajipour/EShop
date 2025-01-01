from django.contrib import admin

from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name','subject','is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['subject']
# Register your models here.
admin.site.register(ContactUs,ContactUsAdmin)
    
