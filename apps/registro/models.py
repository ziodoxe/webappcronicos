from django.db import models

# Create your models here.

class Enfermedad(models.Model):
   id=models.AutoField(primary_key=True)
   nombre=models.CharField(max_length=100, null=True, blank=True)

   class Meta:
      verbose_name='Enfermedad'
      verbose_name_plural='Enfermedades'
      ordering=['nombre']

   def __str__(self):
       return self.nombre


class Medicacion(models.Model):
   id=models.AutoField(primary_key=True)
   marca=models.CharField(max_length=100, null=True, blank=True)
   nombres_drogas=models.CharField(max_length=100, null=True, blank=True)
   posologia=models.CharField(max_length=200, null=True, blank=True)

   class Meta:
      verbose_name='Medicacion'
      verbose_name_plural='Medicaciones'
      ordering=['marca']

   def __str__(self):
       return self.marca