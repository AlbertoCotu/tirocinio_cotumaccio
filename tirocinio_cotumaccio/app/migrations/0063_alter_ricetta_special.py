# Generated by Django 3.2.8 on 2021-11-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_alter_impianto_classificazione'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ricetta',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
