from django.urls import path
from .views import crearPaciente, listarPaciente, editarPaciente

urlpatterns = [
   path('crear_paciente/', crearPaciente, name='crear_paciente'),
   path('listar_paciente/', listarPaciente, name='listar_paciente'),
   path('editar_paciente/<int:id>', editarPaciente, name='editar_paciente')
]
