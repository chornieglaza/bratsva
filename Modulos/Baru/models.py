from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Area(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (Duracion: {1} año(s))"
        return txt.format(self.nombre, self.duracion)

class Estudiante(models.Model):
    dni = models.CharField(max_length=12,primary_key=True)
    apellidoPaterno = models.CharField(max_length=15)
    apellidoMaterno = models.CharField(max_length=15)
    nombres = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    sexos =[
        ('F','Femenino'),
        ('M','Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    area = models.ForeignKey(Area, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt = "{0}, {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
    def __str__(self):
        txt = "{0} / area: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"
        return txt.format(self.nombreCompleto(), self.area, estadoEstudiante)

class Seminarios(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveIntegerField()
    instructor = models.CharField(max_length=30)

    def __str__(self):
        txt = "{0} ({1}) / instructor: {2}"
        return txt.format(self.nombre, self.codigo, self.instructor)
        
class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=CASCADE)
    seminario = models.ForeignKey(Seminarios, null=False, blank=False, on_delete=CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el seminario {2} / fecha: {3}"
        if self.estudiante.sexo ==("F"):
            letraSexo = "a"
        else:
            letraSexo = "o"
        FecMat = self.fechaMatricula.strftime("%A %d/%m/%Y  %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(), letraSexo, self.seminario, FecMat)


