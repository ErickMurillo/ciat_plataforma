# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from analisis.configuracion.models  import *
from comunicacion.lugar.models import *

# Create your models here.

ALCANCE_CHOICES = (
    ('nacinal','Nacional'),
    ('territorial','Territorial'),
    )

class Entrevista(models.Model):
	nombre = models.CharField(max_length=200)
	posicion = models.CharField(max_length=200)
	email = models.EmailField()
	organizacion = models.ForeignKey(Organizacion)
	departamento = models.ForeignKey(Departamento)
	telefono = models.IntegerField()
	fecha = models.DateField()
	slug = models.SlugField(editable=False)
	alcance = models.CharField(max_length=50,choices=ALCANCE_CHOICES)
	tipo_estudio = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not  self.id:
			self.slug = slugify(self.nombre)
		super(Entrevista, self).save(*args, **kwargs)

ESTADO_CHOICES = (
	('Activo','Activo'),
	('Finalizado','Finalizado')
	)

class Pregunta_1(models.Model):
	proyecto = models.CharField(max_length=250, verbose_name='Proyecto(s) e iniciativa(s)')
	estado = models.CharField(max_length=50,choices=ESTADO_CHOICES)
	ubicacion = models.ManyToManyField(Ubicacion)
	socio = models.ManyToManyField(Socio,verbose_name='Socios')
	tema = models.ManyToManyField(Tema,verbose_name='Temas')
	slug = models.SlugField(editable=False)
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.proyecto

	class Meta:
		verbose_name = 'Proyectos e iniciativas'
		verbose_name_plural = 'Proyectos e iniciativas que ha llegado su organización en los ultimos 5 años'

PREGUNTA2_CHOICES = (
    ('tecnicos','Tecnicos'),
    ('promotores ','Promotores '),
    ('invetigadores','Invetigadores'),
    ('decisores','Decisores'),
    )

class Pregunta_2(models.Model):
	seleccion = models.CharField(max_length=50,choices=PREGUNTA2_CHOICES,verbose_name='Cargos')
	hombre = models.IntegerField(verbose_name='Número de Hombre(s)')
	mujer = models.IntegerField(verbose_name='Número de 	Mujer(es)')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Recursos humanos'
		verbose_name_plural = 'Recursos humanos que tiene su organización'


class Pregunta_3(models.Model):
	grupo = models.ManyToManyField(Grupo,verbose_name='Grupos')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'A que grupos beneficia su organización'
		verbose_name_plural = 'A que grupos beneficia su organización'

class Pregunta_4(models.Model):
	impacto = models.CharField(max_length=250, verbose_name='Impacto(s)')
	grupo_beneficiario = models.ManyToManyField(Grupo,verbose_name='Grupos beneficiarios principales de este impacto')
	tema = models.ManyToManyField(Tema,verbose_name='Temas')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Impactos Organizacionales'
		verbose_name_plural = 'Tipos de impactos organizacionales que ha hecho su organización en los ultimos 5 años'

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
		verbose_name = 'Innovación productiva u organizacional'
		verbose_name_plural = 'Ha participado su organización en alguna innovación productiva u organizacional en la región'

class Pregunta_5c(models.Model):
	organizacion_1 = models.ForeignKey(Organizacion,verbose_name='Organizacion')
	papel_1 = models.ManyToManyField(Papel,verbose_name='Papel')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Papel que juega su organización'
		verbose_name_plural = 'Papel que juega su organización y otros socios en relación a cada innovacion'

class Pregunta_5d(models.Model):
	innovacion_1 = models.CharField(max_length=200,verbose_name='Innovación')
	categoria_1 = models.ManyToManyField(Categoria,verbose_name='Categorias')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Limitaciones'
		verbose_name_plural = 'Principales limitaciones que afectaron el éxito de estas innovaciones'

class Pregunta_5e(models.Model):
	fuente_1 = models.CharField(max_length=200, verbose_name='Fuente de aprendizaje de Innovación')
	categoria_fuente_1 = models.ManyToManyField(Categoria_Fuente,verbose_name='Categoria de Fuente')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Fuentes de aprendizaje'
		verbose_name_plural = 'Fuentes mas importantes de aprendizaje y consulta dentro y fuera de la región'

class Pregunta_6a(models.Model):
	innovacion = models.CharField(max_length=200, verbose_name='Innovación(es)')
	ubicacion =  models.ManyToManyField(Ubicacion)
	tema = models.ManyToManyField(Tema)
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES)
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Innovaciones'
		verbose_name_plural = 'Innovaciones en las que le gustaria trabajar a su organización en los proximas 5-10 años'

class Pregunta_6c(models.Model):
	organizacion_1_6c = models.ForeignKey(Organizacion,verbose_name='Organizacion')
	papel_1_6c = models.ManyToManyField(Papel,verbose_name='Papel')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Socios o colaboradores'
		verbose_name_plural = 'Socios o colaboradores claves para llevar a cabo las innovaciones'


class Pregunta_6d(models.Model):
	innovacion_1 = models.CharField(max_length=200,verbose_name='Innovación')
	categoria_1 = models.ManyToManyField(Categoria,verbose_name='Categorias')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Posibles limitaciones'
		verbose_name_plural = 'Posibles limitaciones para llevar a cabo estos cambios en la región'

class Pregunta_6e(models.Model):
	conocimiento_1 = models.CharField(max_length=200, verbose_name='Conocimiento clave faltante para Innovacion')
	categoria_innovacion_1 = models.ForeignKey(Categoria_Innovacion,verbose_name='Categoria de Innovación')
	categoria_conocimiento_1 = models.ManyToManyField(Categoria_Conocimiento,verbose_name='Categoria de Conocimiento')
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Informacion necesaria o calve para la realización de las innovaciones'
		verbose_name_plural = 'Informacion necesaria o calve para la realización de las innovaciones'

class Pregunta_7a(models.Model):
	ubicacion = models.ManyToManyField(Ubicacion)
	seleccion = models.ManyToManyField(Seleccion_7a)
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Sitios de campo'
		verbose_name_plural = 'Sitios de campo donde Humidtropics debería desarrollar actividades con socios locales'

class Pregunta_7b(models.Model):
	seleccion = models.ManyToManyField(Seleccion_7b)
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Papel que podría jugar su organización en los sitios de campo seleccionados/Humidtropics'
		verbose_name_plural = 'Papel que podría jugar su organización en los sitios de campo seleccionados/Humidtropics'

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
		verbose_name = 'Relación con las organizaciones'
		verbose_name_plural = 'Relaciones con las organizaciones que radican en los territorios'


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
		verbose_name = 'Análisis de capacidad de las organizaciones'
		verbose_name_plural = 'Análisis de capacidad de las organizaciones'

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
	calendario = models.IntegerField(verbose_name='Año')
	disponibilidad = models.CharField(max_length=100,choices=DISPONIBILIDAD_CHOICES)
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = 'Datos que tiene la organización para análisis de datos secundarios'
		verbose_name_plural = 'Datos que tiene la organización para análisis de datos secundarios'

