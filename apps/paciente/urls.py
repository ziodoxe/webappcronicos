from django.urls import path
from .views import crearPaciente

urlpatterns = [
   path('crear_paciente/', crearPaciente, name='crear_paciente')
]
