# Generated by Django 5.0 on 2024-07-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]