# Generated by Django 3.2.5 on 2021-09-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_carta_menusettimana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusettimana',
            name='ricette',
            field=models.ManyToManyField(blank=True, null=True, to='app.Ricetta'),
        ),
    ]
