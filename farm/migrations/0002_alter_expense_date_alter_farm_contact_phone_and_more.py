# Generated by Django 5.0.3 on 2024-03-23 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='farm',
            name='contact_phone',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='sale_date',
            field=models.DateField(),
        ),
    ]