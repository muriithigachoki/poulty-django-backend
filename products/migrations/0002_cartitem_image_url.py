# Generated by Django 5.0.3 on 2024-03-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]