# Generated by Django 5.1.5 on 2025-02-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop_account', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'عکس پروفایل', 'verbose_name_plural': 'پروفایل کاربران'},
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان'),
        ),
    ]
