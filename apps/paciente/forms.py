from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
   class Meta:
      model=Paciente
      fields=[
         'nombres', 
         'apellidos', 
         'fnacimiento', 
         'obra_social', 
         'h_clinica', 
         'documento_type', 
         'documento_number', 
         'direccion', 
         'localidad', 
         'telefono', 
         'correo', 
         'peso', 
         'altura', 
         'pres_arterial', 
         'hemog_glic', 
         'saturacion_oxig', 
         'frec_cardiaca', 
         'fil_glomerular', 
         'vacunacion', 
         'temperatura', 
         'fuma', 
         'indice_masa_corp', 
         'vef1', 
         'enfermedad', 
         'medicacion'
      ]