# Generated by Django 2.2 on 2021-03-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_auto_20210202_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fnacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
    ]