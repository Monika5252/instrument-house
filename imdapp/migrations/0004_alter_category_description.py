# Generated by Django 4.1.2 on 2022-10-21 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdapp', '0003_category_description_category_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]