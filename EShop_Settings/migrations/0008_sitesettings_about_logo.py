# Generated by Django 5.1.2 on 2025-01-09 05:39

import EShop_Settings.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop_Settings', '0007_sitesettings_copy_right'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='About_logo',
            field=models.ImageField(blank=True, null=True, upload_to=EShop_Settings.models.upload_settings_image_path, verbose_name='تصویر لوگو درباره ما'),
        ),
    ]
