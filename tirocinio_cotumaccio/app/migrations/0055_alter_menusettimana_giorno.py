# Generated by Django 3.2.5 on 2021-10-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_alter_tag_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusettimana',
            name='giorno',
            field=models.CharField(choices=[('1', 'Lunedi'), ('2', 'Martedi'), ('3', 'Mercoledi'), ('4', 'Giovedi'), ('5', 'Venerdi')], max_length=9),
        ),
    ]
