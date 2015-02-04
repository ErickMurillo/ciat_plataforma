# -*- coding: UTF-8 -*-

from django.db import models
from comunicacion.foros.models import Documentos
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from south.modelsinspector import add_introspection_rules
from ckeditor.fields import RichTextField
from analisis.configuracion.models import SitioAccion

add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

# Create your models here.

class Agendas(models.Model):
    evento = models.CharField(max_length=200)
    descripcion = RichTextField()
    contacto = models.CharField('Persona de contacto', max_length=250)
    lugar = models.CharField('Lugar del evento', max_length=250)
    correo = models.EmailField('correo para contactar')
    inicio = models.DateField('Fecha de Inicio')
    final = models.DateField('Fecha de Finalización')
    publico = models.BooleanField()
    sitio_accion = models.ForeignKey(SitioAccion)
    adjunto = generic.GenericRelation(Documentos)
    
    user = models.ForeignKey(User)

    class Meta:
    	verbose_name_plural = "Agendas"

    def __unicode__(self):
    	return u'%s' % self.evento

    def get_absolute_url(self):
        return '/agendas/%d/' % (self.id,)


