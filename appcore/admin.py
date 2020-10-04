from django.contrib import admin

from appcore.models import (Titulo, Profesion, Provincia, Paciente, Ciudad, Sangre)


admin.site.register(Titulo)
admin.site.register(Profesion)
admin.site.register(Provincia)
admin.site.register(Paciente)
admin.site.register(Ciudad)
admin.site.register(Sangre)