# Generated by Django 4.1.2 on 2022-10-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdapp', '0004_alter_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]