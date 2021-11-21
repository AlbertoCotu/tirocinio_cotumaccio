# Generated by Django 3.2.5 on 2021-10-13 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0042_alter_menusettimana_aggiornato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menusettimana',
            name='aggiornato',
        ),
        migrations.AlterField(
            model_name='menusettimana',
            name='ricette',
            field=models.ManyToManyField(blank=True, to='app.Ricetta'),
        ),
        migrations.CreateModel(
            name='HistoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(editable=False)),
                ('istante', models.DateTimeField(editable=False)),
                ('text', models.TextField()),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menusettimana')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
