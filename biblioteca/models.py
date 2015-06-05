# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from comunicacion.utils import *

# Create your models here.

class Biblioteca(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    autor = models.CharField(max_length=250)
    descripcion = RichTextField('Descripción')
    fecha = models.DateField(auto_now=True)
    edicion = models.CharField('Edición', max_length=50, null=True, blank=True)
    portada = ImageField(upload_to=get_file_path, null=True, blank=True)
    url_video = models.URLField(null=True, blank=True)
    palabras_claves = models.CharField(max_length=250, null=True, blank=True)

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

    class Meta:
        verbose_name = 'Archivo adjunto'
        verbose_name_plural = 'Archivos adjuntos'