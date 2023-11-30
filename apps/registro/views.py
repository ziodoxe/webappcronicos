from django.db import models
from django.shortcuts import render
from .models import Enfermedad, Medicacion
from django.views.generic import TemplateView, ListView

# Create your views here.

class ListarEnfermedad(ListView):
   models=Enfermedad
   template_name='paciente/crear_paciente.html'
   context_object_name='enfermedades'


class ListarMedicacion(ListView):
   models=Medicacion
   template_name='paciente/crear_paciente.html'
   context_object_name='medicaciones'
