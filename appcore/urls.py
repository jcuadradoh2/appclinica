from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import * #PacienteView, CrearPacienteView, EditarPacienteView, EliminarPacienteView, DoctorView, EditarDoctorView, EliminarDoctorView, CrearDoctorView, IndexView
app_name = 'base'
urlpatterns = [
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('crear_paciente/', CrearPacienteView.as_view(), name='crear_paciente'),
    path('editar_paciente/<int:pk>/',
         EditarPacienteView.as_view(), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>/',
         EliminarPacienteView.as_view(), name='eliminar_paciente'),

    path('cita/', CitaView.as_view(), name='cita'),
    path('crear_cita/', CrearCitaView.as_view(), name='crear_cita'),
    path('editar_cita/<int:pk>/',
         EditarCitaView.as_view(), name='editar_cita'),
    path('eliminar_cita/<int:pk>/',
         EliminarCitaView.as_view(), name='eliminar_cita'),

     path('', IndexView.as_view(), name='index'),  
     path('doctor_view/', login_required(DoctorView.as_view()), name='doctor_view'), 
     path('doctor/', CrearDoctorView.as_view(), name='doctor'), 
     path('doctor_edit/<int:pk>/', EditarDoctorView.as_view(), name='doctor_edit'),
     path('doctor_delete/<int:pk>/', EliminarDoctorView.as_view(), name='doctor_delete'),

]
