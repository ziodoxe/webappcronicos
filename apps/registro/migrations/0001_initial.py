# Generated by Django 2.2 on 2021-01-29 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('peso', models.IntegerField(blank=True, null=True)),
                ('altura', models.IntegerField(blank=True, null=True)),
                ('pres_arterial', models.IntegerField(blank=True, null=True)),
                ('hemog_glic', models.IntegerField(blank=True, null=True)),
                ('saturacion_oxig', models.IntegerField(blank=True, null=True)),
                ('frec_cardiaca', models.IntegerField(blank=True, null=True)),
                ('fil_glomerular', models.IntegerField(blank=True, null=True)),
                ('vacunacion', models.BooleanField(default=True, verbose_name='Ultimo refuerzo')),
                ('temperatura', models.FloatField(blank=True, max_length=10, null=True)),
                ('fuma', models.BooleanField(default=False, verbose_name='Fuma')),
                ('indece_masa_corp', models.FloatField(blank=True, max_length=10, null=True)),
                ('vef1', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'ordering': ['id'],
            },
        ),
    ]
