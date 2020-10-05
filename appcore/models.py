from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class Provincia(models.Model):
    descripcion = models.CharField(verbose_name='Descripcion', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Ciudad(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Profesion(models.Model):
    descripcion = models.CharField(
        verbose_name='Descripcion', max_length=100, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Profesion'
        verbose_name_plural = 'Profesiones'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Titulo(models.Model):
    descripcion = models.CharField(
        verbose_name='Descripcion', max_length=100, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Titulo'
        verbose_name_plural = 'Titulos'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Persona(models.Model):
    tipo_sexo = (('N', 'Ninguno'), ('M', 'Masculino'), ('F', 'Femenino'))
    estado_civil = (('S', 'Soltero'), ('C', 'Casado'),
                    ('D', 'Divorciado'), ('V', 'Viudo'), ('U', 'Union'))
    cedula = models.CharField('Cedula', max_length=13, unique=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombres')
    apellido = models.CharField(max_length=100, verbose_name='Apellidos')
    nacimiento = models.DateField('Fecha Nacimiento', blank=True, null=True)
    sexo = models.CharField('sexo', choices=tipo_sexo,
                            default='N', max_length=1)
    civil = models.CharField(
        'Estado civil', choices=estado_civil, default='S', max_length=1)
    profesion = models.ManyToManyField(Profesion)
    titulo = models.ManyToManyField(Titulo)
    provincia = models.ForeignKey(
        Provincia, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey(
        Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    direccion = models.CharField(
        'Direccion', max_length=100, blank=True, null=True)
    telefono = models.CharField(
        'Telefono', max_length=100, blank=True, null=True)
    email = models.EmailField('Correo', max_length=100, blank=True, null=True)
    foto = models.ImageField('Foto', upload_to='fotos/', blank=True, null=True)

    class Meta:
        abstract = True

    def get_foto(self):
        try:
            return str(self.foto.url)
        except:
            pass
        return None

class Sangre(models.Model):
    tipo = models.CharField('Tipo de Sangre', max_length=20, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tipo de Sangre'
        verbose_name_plural = 'Tipos de Sangre'

    def __str__(self):
        return '{}'.format(self.tipo)


class Paciente(Persona):
    sangre = models.ForeignKey(
        Sangre, on_delete=models.PROTECT, blank=True, null=True)
    hijos = models.IntegerField('No.hijos', default=0)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return '{}'.format(self.nombre)


class Horario(models.Model): 
    d_semana={(0,'Domingo'), (1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4,'Jueves'), (5, 'Viernes'), (6, 'Sabado'), (7, 'Domingo')}   
    dia=models.IntegerField('Dia', choices=d_semana, default=1)
    desde=models.TimeField('Desde', blank=True, null=True)
    hasta=models.TimeField('Hasta', blank=True, null=True)    
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name='Dia'
        verbose_name_plural='Dias'

    def __str__(self):
        return '{}'.format(self.dia)

class Doctor(Persona):
    consultoria=models.CharField(max_length=200)
    lugar=models.CharField(verbose_name='Direccion de Consultorio', max_length=100)
    logo=models.ImageField(verbose_name='Logo', upload_to='Logos/', blank=True, null=True)
    horario=models.ManyToManyField(Horario)
    registro=models.CharField(verbose_name='Registro Medico', max_length=50)
    duracion=models.IntegerField(verbose_name='Duracion de Consulta', default=30)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name='Doctor'
        verbose_name_plural='Doctores'

    def __str__(self):
            return '{}'.format(self.nombre)


class Agenda(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    fecha = models.DateField(
        'Fecha de Agenda', blank=True, null=True, default=date.today())
    hora = models.TimeField('Hora', default=datetime.now().time())
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return '{}'.format(self.fecha)



#---------------------------------------------------------------------Sintomas
class Sintoma(models.Model):
    descripcion = models.CharField('Sintoma', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Sintoma'
        verbose_name_plural = 'Sintomas'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Diagnostico(models.Model):
    codigo = models.CharField('Codigo', max_length=100)
    descripcion = models.CharField('Diagnostico', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'

    def __str__(self):
        return '{}'.format(self.descripcion)
