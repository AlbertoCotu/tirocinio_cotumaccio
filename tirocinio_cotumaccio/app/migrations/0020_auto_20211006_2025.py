# Generated by Django 3.2.5 on 2021-10-06 18:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20211006_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ricetta',
            options={'ordering': ('nome',)},
        ),
        migrations.RenameField(
            model_name='menusettimana',
            old_name='updated',
            new_name='approvato',
        ),
        migrations.AddField(
            model_name='menusettimana',
            name='creazione',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='menusettimana',
            name='creatore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.chef'),
        ),
    ]