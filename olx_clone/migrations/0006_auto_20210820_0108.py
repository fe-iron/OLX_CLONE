# Generated by Django 3.2.6 on 2021-08-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx_clone', '0005_auto_20210820_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]