# Generated by Django 5.0.6 on 2024-07-08 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_registro_ultimaedicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='FechaProduccion',
            field=models.DateField(verbose_name='Fecha de Produccion'),
        ),
    ]
