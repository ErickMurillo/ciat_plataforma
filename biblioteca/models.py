# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from comunicacion.utils import *
from mapeo.models import Proyectos
from analisis.configuracion.models import Plataforma
from mapeo.models import Temas

# Create your models here.
CHOICE_TIPO = (
                (1, 'Libros'),
                (2, 'Capítulo de libro'),
                (3, 'Manual, Guía'),
                (4, 'Revista popular'),
                (5, 'Propuesta'),
                (6, 'Método'),
                (7, 'Memoria'),
                (8, 'Base de dato'),
                (9, 'Radio'),
                (10, 'Video'),
                (11, 'Afiche'),
                (12, 'Presentación'),
                (13, 'Artículo en revista'),
    )

class Biblioteca(models.Model):
    tipo = models.IntegerField(choices=CHOICE_TIPO, verbose_name="Tipo de documento", null=True, blank=True)
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    autor = models.CharField('Autores',max_length=250)
    anio = models.CharField('Año', max_length=50, null=True, blank=True)
    descripcion = RichTextField('Descripción')
    cita = models.CharField('Cita bibliográfica', max_length=50, null=True, blank=True)
    fecha = models.DateField(auto_now=True)
    edicion = models.CharField('Editorial o revista', max_length=50, null=True, blank=True)
    portada = ImageField(upload_to=get_file_path, null=True, blank=True)
    url_video = models.URLField(null=True, blank=True)
    palabras_claves = models.CharField(max_length=250, null=True, blank=True)
    proyecto = models.ManyToManyField(Proyectos, blank=True)
    alianza = models.ManyToManyField(Plataforma, blank=True)
    temas = models.ManyToManyField(Temas, blank=True)

    user = models.ForeignKey(User)

    fileDir = 'BibliotecaPortadas/'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.titulo)
        return super(Biblioteca, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Biblioteca'
        verbose_name_plural = 'Bibliotecas'

class ArchivoAdjunto(models.Model):
    biblioteca = models.ForeignKey(Biblioteca)
    archivo = models.FileField(upload_to=get_file_path)

    fileDir = 'BibliotecaArchivos/'

    def extension(self):
        name, extension = os.path.splitext(self.archivo.name)
        return extension

    class Meta:
        verbose_name = 'Archivo adjunto'
        verbose_name_plural = 'Archivos adjuntos'
