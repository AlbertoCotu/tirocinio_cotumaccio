# Generated by Django 3.2.5 on 2021-09-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_menusettimana_ricette'),
    ]

    operations = [
        migrations.AddField(
            model_name='menusettimana',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='app.Tag'),
        ),
    ]
