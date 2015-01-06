# -*- coding: UTF-8 -*-

from django.db import models
from comunicacion.utils import *
from ckeditor.fields import RichTextField
from comunicacion.contrapartes.models import Pais
from sorl.thumbnail import ImageField

# Create your models here.
# 
class Aliados(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField("Siglas o nombre corto",help_text="Siglas o nombre corto de la oganización",max_length=200,blank=True, null=True)
    logo = ImageField(upload_to=get_file_path,
                      null=True, blank=True)
    fileDir = 'aliados/logos/'
    pais = models.ForeignKey(Pais)
    fundacion = models.CharField('Año de fundación', max_length=200, 
                                 blank=True, null=True)
    temas = RichTextField(blank=True, null=True)
    generalidades = RichTextField(blank=True, null=True)
    contacto = models.CharField(max_length=200,blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    rss = models.CharField(max_length=200,blank=True, null=True)

    class Meta:
        verbose_name_plural = "Aliados"
        unique_together = ("nombre",)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return '/aliados/%d/' % (self.id,)
