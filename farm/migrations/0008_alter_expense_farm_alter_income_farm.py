# Generated by Django 5.0.3 on 2024-03-26 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0007_alter_farm_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='farm',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='income',
            name='farm',
            field=models.CharField(max_length=50),
        ),
    ]
