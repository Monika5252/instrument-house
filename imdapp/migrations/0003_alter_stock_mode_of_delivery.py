# Generated by Django 4.1.2 on 2022-11-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdapp', '0002_stock_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Mode_of_delivery',
            field=models.CharField(choices=[('BY-HAND', 'BY-HAND'), ('COURIER', 'COURIER'), ('OTHER', 'OTHER')], max_length=50),
        ),
    ]
