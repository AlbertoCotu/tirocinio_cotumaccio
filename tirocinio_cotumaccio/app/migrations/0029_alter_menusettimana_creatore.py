# Generated by Django 3.2.5 on 2021-10-07 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20211007_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusettimana',
            name='creatore',
            field=models.ForeignKey(blank=True, limit_choices_to={'impianto': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.impianto')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.chef'),
        ),
    ]
