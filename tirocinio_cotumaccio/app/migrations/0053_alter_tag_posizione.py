# Generated by Django 3.2.5 on 2021-10-14 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_auto_20211014_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='posizione',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
