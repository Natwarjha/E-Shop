# Generated by Django 5.0 on 2023-12-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0002_shop_item_image_alter_shop_item_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='for_user',
            field=models.CharField(default='ShopOwner', max_length=30),
        ),
    ]
