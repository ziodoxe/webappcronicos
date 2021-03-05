from django.db import models
from apps.historiaclinica.models import H_clinica

# Create your models here.

class Documento(models.Model):
   id=models.AutoField(primary_key=True)
   documento_tipo=models.CharField(max_length=200, blank=False, null=False)
   dni_numero=models.IntegerField(blank=True, null=True)

   class Meta:
      ordering=['dni_numero']

   def __str__(self):
      return '{}'.format(self.dni_numero)


class Localizacion(models.Model):
   id=models.AutoField(primary_key=True)
   direccion=models.CharField(max_length=200, blank=False, null=False)
   localidad=models.CharField(max_length=200, blank=False, null=False)
   telefono=models.IntegerField(blank=False, null=False)
   correo=models.EmailField()

   class Meta:
      verbose_name='Localizacion'
      verbose_name_plural='Localizaciones'
      ordering=['localidad']

   def __str__(self):
      return self.localidad


class Paciente(models.Model):
   id=models.AutoField(primary_key=True)
   nombres=models.CharField(max_length=200, blank=False, null=False)
   apellidos=models.CharField(max_length=200, blank=False, null=False)
   fnacimiento=models.DateField('Fecha de nacimiento', auto_now=True, auto_now_add=False)
   obra_social=models.BooleanField('Activo/Desactivo', default=True)
   h_clinica=models.OneToOneField(H_clinica, null=True, blank=True, on_delete=models.CASCADE)
   documento=models.ForeignKey(Documento, null=True, blank=True, on_delete=models.CASCADE)
   localizacion=models.ForeignKey(Localizacion, null=True, blank=True, on_delete=models.CASCADE)

   class Meta:
      ordering=['nombres']

   def __str__(self):
      return self.nombres