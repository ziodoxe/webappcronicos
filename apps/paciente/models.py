from django.db import models
from apps.historiaclinica.models import H_clinica

# Create your models here.

class Documento(models.Model):
   id=models.AutoField(primary_key=True)
   documento_tipo=models.CharField(max_length=200, blank=False, null=False)

   class Meta:
      ordering=['documento_tipo']

   def __str__(self):
      return '{}'.format(self.documento_tipo)


class Paciente(models.Model):
   id=models.AutoField(primary_key=True)
   nombres=models.CharField(max_length=200, blank=False, null=False)
   apellidos=models.CharField(max_length=200, blank=False, null=False)
   fnacimiento=models.DateField('Fecha de nacimiento', auto_now=False, auto_now_add=False)
   obra_social=models.BooleanField('Con Obra Social/Sin Obra Social', default=True)
   h_clinica=models.OneToOneField(H_clinica, null=True, blank=True, on_delete=models.CASCADE)
   documento_type=models.ForeignKey(Documento, null=True, blank=True, on_delete=models.CASCADE)
   documento_number=models.IntegerField(blank=True, null=True)
   direccion=models.CharField(max_length=200, blank=False, null=False)
   localidad=models.CharField(max_length=200, blank=False, null=False)
   telefono=models.IntegerField(blank=False, null=False)
   correo=models.EmailField()

   class Meta:
      ordering=['nombres']

   def __str__(self):
      return self.nombres