# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from analisis.configuracion.models  import *
from comunicacion.lugar.models import *

# Create your models here.

class Entrevista(models.Model):
	nombre = models.CharField(max_length=200)
	posicion = models.CharField(max_length=200)
	email = models.EmailField()
	organizacion = models.ForeignKey(Organizacion)
	departamento = models.ForeignKey(Departamento)
	telefono = models.IntegerField()
	fecha = models.DateField()
	slug = models.SlugField(editable=False)

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not  self.id:
			self.slug = slugify(self.nombre)
		super(Entrevista, self).save(*args, **kwargs)


class Pregunta_1(models.Model):
	proyecto = models.CharField(max_length=250, verbose_name='Proyecto(s) e iniciativa(s)')
	estado = models.ForeignKey(Estado)
	ubicacion = models.ManyToManyField(Ubicacion)
	socio = models.ManyToManyField(Socio,verbose_name='Socios')
	tema = models.ManyToManyField(Tema,verbose_name='Temas')
	slug = models.SlugField(editable=False)
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.proyecto

	class Meta:
		verbose_name = 'pregunta 1'
		verbose_name_plural = 'pregunta 1'

PREGUNTA2_CHOICES = (
    ('numero tecnicos','Numero de Tecnicos'),
    ('numero promotores ','Numero de Promotores '),
    ('numero invetigadores','Numero de Invetigadores'),
    ('numero decisores','Numero de Decisores'),
    )

class Pregunta_2(models.Model):
	seleccion = models.CharField(max_length=50,choices=PREGUNTA2_CHOICES)
	hombre = models.IntegerField()
	mujer = models.IntegerField()
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 2'
		verbose_name_plural = 'pregunta 2'


class Pregunta_3(models.Model):
	grupo = models.ManyToManyField(Grupo,verbose_name='Grupos')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 3'
		verbose_name_plural = 'pregunta 3'

class Pregunta_4(models.Model):
	impacto = models.CharField(max_length=250, verbose_name='Impacto(s)')
	grupo_beneficiario = models.ManyToManyField(Grupo_Beneficiario,verbose_name='Grupos beneficiarios principales de este impacto')
	tema = models.ManyToManyField(Tema,verbose_name='Temas')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 4'
		verbose_name_plural = 'pregunta 4'

PRIORITIZADO_CHOICES = (
	(1,'Si'),
	(2,'No')
	)

class Pregunta_5a(models.Model):
	innovacion = models.CharField(max_length=250, verbose_name='Innovación(es)')
	ubicacion = models.ManyToManyField(Ubicacion)
	socio = models.ManyToManyField(Socio)
	tema = models.ManyToManyField(Tema)
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES)
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 5a'
		verbose_name_plural = 'pregunta 5a'

class Pregunta_5c(models.Model):
	organizacion_1 = models.ForeignKey(Organizacion,related_name='organizacion_1_5c',verbose_name='Organizacion')
	papel_1 = models.ManyToManyField(Papel,related_name='papel_1_5c',verbose_name='Papel')
	organizacion_2 = models.ForeignKey(Organizacion,related_name='organizacion_2_5c',verbose_name='Organizacion')
	papel_2 = models.ManyToManyField(Papel,related_name='papel_2_5c',verbose_name='Papel')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 5c'
		verbose_name_plural = 'pregunta 5c'

class Pregunta_5d(models.Model):
	innovacion_1 = models.CharField(max_length=200,verbose_name='Innovación 1')
	categoria_1 = models.ManyToManyField(Categoria,related_name='categorias_1',verbose_name='Categorias')
	innovacion_2 = models.CharField(max_length=200,verbose_name='Innovación 2')
	categoria_2 = models.ManyToManyField(Categoria,related_name='categorias_2',verbose_name='Categorias')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 5d'
		verbose_name_plural = 'pregunta 5d'

class Pregunta_5e(models.Model):
	fuente_1 = models.CharField(max_length=200, verbose_name='Fuente de aprendizaje de Innovación 1')
	categoria_fuente_1 = models.ManyToManyField(Categoria_Fuente, related_name='categoria_fuente_1',verbose_name='Categoria de Fuente')
	fuente_2 = models.CharField(max_length=200, verbose_name='Fuente de aprendizaje de Innovación 2')
	categoria_fuente_2 = models.ManyToManyField(Categoria_Fuente, related_name='categoria_fuente_2',verbose_name='Categoria de Fuente')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 5e'
		verbose_name_plural = 'pregunta 5e'

class Pregunta_6a(models.Model):
	innovacion = models.CharField(max_length=200, verbose_name='Innovación(es)')
	ubicacion =  models.ManyToManyField(Ubicacion)
	tema = models.ManyToManyField(Tema)
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES)
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 6a'
		verbose_name_plural = 'pregunta 6a'

class Pregunta_6c(models.Model):
	organizacion_1_6c = models.ForeignKey(Organizacion,related_name='organizacion_1_6c',verbose_name='Organizacion')
	papel_1_6c = models.ManyToManyField(Papel,related_name='papel_1_6c',verbose_name='Papel')
	organizacion_2_6c = models.ForeignKey(Organizacion,related_name='organizacion_2_6c',verbose_name='Organizacion')
	papel_2_6c = models.ManyToManyField(Papel,related_name='papel_2_6c',verbose_name='Papel')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 6c'
		verbose_name_plural = 'pregunta 6c'


class Pregunta_6d(models.Model):
	innovacion_1 = models.CharField(max_length=200,verbose_name='Innovación 1')
	categoria_1 = models.ManyToManyField(Categoria,related_name='categorias_1_6d',verbose_name='Categorias')
	innovacion_2 = models.CharField(max_length=200,verbose_name='Innovación 2')
	categoria_2 = models.ManyToManyField(Categoria,related_name='categorias_2_6d',verbose_name='Categorias')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 6d'
		verbose_name_plural = 'pregunta 6d'

class Pregunta_6e(models.Model):
	conocimiento_1 = models.CharField(max_length=200, verbose_name='Conocimiento clave faltante para Innovacion 1')
	categoria_innovacion_1 = models.ForeignKey(Categoria_Innovacion, related_name='categoria_innocavion_1',verbose_name='Categoria de Innovación')
	categoria_conocimiento_1 = models.ManyToManyField(Categoria_Conocimiento, related_name='categoria_conocimiento_1',verbose_name='Categoria de Conocimiento')
	conocimiento_2 = models.CharField(max_length=200, verbose_name='Conocimiento clave faltante para Innovacion 2')
	categoria_innocavion_2 = models.ForeignKey(Categoria_Innovacion, related_name='categoria_innocavion_2',verbose_name='Categoria de Innovación')
	categoria_conocimiento_2 = models.ManyToManyField(Categoria_Conocimiento, related_name='categoria_conocimiento_2',verbose_name='Categoria de Conocimiento')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 6e'
		verbose_name_plural = 'pregunta 6e'

class Pregunta_7a(models.Model):
	ubicacion = models.ManyToManyField(Ubicacion)
	seleccion = models.ManyToManyField(Seleccion_7a)
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 7a'
		verbose_name_plural = 'pregunta 7a'

class Pregunta_7b(models.Model):
	seleccion = models.ManyToManyField(Seleccion_7b)
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 7b'
		verbose_name_plural = 'pregunta 7b'

TERRITORIO_CHOICES = (
    ('dentro','Dentro'),
    ('afuera','Afuera'),
    )

PERIODO_CHOICES = (
    ('reciente','Reciente'),
    ('mediano','Mediano'),
    ('largo','Largo'),
    )

PROFUNDIDAD_CHOICES = (
    ('esporadica','Esporádica'),
    ('fortuita','Fortuita'),
    ('estrategica','Estratégica'),
    )

class Pregunta_8(models.Model):
	organizacion = models.ForeignKey(Organizacion,verbose_name='Organizacion')
	territorio = models.CharField(max_length=50,choices=TERRITORIO_CHOICES,verbose_name='Dentro o Afuera del Territorio')
	periodo = models.CharField(max_length=50,choices=PERIODO_CHOICES,verbose_name='Periodo de relación')
	profundidad = models.CharField(max_length=50,choices=PROFUNDIDAD_CHOICES,verbose_name='Profundidad de relación')
	tema = models.ManyToManyField(Tema_Relacion, verbose_name='Razón o temas de la relacion')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 8'
		verbose_name_plural = 'pregunta 8'


TEMA_CHOICES = (
    (1,'Mayor y sostenible, Intensificación ecológica'),
    (2,'Manejo sostenible de los recursos naturales de las fincas y cuencas'),
    (3,'Mejorar la comercialización y acceso a mercados juntos'),
    (4,'Aumento de ingreso y reduccion de pobreza'),
    (5,'Mejorada de Seguridad alimentaria y nutrición'),
    (6,'Empoderamiento de las mujeres y jóvenes'),
    (7,'Innovación local e innovación a través  de políticas e instituciones'),
    )

PRIORIDAD_CHOICES = (
	('alta','Alta'),
	('baja','Baja'),
	('media','Media'),
	)

PAPEL_CHOICES = (
	('facilitador','Facilitador'),
	('neutro','Neutro'),
	('bloqueador','Bloqueador'),
	)
AUTO_EVALUACION_CHOICES = (
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
	)

class Pregunta_9(models.Model):
	tema = models.IntegerField(choices=TEMA_CHOICES)
	prioridad = models.CharField(max_length=50,choices=PRIORIDAD_CHOICES,verbose_name='Prioridad Organizacional')
	papel = models.CharField(max_length=50,choices=PAPEL_CHOICES,verbose_name='Papel de la organización en el territorio')
	conocimiento = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text='Escala de valor: 1 (debilidad) hasta 5 (fuerte)')
	experiencia = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text='Escala de valor: 1 (debilidad) hasta 5 (fuerte)')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 9'
		verbose_name_plural = 'pregunta 9'

SOBRE_CHOICES = (
	(1,'Situación de las fincas (producción y biodivarsidad)'),
	(2,'Situación de los recursos naturales y manejo de ellos'),
	(3,'Situación de comerzialización y acceso a mercados'),
	(4,'Situación de organización de las comunidades y capacidad de aprendizaje'),
	(5,'Situación de equidad de género y generacional'),
	(6,'Situación de seguridad alimentaria y nutricional'),
	(7,'Situación de ingreso familiar y pobreza')
	)

DISPONIBILIDAD_CHOICES = (
	('informe tecnico','Informé técnico'),
	('informe ejecutivo','Informé ejecutivo'),
	('base de datos','Base de datos'),
	('sistema en linea','Sistema en línea'),
	)
class Pregunta_11(models.Model):
	sobre = models.IntegerField(choices=SOBRE_CHOICES)
	tipo_estudio = models.ForeignKey(Tipo_Estudio,verbose_name='Tipo de estudio')
	calendario = models.DateField()
	disponibilidad = models.CharField(max_length=100,choices=DISPONIBILIDAD_CHOICES)
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'pregunta 11'
		verbose_name_plural = 'pregunta 11'

