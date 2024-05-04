# Generated by Django 5.0.4 on 2024-05-04 18:48

import django.contrib.auth.base_user
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('documento_identidad', models.CharField(max_length=20, unique=True)),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('obra_social', models.CharField(max_length=255)),
                ('alergias', models.TextField(blank=True)),
                ('enfermedades_cronicas', models.TextField(blank=True)),
                ('medicamentos_que_toma', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('matricula', models.CharField(max_length=20, unique=True)),
                ('especialidad', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=255, unique=True)),
                ('contrasena', models.CharField(max_length=255)),
                ('perfil', models.CharField(choices=[('administrador', 'Administrador'), ('recepcionista', 'Recepcionista'), ('profesional', 'Profesional'), ('paciente', 'Paciente')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, django.contrib.auth.base_user.BaseUserManager),
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('tipo_informe', models.CharField(max_length=255)),
                ('diagnostico', models.TextField(blank=True)),
                ('tratamiento', models.TextField(blank=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.paciente')),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.profesional')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informe', models.ManyToManyField(to='patient.informe')),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Confirmado', 'Confirmado'), ('Cancelado', 'Cancelado'), ('Atendido', 'Atendido')], max_length=255)),
                ('notas', models.TextField(blank=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.paciente')),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.profesional')),
            ],
        ),
        migrations.CreateModel(
            name='Recepcionista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='profesional',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.usuario'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.usuario'),
        ),
    ]
