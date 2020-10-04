from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import DoctorForm
from django.urls.base import reverse_lazy
from .models import Doctor

# Create your views here.  form.cleaned_data['renewal_date']
class IndexView(TemplateView):
    template_name = "index.html"

#class EmpleadosView(TemplateView):
#    template_name = "empleados_view.html"


class EmpleadosView(ListView):
    model = Doctor
    template_name = "empleados_view.html"
    context_object_name = "datos"
    #queryset = Paciente.objects.filter(estado=False)
    paginate_by = 3

    def get_queryset(self):
        nombre = self.request.GET.get('nombre') if self.request.GET.get('nombre') else ''                
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)#.values('id', 'foto','nombre','ciudad__descripcion', 'sexo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de pacientes"
        #context['header_table'] = ('ID', 'Foto','Nombre','Ciudad', 'Sexo')        
        return context


class CrearDoctorView(CreateView):
    model = Doctor    
    template_name = "doctor_new.html"
    form_class = DoctorForm
    success_url = reverse_lazy('empleado_view')
    context_object_name = "Doctor"

    
class EditarDoctorView(UpdateView):
    model = Doctor
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "doctor_new.html"
    form_class = DoctorForm
    success_url = reverse_lazy('empleado_view')
    context_object_name = "Doctor"


class EliminarDoctorView(DeleteView):    
    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        doctor = Doctor.objects.get(id=pk)
        doctor.delete()
        # object.estado = False
        # object.save()
        return redirect('empleado_view')