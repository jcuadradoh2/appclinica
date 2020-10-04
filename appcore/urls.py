from django.urls import path
from .views import PacienteView, CrearPacienteView, EditarPacienteView, EliminarPacienteView
app_name = 'base'
urlpatterns = [
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('crear_paciente/', CrearPacienteView.as_view(), name='crear_paciente'),
    path('editar_paciente/<int:pk>/',
         EditarPacienteView.as_view(), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>/',
         EliminarPacienteView.as_view(), name='eliminar_paciente'),

]