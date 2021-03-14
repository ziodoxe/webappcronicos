from django.urls import path
from .views import crearPaciente, listarPaciente

urlpatterns = [
   path('crear_paciente/', crearPaciente, name='crear_paciente'),
   path('listar_paciente/', listarPaciente, name='listar_paciente')
]
