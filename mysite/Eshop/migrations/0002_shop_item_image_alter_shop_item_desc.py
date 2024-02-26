# Generated by Django 5.0 on 2023-12-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='item_image',
            field=models.CharField(default='https://its.unl.edu/images/services/icons/eShop_Icon-01.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='shop',
            name='item_desc',
            field=models.CharField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae ratione ipsum tenetur quos expedita distinctio eligendi ea rem eum accusamus sit, dolore possimus tempore, veritatis qui dignissimos officiis fugiat quibusdam.', max_length=500),
        ),
    ]
