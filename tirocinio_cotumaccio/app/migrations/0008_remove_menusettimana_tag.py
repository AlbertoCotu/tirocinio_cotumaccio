# Generated by Django 3.2.5 on 2021-09-04 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_tags_menusettimana_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menusettimana',
            name='tag',
        ),
    ]
