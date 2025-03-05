from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from EShop_account.models import UserProfile

@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            adress1='',
            adress2='',
            postal_code=0,
            city='',
            province='',
            mobile='',
            emergency_call=''
        )

@receiver(post_save,sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.userprofile.save()