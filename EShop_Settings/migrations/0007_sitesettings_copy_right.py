# Generated by Django 5.1.2 on 2025-01-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop_Settings', '0006_alter_sitesettings_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='copy_right',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='متن کپی رایت'),
        ),
    ]
