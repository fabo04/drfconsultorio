from rest_framework import serializers
from .models import Paciente, Profesional, Recepcionista, Usuario, Informe, HistoriaClinica, Turno

from rest_framework import serializers
from .models import Paciente, Profesional, Recepcionista, Usuario, Informe, HistoriaClinica, Turno

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(required=False)

    class Meta:
        model = Paciente
        fields = '__all__'

class ProfesionalSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(required=False)

    class Meta:
        model = Profesional
        fields = '__all__'

class RecepcionistaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(required=False)

    class Meta:
        model = Recepcionista
        fields = '__all__'

class InformeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Informe
        fields = '__all__'

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    informes = InformeSerializer(many=True, required=False)

    class Meta:
        model = HistoriaClinica
        fields = '__all__'

class TurnoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(required=False)
    profesional = ProfesionalSerializer(required=False)
    
    class Meta:
        model = Turno
        fields = '__all__'
