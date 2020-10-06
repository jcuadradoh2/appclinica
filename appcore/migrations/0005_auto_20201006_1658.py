# Generated by Django 3.1.1 on 2020-10-06 21:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcore', '0004_auto_20201004_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='fecha',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Agenda'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora',
            field=models.TimeField(default=datetime.time(16, 58, 22, 531301), verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.IntegerField(choices=[(3, 'Miercoles'), (6, 'Sabado'), (1, 'Lunes'), (0, 'Domingo'), (5, 'Viernes'), (2, 'Martes'), (4, 'Jueves'), (7, 'Domingo')], default=1, verbose_name='Dia'),
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatura', models.FloatField(default=1.6, verbose_name='estatura')),
                ('peso', models.IntegerField(verbose_name='peso')),
                ('masa', models.FloatField(blank=True, default=0, null=True, verbose_name='Masa Corporal')),
                ('temperatura', models.FloatField(verbose_name='Temperatura')),
                ('frecRespira', models.IntegerField(blank=True, default=0, null=True, verbose_name='Frecuencia Respiratoria')),
                ('frecCard', models.IntegerField(blank=True, default=0, null=True, verbose_name='Frecuencia Cardiaca')),
                ('porGraCor', models.IntegerField(blank=True, default=0, null=True, verbose_name='Porcentaje Grasa Corporal')),
                ('porMasaMus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Porcentaje Masa Muscular')),
                ('precionArt', models.CharField(max_length=10, verbose_name='Precion Arterial')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appcore.agenda')),
            ],
            options={
                'verbose_name': 'SignosVitales',
                'verbose_name_plural': 'SignosVitales',
            },
        ),
    ]
