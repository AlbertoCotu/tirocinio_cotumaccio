# Generated by Django 3.2.5 on 2021-10-13 10:28

import app.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20211013_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusettimana',
            name='anno',
            field=models.PositiveIntegerField(default=2021, editable=False, validators=[django.core.validators.MinValueValidator(1984), app.models.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='menusettimana',
            name='giorno',
            field=models.CharField(choices=[('Lunedi', 'Lunedi'), ('Martedi', 'Martedi'), ('Mercoledi', 'Mercoledi'), ('Giovedi', 'Giovedi'), ('Venerdi', 'Venerdi')], editable=False, max_length=9),
        ),
        migrations.AlterField(
            model_name='menusettimana',
            name='impianto',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='app.impianto'),
        ),
        migrations.AlterField(
            model_name='menusettimana',
            name='settimana',
            field=models.CharField(choices=[('1', 'Settimana 1'), ('2', 'Settimana 2'), ('3', 'Settimana 3'), ('4', 'Settimana 4'), ('5', 'Settimana 5'), ('6', 'Settimana 6'), ('7', 'Settimana 7'), ('8', 'Settimana 8'), ('9', 'Settimana 9'), ('10', 'Settimana 10'), ('11', 'Settimana 11'), ('12', 'Settimana 12'), ('13', 'Settimana 13'), ('14', 'Settimana 14'), ('15', 'Settimana 15'), ('16', 'Settimana 16'), ('17', 'Settimana 17'), ('18', 'Settimana 18'), ('19', 'Settimana 19'), ('20', 'Settimana 20'), ('21', 'Settimana 21'), ('22', 'Settimana 22'), ('23', 'Settimana 23'), ('24', 'Settimana 24'), ('25', 'Settimana 25'), ('26', 'Settimana 26'), ('27', 'Settimana 27'), ('28', 'Settimana 28'), ('29', 'Settimana 29'), ('30', 'Settimana 30'), ('31', 'Settimana 31'), ('32', 'Settimana 32'), ('33', 'Settimana 33'), ('34', 'Settimana 34'), ('35', 'Settimana 35'), ('36', 'Settimana 36'), ('37', 'Settimana 37'), ('38', 'Settimana 38'), ('39', 'Settimana 39'), ('40', 'Settimana 40'), ('41', 'Settimana 41'), ('42', 'Settimana 42'), ('43', 'Settimana 43'), ('44', 'Settimana 44'), ('45', 'Settimana 45'), ('46', 'Settimana 46'), ('47', 'Settimana 47'), ('48', 'Settimana 48'), ('49', 'Settimana 49'), ('50', 'Settimana 50'), ('51', 'Settimana 51'), ('52', 'Settimana 52')], editable=False, max_length=12),
        ),
    ]
