from django.shortcuts import render, redirect
from .forms import PacienteForm
from .models import Paciente, Documento

# Create your views here.

def Home(request):
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
   pacientes=Paciente.objects.all()
   return render(request, 'paciente/listar_paciente.html', {'pacientes':pacientes})