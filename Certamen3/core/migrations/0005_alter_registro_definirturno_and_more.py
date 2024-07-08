# Generated by Django 5.0.6 on 2024-07-08 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_registro_fechaproduccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='DefinirTurno',
            field=models.CharField(choices=[('AM', 'Mañana'), ('PM', 'Tarde'), ('MM', 'Noche')], max_length=2, verbose_name='Turno'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='Horaregistro',
            field=models.TimeField(verbose_name='Hora de Registro'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='LitrosCombustible',
            field=models.FloatField(verbose_name='Litros de Combustible Cargados'),
        ),
    ]
