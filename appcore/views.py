from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente, Doctor
from .forms import PacienteForm, DoctorForm


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

#-----------------------------------------------------------------------

class IndexView(TemplateView):
    template_name = "index.html"

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
        context['titulo'] = "Consulta de pacientes"          
        return context


class CrearDoctorView(CreateView):
    model = Doctor    
    template_name = "doctor_new.html"
    form_class = DoctorForm
    success_url = reverse_lazy('doctor_view')
    context_object_name = "Doctor"

    
class EditarDoctorView(UpdateView):
    model = Doctor    
    template_name = "doctor_new.html"
    form_class = DoctorForm
    success_url = reverse_lazy('doctor_view')
    context_object_name = "Doctor"


class EliminarDoctorView(DeleteView):    
    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        doctor = Doctor.objects.get(id=pk)
        doctor.delete()        
        return redirect('doctor_view')