from django.contrib import admin

from appcore.models import (Titulo, Profesion, Provincia, Paciente, Ciudad, Sangre, Doctor, Horario, Agenda, SignosVitales)


admin.site.register(Titulo)
admin.site.register(Profesion)
admin.site.register(Provincia)
admin.site.register(Paciente)
admin.site.register(Ciudad)
admin.site.register(Sangre)
admin.site.register(Doctor)
admin.site.register(Horario)
admin.site.register(Agenda)
admin.site.register(SignosVitales)
