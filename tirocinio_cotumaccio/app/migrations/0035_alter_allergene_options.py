# Generated by Django 3.2.5 on 2021-10-09 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20211009_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allergene',
            options={'ordering': ('nome',)},
        ),
    ]
