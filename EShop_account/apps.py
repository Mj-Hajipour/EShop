from django.apps import AppConfig


class EshopAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EShop_account'
    verbose_name = 'ماژول پروفایل کاربران'

class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import  EShop_account.signals