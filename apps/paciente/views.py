from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import PacienteForm
from .models import Paciente, Documento
from django.views.generic import View

# Create your views here.

def home(request):
   return render(request, 'index.html')

class Inicio(View):
   def get(self, request, *args, **kwargs):
      return render(request, 'index.html')

def crearPaciente(request):
   if request.method=='POST':
      paciente_form=PacienteForm(request.POST)
      if paciente_form.is_valid():
         paciente_form.save()
         return redirect('index')
   else:
      paciente_form=PacienteForm()
   return render(request, 'paciente/crear_paciente.html', {'paciente_form':paciente_form})

def listarPaciente(request):
   pacientes=Paciente.objects.filter(estado=True)
   return render(request, 'paciente/listar_paciente.html', {'pacientes':pacientes})

def editarPaciente(request, id):
   paciente_form=None
   error=None
   try:
      paciente=Paciente.objects.get(id=id)
      if request.method=='GET':
         paciente_form=PacienteForm(instance=paciente)
      else:
         paciente_form=PacienteForm(request.POST, instance=paciente)
         if paciente_form.is_valid():
            paciente_form.save()
         return redirect('index')
   except ObjectDoesNotExist as e:
      error=e
   
   return render(request, 'paciente/crear_paciente.html', {'paciente_form':paciente_form, 'error':error})

def eliminarPaciente(request, id):
   paciente=Paciente.objects.get(id=id)
   if request.method=='POST':
      paciente.estado=False
      paciente.save()
      return redirect('paciente:listar_paciente')
   return render(request, 'paciente/eliminar_paciente.html', {'paciente':paciente})