# Generated by Django 4.1.2 on 2022-10-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdapp', '0002_stock_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='subcategory',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
