# Generated by Django 5.1.2 on 2024-11-19 07:43

import EShop_Sliders.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('link', models.URLField(max_length=100, verbose_name='آدرس')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=EShop_Sliders.models.upload_image_path, verbose_name='تصویر')),
            ],
        ),
    ]
