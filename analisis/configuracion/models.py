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
		verbose_name = _(u'Area de Acción')
		verbose_name_plural = _(u'Areas de Acción')

class SitioAccion(models.Model):
	nombre = models.CharField(max_length=250)
	area_accion = models.ForeignKey(AreaAccion)
	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Sitio de Acción')
		verbose_name_plural = _(u'Sitios de Acción')

class Plataforma(models.Model):
	nombre = models.CharField(max_length=250)
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
		verbose_name = _(u'Status Legal')
		verbose_name_plural = _(u'Status Legal')

class Sector(models.Model):
	nombre  = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Sector')
		verbose_name_plural = _(u'Sectores')

		
# class Organizacion(models.Model):
# 	nombre = models.CharField(max_length=200)
# 	status_legal = models.ForeignKey(Status_Legal)
# 	anno_fundacion = models.DateField(verbose_name='Año de fundación')
# 	dueno = models.CharField(verbose_name='Dueño, Presidente, Director',max_length=200)
# 	numero_activistas = models.IntegerField(verbose_name='Numero de activistas o miembros')
# 	direccion = models.CharField(max_length=200)
# 	departamento = models.ForeignKey(Departamento)
# 	municipio = ChainedForeignKey(
# 								Municipio,
# 	 							chained_field="departamento", 
# 	 					 		chained_model_field="departamento",
# 	 					 		show_all=False, auto_choose=True)
# 	telefono = models.IntegerField()
# 	fax = models.IntegerField()
# 	email = models.EmailField()
# 	sector = models.ForeignKey(Sector)
# 	slug = models.SlugField(editable=False)

# 	def __unicode__(self):
# 		return self.nombre

# 	def save(self, *args, **kwargs):
# 		if not  self.id:
# 			self.slug = slugify(self.nombre)
# 		super(Organizacion, self).save(*args, **kwargs)

# 	class Meta:
# 		verbose_name = 'Organización'
# 		verbose_name_plural = 'Organizaciones'


class Ubicacion(models.Model):
	ubicacion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.ubicacion

	class Meta:
		verbose_name = _(u'Ubicación')
		verbose_name_plural = _(u'Ubicaciones')

class Socio(models.Model):
	socio = models.CharField(max_length=100)

	def __unicode__(self):
		return self.socio

class Tema(models.Model):
	tema = models.CharField(_(u'Tema'),max_length=200)

	def __unicode__(self):
		return self.tema

class Grupo(models.Model):
	nombre = models.CharField(_(u'Grupo'),max_length=100)

	def __unicode__(self):
		return self.nombre

class Grupo_Beneficiario(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Grupo Beneficiario')
		verbose_name_plural = _(u'Grupos Beneficiarios')

class Papel(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Papel')
		verbose_name_plural = _(u'Papeles')

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
	nombre = models.CharField(_(u'Nombre'),max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Categoria de Innovación')
		verbose_name_plural = _(u'Categorias de Innovación')

class Categoria_Conocimiento(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Categoria de Conocimiento')
		verbose_name_plural = _(u'Categorias de Conocimiento')

class Categoria_Fuente(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Categoria de Fuente')
		verbose_name_plural = _(u'Categorias de Fuente')

class Seleccion_7a(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Selección pregunta 7a')
		verbose_name_plural = _(u'Selecciones pregunta 7a')

class Seleccion_7b(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Selección pregunta 7b')
		verbose_name_plural = _(u'Selecciones pregunta 7b')


class Tipo_Estudio(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Tipo de estudio')
		verbose_name_plural = _(u'Tipos de estudios')

class Tema_Relacion(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = _(u'Tipo de Relación')
		verbose_name_plural = _(u'Tipos de Relación')
