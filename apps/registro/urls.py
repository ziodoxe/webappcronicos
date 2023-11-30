from django.urls import path
from .views import ListarMedicacion, ListarEnfermedad

urlpatterns = [
   path('crear_paciente/', ListarMedicacion.as_view(), name='crear_paciente'),
   path('crear_paciente/', ListarEnfermedad.as_view(), name='crear_paciente'),
]