from django.urls import path
from .views import crearPaciente, editarPaciente, eliminarPaciente, ListadoPaciente, CrearPaciente

urlpatterns = [
   path('crear_paciente/', CrearPaciente.as_view(), name='crear_paciente'),
   path('listar_paciente/', ListadoPaciente.as_view(), name='listar_paciente'),
   path('editar_paciente/<int:id>', editarPaciente, name='editar_paciente'),
   path('eliminar_paciente/<int:id>', eliminarPaciente, name='eliminar_paciente')
]