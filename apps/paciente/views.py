from django.shortcuts import render, redirect
from .forms import PacienteForm

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