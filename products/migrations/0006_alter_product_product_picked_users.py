# Generated by Django 4.0.1 on 2022-01-18 03:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_user_provider_accounts_id_user_provider_type_code'),
        ('products', '0005_productpickeduser_product_product_picked_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_picked_users',
            field=models.ManyToManyField(related_name='picked_products', through='products.ProductPickedUser', to=settings.AUTH_USER_MODEL),
        ),
    ]