# Generated by Django 5.1.5 on 2025-02-03 08:13

import EShop_account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=EShop_account.models.upload_profile_pic_path, verbose_name='عکس پروفایل'),
        ),
    ]
