# Generated by Django 2.0.2 on 2018-02-26 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='image',
        ),
    ]
