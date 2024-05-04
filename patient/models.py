from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Modelos de usuarios
class Usuario(AbstractBaseUser, BaseUserManager):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255, unique=True)
    contrasena = models.CharField(max_length=255)
    perfil = models.CharField(max_length=255, choices=(('administrador', 'Administrador'), ('recepcionista', 'Recepcionista'), ('profesional', 'Profesional'), ('paciente', 'Paciente')))

    REQUIRED_FIELDS = ['nombre_usuario', 'contrasena', 'perfil']
    USERNAME_FIELD = 'nombre_usuario'

    objects = BaseUserManager()

    def create_user(self, nombre_usuario, contrasena, perfil, **extra_fields):
        # Crea un usuario con las credenciales proporcionadas
        user = self.model(nombre_usuario=nombre_usuario, contrasena=contrasena, perfil=perfil, **extra_fields)
        user.set_password(contrasena)
        self.save(user, commit=True)
        return user

    def create_superuser(self, nombre_usuario, contrasena, perfil, **extra_fields):
        # Crea un superusuario con las credenciales proporcionadas
        user = self.create_user(nombre_usuario, contrasena, perfil, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(commit=True)
        return user

    def __str__(self):
        return self.nombre_usuario

# Modelos de pacientes
class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    documento_identidad = models.CharField(max_length=20, unique=True)
    genero = models.CharField(max_length=10, choices=(('Masculino', 'Masculino'), ('Femenino', 'Femenino')))
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    obra_social = models.CharField(max_length=255)
    alergias = models.TextField(blank=True)
    enfermedades_cronicas = models.TextField(blank=True)
    medicamentos_que_toma = models.TextField(blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# Modelos de profesionales
class Profesional(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(max_length=20, unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# Modelos de recepcionistas
class Recepcionista(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# Modelos de informes
class Informe(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_informe = models.CharField(max_length=255)
    diagnostico = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)

# Modelos de historia clínica
class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, unique=True)
    informe = models.ManyToManyField(Informe)

# Modelos de turnos
class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=255, choices=(('Pendiente', 'Pendiente'), ('Confirmado', 'Confirmado'), ('Cancelado', 'Cancelado'), ('Atendido', 'Atendido')))
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente.nombre} {self.paciente.apellido} - {self.fecha} {self.hora}"
