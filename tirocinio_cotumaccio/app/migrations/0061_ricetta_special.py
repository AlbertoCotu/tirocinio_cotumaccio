# Generated by Django 3.2.8 on 2021-11-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_impianto_classificazione'),
    ]

    operations = [
        migrations.AddField(
            model_name='ricetta',
            name='special',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
