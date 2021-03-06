# Generated by Django 2.2 on 2021-02-03 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_auto_20210202_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.Documento'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='localizacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.Localizacion'),
        ),
    ]
