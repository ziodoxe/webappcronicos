# Generated by Django 2.2 on 2021-02-03 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_documento_localizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='dni_numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='localizacion',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
