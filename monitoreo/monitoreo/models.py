# -*- coding: utf-8 -*-

from django.db import models
from comunicacion.lugar.models import Comunidad, Departamento, Municipio
from django.conf import settings
from comunicacion.utils import get_file_path 
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

# Create your models here.
class Recolector(models.Model):
    ''' Esta es la clase para el nombre del recolector
    '''
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Recolector"

CHOICE_ZONA = ((1,'Seca'),(2,'Alta'))

class Organizaciones(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.IntegerField(null=True, blank=True)
    fax = models.IntegerField(null=True, blank=True)
    celular = models.IntegerField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    departamento = models.ForeignKey(Departamento, null=True, blank=True)
    logo = ImageField(upload_to=get_file_path, null=True, blank=True)
    sitio_web = models.URLField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    zona = models.IntegerField(choices=CHOICE_ZONA)
    fileDir = 'attachments/logos'

    def __unicode__(self):
        return self.nombre
#        return '%s - %s' % (self.departamento.nombre, self.nombre)

    class Meta:
        verbose_name_plural = "Organizaciones"

CHOICE_SEXO = ((1,'Hombre'),(2,'Mujer'))
CHOICE_OPCION = ((1,'Si'),(2,'No')) # Este choice se utilizara en toda la aplicacion que necesite si o no
CHOICE_RANGO = (
                (1, '18 - 25'),
                (2, '26 - 45'),
                (3, '26 - 65'),
                (4, 'Más de 65')
            )
CHOICE_NIVEL_EDUCATIVO = (
                (1, 'No sabe leer o escribir'),
                (2, 'Primaria Incompleta'),
                (3, 'Primaria Completa'),
                (4, 'Secundaria Incompleta'),
                (5, 'Bachiller'),
                (6, 'Universitario'),
            )

class Productor(models.Model):
    nombre = models.CharField('Nombre de entrevistado/a', max_length=200)
    cedula = models.CharField('cedula de entrevistado', max_length=200, null=True, blank=True)
    sexo = models.IntegerField(choices=CHOICE_SEXO)
    edad = models.IntegerField(choices=CHOICE_RANGO)
    finca = models.CharField('Nombre de Finca', max_length=200)
    municipio = models.ForeignKey(Municipio)
    comunidad = models.ForeignKey(Comunidad)
    organizacion = models.ManyToManyField(Organizaciones, related_name ="org")
    jefe = models.IntegerField(choices=CHOICE_OPCION)
    nivel_educacion = models.IntegerField(choices=CHOICE_NIVEL_EDUCATIVO)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productor/as"

class Encuesta(models.Model):
    ''' Esta es la parte de la encuesta donde van los demas
    '''
    fecha = models.DateField()
    recolector = models.ForeignKey(Recolector)
    productor = models.ForeignKey(Productor)
    user = models.ForeignKey(User)
    
    #campos ocultos para querys
    year = models.IntegerField(editable=False)
    
    def save(self):
        self.year = self.fecha.year
        super(Encuesta, self).save()
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Encuesta"

## Indicador 1: Familia

CHOICE_EDUCACION = ((1,'Hombre mas de 18 años'),(2,'Mujeres mas de 18 años'),(3,'Hombre de 7 a 18 años'),
                     (4,'Mujeres de 7 a 18 años'),(5,'Niños menos de 6 años'),(6,'Niñas menos de 6 años'))

CHOICE_DESDE = ((1,'Menos de 5 años'),(2,'Más de 5 años'),(3,'No utilizar'))

##-------------------------------------------------------------------------------

# Indicador 3 y 4. Tipo de tenencia de parcela y solar y Documento legal de la propiedad, a nombre de quién

CHOICE_TENENCIA = ((1,"Propia con escritura pública"),(2,"Propia por herencia"),
                   (3,"Propias con promesa de venta"),(4,"Propias con titulo de reforma agraria"),
                   (5,"Arrendada"),(6,"Sin documento"),(7,"Escritura posesoria"),(8,"No tiene"))
                   
                   
CHOICE_DUENO = ((1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),
                (5,"Colectivo"),(6,"No hay"))

class Tenencia(models.Model):
    ''' Modelo tipo de tenencia de la propiedad
    '''
    parcela = models.IntegerField('Parcela (tierra)', choices=CHOICE_TENENCIA)
    solar = models.IntegerField('Solar (dónde está la vivienda)', choices=CHOICE_TENENCIA)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_parcela_display()

class TenenciaEntrevistada(models.Model):
    ''' Modelo tipo de tenencia de la propiedad
    '''
    parcela = models.IntegerField('Parcela (tierra)', choices=CHOICE_TENENCIA)
    solar = models.IntegerField('Solar (dónde está la vivienda)', choices=CHOICE_TENENCIA)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_parcela_display()

#-----------------------------------------------------------
CHOICE_CASA_SOLAR = (
                    (1,"Propios (con o sin documento)"),
                    (2,"De su esposo/a"),
                    (3,"De su padres o suegros"),
                    (4,"Compartidos con los padres o suegros"),
                    (5,"Compartidos con familiares"),
                    (6,"Compartidos con otra familia"),
                    (7,"Alquilados"),
                )
CHOICE_TENENCIA_SOLAR = (
                    (1,"Escritura pública"),
                    (2,"Promesa de venta"),
                    (3,"Testamento o Herencia"),
                    (4,"Título de reforma Agraria"),
                    (5,"Escritura posesoria"),
                    (6,"Sin documento"),
                )
CHOICE_DUENO_CASA_SOLAR = ((1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"))

class CasaSolar(models.Model):
    casa = models.IntegerField('La casa y el solar son', choices=CHOICE_CASA_SOLAR)
    tenencia = models.IntegerField('Tenencia de solar', choices=CHOICE_TENENCIA_SOLAR)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO_CASA_SOLAR)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Casa y solar"
    
#-------------------------------------------------------------------------------


CHOICE_MANEJA = ((1,"Hombre"),(2,"Mujer"),(3,"Ambos"),(4,"Hijos/as"),
                 (5,'Hombre-Hijos'),(6,'Mujer-Hijos'),(7,'Todos'))

#-------------------------------------------------------------------------------
