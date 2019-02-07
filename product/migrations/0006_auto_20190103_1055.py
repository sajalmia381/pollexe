# Generated by Django 2.1.4 on 2019-01-03 04:55

from django.db import migrations, models
import product.utils


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, upload_to=product.utils.get_product_images_name),
        ),
    ]
