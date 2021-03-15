from django.urls import path
from .views import crearPaciente, listarPaciente, editarPaciente, eliminarPaciente

urlpatterns = [
   path('crear_paciente/', crearPaciente, name='crear_paciente'),
   path('listar_paciente/', listarPaciente, name='listar_paciente'),
   path('editar_paciente/<int:id>', editarPaciente, name='editar_paciente'),
   path('eliminar_paciente/<int:id>', eliminarPaciente, name='eliminar_paciente')
]