# Generated by Django 2.2 on 2021-03-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0010_auto_20210311_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='documento_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Numero de documento'),
        ),
    ]