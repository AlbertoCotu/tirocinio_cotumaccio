# Generated by Django 3.2.5 on 2021-10-06 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_rename_approvato_menusettimana_approvazione'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusettimana',
            name='creazione',
            field=models.DateTimeField(blank=True, default=datetime.date(2021, 10, 6)),
        ),
    ]
