# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from smart_selects.db_fields import ChainedForeignKey
from comunicacion.lugar.models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class AreaAccion(models.Model):
	nombre = models.CharField(_(u'Nombre'), max_length=250)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Area de Acción')
		verbose_name_plural = _(u'Areas de Acción')

class SitioAccion(models.Model):
	nombre = models.CharField(_(u'Nombre'), max_length=250)
	area_accion = models.ForeignKey(AreaAccion)
	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Sitio de Acción')
		verbose_name_plural = _(u'Sitios de Acción')

class Plataforma(models.Model):
	nombre = models.CharField(_(u'Nombre'), max_length=250)
	sitio_accion = models.ForeignKey(SitioAccion)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Plataforma')
		verbose_name_plural = _(u'Plataformas')


class Status_Legal(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Status Legal')
		verbose_name_plural = (u'Status Legal')

class Sector(models.Model):
	nombre  = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Sector')
		verbose_name_plural = (u'Sectores')


class Ubicacion(models.Model):
	ubicacion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.ubicacion

	class Meta:
		verbose_name = (u'Ubicación')
		verbose_name_plural = (u'Ubicaciones')

class Socio(models.Model):
	socio = models.CharField(max_length=100)

	def __unicode__(self):
		return self.socio

class Tema(models.Model):
	tema = models.CharField((u'Tema'),max_length=200)

	def __unicode__(self):
		return self.tema

class Grupo(models.Model):
	nombre = models.CharField((u'Grupo'),max_length=100)

	def __unicode__(self):
		return self.nombre

class Grupo_Beneficiario(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Grupo Beneficiario')
		verbose_name_plural = (u'Grupos Beneficiarios')

class Papel(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Papel')
		verbose_name_plural = (u'Papeles')

LIMITACIONES_CATEGORIA = (
    (1,'Productivo'),
    (2,'Económico'),
    (3,'Técnico'),
    (4,'Comercialización'),
    (5,'Institucional'),
    (6,'Actitud/Cultural'),
    (7,'Capacidad Humana'),
    (8,'Alianza/Socios'),
    (9,'Política'),
    (10,'Otros'),
    )

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	categoria = models.IntegerField(choices=LIMITACIONES_CATEGORIA)

	def __unicode__(self):
		return self.nombre

class Categoria_Innovacion(models.Model):
	nombre = models.CharField((u'Nombre'),max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Categoria de Innovación')
		verbose_name_plural = (u'Categorias de Innovación')

class Categoria_Conocimiento(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Categoria de Conocimiento')
		verbose_name_plural = (u'Categorias de Conocimiento')

class Categoria_Fuente(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Categoria de Fuente')
		verbose_name_plural = (u'Categorias de Fuente')

class Seleccion_7a(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Selección pregunta 7a')
		verbose_name_plural = (u'Selecciones pregunta 7a')

class Seleccion_7b(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Selección pregunta 7b')
		verbose_name_plural = (u'Selecciones pregunta 7b')


class Tipo_Estudio(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Tipo de estudio')
		verbose_name_plural = (u'Tipos de estudios')

class Tema_Relacion(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = (u'Tipo de Relación')
		verbose_name_plural = (u'Tipos de Relación')
