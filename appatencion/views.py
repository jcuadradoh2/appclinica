from django.shortcuts import render
from django.views.generic.base import TemplateView


class menuView(TemplateView):
    template_name = "opciones.html"


class opcionesView(TemplateView):
    template_name = "opciones.html"
