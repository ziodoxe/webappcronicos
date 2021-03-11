from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
   class Meta:
      model=Paciente
      fields=['nombres', 'apellidos', 'fnacimiento', 'obra_social', 'h_clinica', 'documento_type']