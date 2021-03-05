from django.db import models

# Create your models here.
class H_clinica(models.Model):
   id=models.AutoField(primary_key=True)
   estado=models.BooleanField('Visible/Oculto', default=True)
   fecha_creacion=models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

   class Meta:
      verbose_name='H_clinica'
      verbose_name_plural='H_clinicas'
      ordering=['id']

   def __str__(self):
      return '{}'.format(self.id)