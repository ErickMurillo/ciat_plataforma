# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from comunicacion.lugar.models import Comunidad, Departamento, Municipio, Pais
from comunicacion.utils import get_file_path
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField

# Create your models here.
from comunicacion.contrapartes.widgets import ColorPickerWidget

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)


CHOICE_LISTA = (
        (1, "NICANORTE"),
        (2, "TRIFINIO"),
        (3, "HAITI/DOMINICANA")
    )

class Organizaciones(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField("Siglas o nombre corto",
                                help_text="Siglas o nombre corto de la oganización",
                                max_length=200, blank=True, null=True)
    pertenece = models.IntegerField(choices=CHOICE_LISTA)
    telefono = models.IntegerField(null=True, blank=True)
    fax = models.CharField(max_length=50, null=True, blank=True)
    logo = ImageField(upload_to=get_file_path, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    pais = models.ForeignKey(Pais)
    departamento = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    fundacion = models.CharField('Año de fundación', 
                                 max_length=200, 
                                 blank=True, null=True)
    temas = RichTextField(blank=True, null=True)
    generalidades = RichTextField(blank=True, null=True)
    contacto = models.CharField(max_length=200, blank=True, null=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    rss = models.CharField(max_length=200, blank=True, null=True)
    font_color = ColorField(blank=True, unique=True)

    fileDir = 'organizaciones/logos/'

    class Meta:
        verbose_name_plural = "Organizaciones"
        unique_together = ("font_color", "nombre")
        ordering = ['nombre',]

    def __unicode__(self):
        return self.nombre

CHOICE_SEXO = ((1,'Hombre'),(2,'Mujer'))
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

class Persona(models.Model):
    nombre = models.CharField('Nombre de entrevistado/a', max_length=200)
    cedula = models.CharField('cedula de entrevistado', max_length=200, null=True, blank=True)
    sexo = models.IntegerField(choices=CHOICE_SEXO)
    edad = models.IntegerField(choices=CHOICE_RANGO)
    finca = models.CharField('Nombre de Finca', max_length=200, null=True, blank=True)
    pais = models.ForeignKey(Pais)
    departamento = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    comunidad = models.ForeignKey(Comunidad)
    organizacion = models.ManyToManyField(Organizaciones, related_name ="org", 
                                        verbose_name='Organizaciones que lo apoyan')
    nivel_educacion = models.IntegerField(choices=CHOICE_NIVEL_EDUCATIVO)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural= 'Personas registradas'