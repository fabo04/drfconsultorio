from django.contrib import admin
from .models import Paciente,Profesional,Recepcionista,Informe,HistoriaClinica,Turno

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Recepcionista)
admin.site.register(Informe)
admin.site.register(HistoriaClinica)
admin.site.register(Turno)