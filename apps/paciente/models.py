from django.db import models
from apps.historiaclinica.models import H_clinica
from apps.registro.models import Enfermedad, Medicacion

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
   documento_number=models.IntegerField('Numero de documento', blank=True, null=True)
   direccion=models.CharField(max_length=200, blank=False, null=False)
   localidad=models.CharField(max_length=200, blank=False, null=False)
   telefono=models.IntegerField(blank=False, null=False)
   correo=models.EmailField()
   estado=models.BooleanField('Estado', default=True)

   peso=models.IntegerField(blank=True, null=True)
   altura=models.FloatField(max_length=10, blank=True, null=True)
   pres_arterial=models.IntegerField(blank=True, null=True)
   hemog_glic=models.IntegerField('Hemoglobina Glicosilada', blank=True, null=True)
   saturacion_oxig=models.IntegerField(blank=True, null=True)
   frec_cardiaca=models.IntegerField(blank=True, null=True)
   fil_glomerular=models.IntegerField(blank=True, null=True)
   vacunacion=models.BooleanField('Ultimo refuerzo', default=True)
   temperatura=models.FloatField(max_length=10, blank=True, null=True)
   fuma=models.BooleanField('Fuma', default=False)
   indice_masa_corp=models.FloatField(max_length=10, blank=True, null=True)
   vef1=models.IntegerField(blank=True, null=True)
   enfermedad=models.ForeignKey(Enfermedad, null=True, blank=True, on_delete=models.CASCADE)
   medicacion=models.ForeignKey(Medicacion, null=True, blank=True, on_delete=models.CASCADE)


   class Meta:
      ordering=['nombres']

   def __str__(self):
      return self.nombres