# Generated by Django 3.2.5 on 2021-10-07 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_menusettimana_creazione'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChefManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.chef')),
                ('impianto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.impianto')),
            ],
            options={
                'unique_together': {('impianto', 'impianto')},
            },
        ),
    ]
