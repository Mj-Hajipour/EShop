# Generated by Django 5.1.5 on 2025-02-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop_account', '0015_alter_invoice_shipping_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Shipping_PostalCode',
            field=models.PositiveIntegerField(verbose_name='کد پستی گیرنده :'),
        ),
    ]
