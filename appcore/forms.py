from django import forms
from django.db.models import fields
from .models import Paciente, Doctor, Agenda, SignosVitales


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente

        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control text-primary',
                    'placeholder': 'Cedula'

                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Sexo'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estadi Civil'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Profesion'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Titulo'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            ),
            'sangre': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hijos': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"

        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero de cedula'
                }
            ),

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus nombres'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su direccion domiciliaria'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero de telefono'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'youremail@example.com'
                }
            ),

            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            ),

            'consultoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de consultorio'

                }
            ),
            'lugar': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion del consultorio'
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            ),
            'horario': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Registro Medico'
                }
            ),
            'duracion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Duracion de consultas'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            )
        }


class CitaForm(forms.ModelForm):
    class Meta:
        model = Agenda

        fields = '__all__'
        widgets = {

            'paciente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'doctor': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'hora': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class SignosForm(forms.ModelForm):
    class Meta:
        model = SignosVitales

        fields = '__all__'
        widgets = {

            'paciente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estatura': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'peso': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                }
            ),
            'masa': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'temperatura': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'frecRespira': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'frecCard': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'porGraCor': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'porMasaMus': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'precionArt': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
