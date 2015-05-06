# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from smart_selects.db_fields import ChainedForeignKey
from comunicacion.lugar.models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class AreaAccion(models.Model):
	nombre = models.CharField(max_length=250)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Action Area')
		verbose_name_plural = _(u'Action Areas')

class SitioAccion(models.Model):
	nombre = models.CharField(max_length=250)
	area_accion = models.ForeignKey(AreaAccion)
	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Action Site')
		verbose_name_plural = _(u'Action Sites')

class Plataforma(models.Model):
	nombre = models.CharField(max_length=250)
	sitio_accion = models.ForeignKey(SitioAccion)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Platform')
		verbose_name_plural = _(u'Platforms')


class Status_Legal(models.Model):
	nombre = models.CharField(max_length=200,verbose_name='Name')

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Legal Status')
		verbose_name_plural = _(u'Legal Status')

class Sector_en(models.Model):
	nombre  = models.CharField(max_length=200,verbose_name='Name')

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Sector')
		verbose_name_plural = _(u'Sectors')


class Ubicacion(models.Model):
	ubicacion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.ubicacion

	class Meta:
		verbose_name = _(u'Location')
		verbose_name_plural = _(u'Locations')

# class Socio(models.Model):
# 	socio = models.CharField(max_length=100)

# 	def __unicode__(self):
# 		return self.socio

class Tema(models.Model):
	tema = models.CharField(_(u'Theme'),max_length=200)

	def __unicode__(self):
		return self.tema

	class Meta:
		verbose_name = _(u'Theme')
		verbose_name_plural = _(u'Themes')

class Grupo(models.Model):
	nombre = models.CharField(_(u'Group'),max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Group')
		verbose_name_plural = _(u'Groups')

class Grupo_Beneficiario(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Beneficiary Group')
		verbose_name_plural = _(u'Beneficiary Groups')

class Papel(models.Model):
	nombre = models.CharField(max_length=100,verbose_name='Name')

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Role')
		verbose_name_plural = _(u'Roles')

LIMITACIONES_CATEGORIA = (
    (1,'Productive'),
    (2,'Economic'),
    (3,'Technician'),
    (4,'Merchandising'),
    (5,'Institutional'),
    (6,'Attitude/Cultural'),
    (7,'Human Capacity'),
    (8,'Alliance / Partner'),
    (9,'Politics'),
    (10,'Others'),
    )


class Categoria(models.Model):
	nombre = models.CharField(max_length=100, verbose_name='Name')
	categoria = models.IntegerField(choices=LIMITACIONES_CATEGORIA, verbose_name='Category')

	def __unicode__(self):
		return self.nombre
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

class Categoria_Innovacion(models.Model):
	nombre = models.CharField('Name',max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Innovation Category')
		verbose_name_plural = _(u'Innovation Categories')

class Categoria_Conocimiento(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Knowledge Category')
		verbose_name_plural = _(u'Knowledge Categories')

class Categoria_Fuente(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Source Category')
		verbose_name_plural = _(u'Sources Category')

class Seleccion_7a(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Selection question 7')
		verbose_name_plural = _(u'Selections question 7')

class Seleccion_7b(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Selection question 7b')
		verbose_name_plural = _(u'Selections question 7b')


class Tipo_Estudio(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Type of study')
		verbose_name_plural = _(u'Types of studies')

class Tema_Relacion(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Type of Relationship')
		verbose_name_plural = _(u'Types of Relationship')
