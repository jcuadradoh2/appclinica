from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente, Doctor, Agenda
from .forms import PacienteForm, DoctorForm, CitaForm


class PacienteView(ListView):
    model = Paciente
    template_name = "core/paciente.html"
    context_object_name = "pacientes"
    #queryset = Paciente.objects.filter(estado=False)
    paginate_by = 7

    def get_queryset(self):
        nombre = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de pacientes"
        return context


class CrearPacienteView(CreateView):
    model = Paciente
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "core/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"


class EditarPacienteView(UpdateView):
    model = Paciente
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "core/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"


class EliminarPacienteView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        paciente =  Paciente.objects.get(id=pk)
        paciente.delete()
        # object.estado = False
        # object.save()
        return redirect('base:paciente')

#-----------------------------------------------------------------------Doctor


class CitaView(ListView):
    model = Agenda
    template_name = "core/cita.html"
    context_object_name = "cita"
    #queryset = Paciente.objects.filter(estado=False)
    paginate_by = 7

    # def get_queryset(self):
    #     fecha = self.request.GET.get(
    #         'fecha') if self.request.GET.get('fecha') else ''
    #     return self.model.objects.filter(fecha__icontains=fecha, estado=True)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['fecha'] = self.request.GET.get(
    #         'fecha') if self.request.GET.get('fecha') else ''
    #     context['titulo'] = "Consulta de citas"
    #     return context


class CrearCitaView(CreateView):
    model = Agenda
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "core/registrar_cita.html"
    form_class = CitaForm
    success_url = reverse_lazy('base:cita')
    context_object_name = "cita"


class EditarCitaView(UpdateView):
    model = Agenda
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "core/registrar_cita.html"
    form_class = CitaForm
    success_url = reverse_lazy('base:cita')
    context_object_name = "cita"


class EliminarCitaView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        cita = Agenda.objects.get(id=pk)
        cita.delete()
        # object.estado = False
        # object.save()
        return redirect('base:cita')


#-----------------------------------------------------------------------Index

class IndexView(TemplateView):
    template_name = "index.html"

#-----------------------------------------------------------------------Doctor

class DoctorView(ListView):
    model = Doctor
    template_name = "doctor_view.html"
    context_object_name = "datos"    
    paginate_by = 3

    def get_queryset(self):
        nombre = self.request.GET.get('nombre') if self.request.GET.get('nombre') else ''                
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''               
        return context


class CrearDoctorView(CreateView):
    model = Doctor    
    template_name = "doctor_new.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:doctor_view')
    context_object_name = "Doctor"

    
class EditarDoctorView(UpdateView):
    model = Doctor    
    template_name = "doctor_new.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:doctor_view')
    context_object_name = "Doctor"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foto'] = Doctor.objects.get(id=self.kwargs['pk'])
        return context


class EliminarDoctorView(DeleteView):    
    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        doctor = Doctor.objects.get(id=pk)
        doctor.delete()        
        return redirect('base:doctor_view')

#-----------------------------------------------------------------------Diagnostico

class DiagnosticoView(ListView):
    model = Doctor
    template_name = "diagnostico.html"
    context_object_name = "Diagnostico"    
    paginate_by = 3

    def get_queryset(self):
        nombre = self.request.GET.get('nombre') if self.request.GET.get('nombre') else ''                
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''               
        return context