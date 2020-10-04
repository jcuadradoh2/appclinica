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
    
#--------------------------------------------------------------------------------------Sintomas

# class CrearSintomaView(CreateView):
#     model = Sintoma   
#     template_name = "diagnostico.html"
#     form_class = DoctorForm
#     success_url = reverse_lazy('menu')
#     context_object_name = "Sintomas"