# Generated by Django 3.2.5 on 2021-09-04 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_menusettimana_ricette'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagricetta',
            name='ricetta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ricetta'),
        ),
    ]