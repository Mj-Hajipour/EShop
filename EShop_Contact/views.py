from django.shortcuts import  render
from EShop_Contact.forms import CreateContactForm
from .models import  ContactUs
from EShop_Settings.models import SiteSettings



# Create your views here.
def contact_page(request):
    contact_form=CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data['full_name']
        email = contact_form.cleaned_data['email']
        subject = contact_form.cleaned_data['subject']
        text = contact_form.cleaned_data['text']
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text)
        #todo :show user a success message
        contact_form=CreateContactForm()

    Site_Settings=SiteSettings.objects.first()
    context = {
        'contact_form':contact_form,
        'settings': Site_Settings,
    }
    return render(request,'contact_us/contact_us_page.html',context)
