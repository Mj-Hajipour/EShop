# Generated by Django 5.1.5 on 2025-02-03 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EShop_account', '0004_remove_profile_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_picture',
            new_name='image',
        ),
    ]
