from rest_framework import viewsets, permissions
from .models import Usuario, Paciente, Profesional, Recepcionista, Informe, HistoriaClinica, Turno
from .serializers import UsuarioSerializer, PacienteSerializer, ProfesionalSerializer, RecepcionistaSerializer, InformeSerializer, HistoriaClinicaSerializer, TurnoSerializer

# ViewSets para usuarios
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

# ViewSets para pacientes
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer

# ViewSets para profesionales
class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfesionalSerializer

# ViewSets para recepcionistas
class RecepcionistaViewSet(viewsets.ModelViewSet):
    queryset = Recepcionista.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RecepcionistaSerializer

# ViewSets para informes
class InformeViewSet(viewsets.ModelViewSet):
    queryset = Informe.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InformeSerializer

# ViewSets para historia clínica
class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    queryset = HistoriaClinica.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HistoriaClinicaSerializer

# ViewSets para turnos
class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TurnoSerializer
