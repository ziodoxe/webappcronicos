from django.db import models
from apps.paciente.models import Paciente

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

class Registro(models.Model):
   id=models.AutoField(primary_key=True)
   peso=models.IntegerField(blank=True, null=True)
   altura=models.FloatField(max_length=10, blank=True, null=True)
   pres_arterial=models.IntegerField(blank=True, null=True)
   hemog_glic=models.IntegerField(blank=True, null=True)
   saturacion_oxig=models.IntegerField(blank=True, null=True)
   frec_cardiaca=models.IntegerField(blank=True, null=True)
   fil_glomerular=models.IntegerField(blank=True, null=True)
   vacunacion=models.BooleanField('Ultimo refuerzo', default=True)
   temperatura=models.FloatField(max_length=10, blank=True, null=True)
   fuma=models.BooleanField('Fuma', default=False)
   indece_masa_corp=models.FloatField(max_length=10, blank=True, null=True)
   vef1=models.IntegerField(blank=True, null=True)
   paciente=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
   enfermedad=models.ForeignKey(Enfermedad, null=True, blank=True, on_delete=models.CASCADE)
   medicacion=models.ForeignKey(Medicacion, null=True, blank=True, on_delete=models.CASCADE)

   class Meta:
      verbose_name='Registro'
      verbose_name_plural='Registros'
      ordering=['id']

   def __str__(self):
      return '{}'.format(self.id)
   