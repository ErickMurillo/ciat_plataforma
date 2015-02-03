# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from analisis.configuracion.models  import *
from comunicacion.lugar.models import *
from mapeo.models import *
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import GroupedForeignKey
from django.utils.translation import ugettext_lazy as _
# Create your models here.

ALCANCE_CHOICES = (
				    ('nacinal',_('Nacional')),
				    ('territorial',_('Territorial')),
    			)

class Entrevista(models.Model):
	nombre = models.CharField(_('Nombre'), max_length=200)
	posicion = models.CharField(_('Posicion'), max_length=200)
	email = models.EmailField(_('Correo'))
	organizacion = models.ForeignKey(Organizaciones, verbose_name= _('Organizacion'))
	pais = models.ForeignKey(Pais, verbose_name= _('Pais'))
	departamento = ChainedForeignKey(
								Departamento,
	 							chained_field="pais", 
	 					 		chained_model_field="pais",
	 					 		show_all=False, auto_choose=True)
	telefono = models.IntegerField(_('Telefono'))
	fecha = models.DateField(_('Fecha'))
	slug = models.SlugField(editable=False)
	alcance = models.CharField(_('Alcance'),max_length=50,choices=ALCANCE_CHOICES)
	tipo_estudio = models.ForeignKey(Tipo_Estudio, verbose_name=_('Tipo de estudio'))
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not  self.id:
			self.slug = slugify(self.nombre)
		super(Entrevista, self).save(*args, **kwargs)



ESTADO_CHOICES = (
	('Activo', _('Activo')),
	('Finalizado',_('Finalizado'))
	)

class Pregunta_1(models.Model):
	proyecto = models.CharField(max_length=250, verbose_name= _('Proyecto(s) e iniciativa(s)'))
	estado = models.CharField(_('Estado'),max_length=50,choices=ESTADO_CHOICES)
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_('Municipio'))
	socio = models.ManyToManyField(Socio,verbose_name=_('Socios'))
	tema = models.ManyToManyField(Tema,verbose_name=_('Temas'))
	slug = models.SlugField(editable=False)
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.proyecto

	#class Meta:
		#verbose_name = 'Proyectos e iniciativas'
		#verbose_name_plural = 'Proyectos e iniciativas que ha llegado su organización en los ultimos 5 años'

PREGUNTA2_CHOICES = (
    ('tecnicos',_('Tecnicos')),
    ('promotores ',_('Promotores ')),
    ('invetigadores',_('Invetigadores')),
    ('decisores',_('Decisores')),
    )

class Pregunta_2(models.Model):
	seleccion = models.CharField(max_length=50,choices=PREGUNTA2_CHOICES,verbose_name=_('Cargos'))
	hombre = models.IntegerField(verbose_name=_('Numero de Hombre(s)'))
	mujer = models.IntegerField(verbose_name=_('Numero de Mujer(es)'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Recursos humanos'
		#verbose_name_plural = 'Recursos humanos que tiene su organización'


class Pregunta_3(models.Model):
	grupo = models.ManyToManyField(Grupo,verbose_name=_('Grupos'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'A que grupos beneficia su organización'
		#verbose_name_plural = 'A que grupos beneficia su organización'

class Pregunta_4(models.Model):
	impacto = models.CharField(max_length=250, verbose_name=_('Impacto(s)'))
	grupo_beneficiario = models.ManyToManyField(Grupo,verbose_name=_('Grupos beneficiarios principales de este impacto'))
	tema = models.ManyToManyField(Tema,verbose_name=_('Temas'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Impactos Organizacionales'
		#verbose_name_plural = 'Tipos de impactos organizacionales que ha hecho su organización en los ultimos 5 años'

PRIORITIZADO_CHOICES = (
	(1,_('Si')),
	(0,_('No'))
	)

class Pregunta_5a(models.Model):
	innovacion = models.CharField(max_length=250, verbose_name=_('Innovacion(es)'))
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_('ubicacion'))
	socio = models.ManyToManyField(Socio, verbose_name=_('socio'))
	tema = models.ManyToManyField(Tema, verbose_name=_('Temas'))
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES, verbose_name=_('Prioritizado'))
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.innovacion

	#class Meta:
		#verbose_name = 'Innovación productiva u organizacional'
		#verbose_name_plural = 'Ha participado su organización en alguna innovación productiva u organizacional en la región'

class Pregunta_5c(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=_('Innovacion'))
	organizacion = models.ForeignKey(Organizaciones,verbose_name=_('Organizacion'))
	papel_1 = models.ManyToManyField(Papel,verbose_name=_('Papel'))
	entrevistado = models.ForeignKey(Entrevista)


	#class Meta:
		#verbose_name = 'Papel que juega su organización'
		#verbose_name_plural = 'Papel que juega su organización y otros socios en relación a cada innovacion'

class Pregunta_5d(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=_('Innovacion'))
	categoria = models.ManyToManyField(Categoria,verbose_name=_('Categorias'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Limitaciones'
		#verbose_name_plural = 'Principales limitaciones que afectaron el éxito de estas innovaciones'

class Pregunta_5e(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=_('Innovacion'))
	fuente = models.CharField(max_length=200, verbose_name=_('Fuente de aprendizaje de Innovacion'))
	categoria_fuente = models.ManyToManyField(Categoria_Fuente,verbose_name=_('Categoria de Fuente'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Fuentes de aprendizaje'
		#verbose_name_plural = 'Fuentes mas importantes de aprendizaje y consulta dentro y fuera de la región'

class Pregunta_6a(models.Model):
	innovacion = models.CharField(max_length=200, verbose_name=_('Innovacion(es)'))
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_('Ubicacion'))
	tema = models.ManyToManyField(Tema, verbose_name=_('Temas'))
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES, verbose_name=_('Prioritizado'))
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.innovacion
		
	#class Meta:
		#verbose_name = 'Innovaciones'
		#verbose_name_plural = 'Innovaciones en las que le gustaria trabajar a su organización en los proximas 5-10 años'

class Pregunta_6c(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=_('Innovacion'))
	organizacion = models.ForeignKey(Organizaciones,verbose_name=_('Organizacion'))
	papel = models.ManyToManyField(Papel,verbose_name=_('Papel'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Socios o colaboradores'
		#verbose_name_plural = 'Socios o colaboradores claves para llevar a cabo las innovaciones'


class Pregunta_6d(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=_('Innovacion'))
	categoria = models.ManyToManyField(Categoria,verbose_name=_('Categorias'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Posibles limitaciones'
		#verbose_name_plural = 'Posibles limitaciones para llevar a cabo estos cambios en la región'

class Pregunta_6e(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=_('Innovacion'))
	conocimient = models.CharField(max_length=200, verbose_name=_('Conocimiento clave faltante para Innovacion'))
	categoria_innovacio = models.ForeignKey(Categoria_Innovacion,verbose_name=_('Categoria de Innovacion'))
	categoria_conocimient = models.ManyToManyField(Categoria_Conocimiento,verbose_name=_('Categoria de Conocimiento'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Informacion necesaria o calve para la realización de las innovaciones'
		#verbose_name_plural = 'Informacion necesaria o calve para la realización de las innovaciones'

class Pregunta_7a(models.Model):
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_('Ubicacion'))
	seleccion = models.ManyToManyField(Seleccion_7a, verbose_name=_('Seleccion'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Sitios de campo'
		#verbose_name_plural = 'Sitios de campo donde Humidtropics debería desarrollar actividades con socios locales'

class Pregunta_7b(models.Model):
	seleccion = models.ManyToManyField(Seleccion_7b, verbose_name=_('Seleccion'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Papel que podría jugar su organización en los sitios de campo seleccionados/Humidtropics'
		#verbose_name_plural = 'Papel que podría jugar su organización en los sitios de campo seleccionados/Humidtropics'

TERRITORIO_CHOICES = (
    ('dentro',_('Dentro')),
    ('afuera',_('Afuera')),
    )

PERIODO_CHOICES = (
    ('reciente',_('Reciente')),
    ('mediano',_('Mediano')),
    ('largo',_('Largo')),
    )

PROFUNDIDAD_CHOICES = (
    ('esporadica',_('Esporádica')),
    ('fortuita',_('Fortuita')),
    ('estrategica',_('Estratégica')),
    )

class Pregunta_8(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=_('Organizacion'))
	territorio = models.CharField(max_length=50,
				choices=TERRITORIO_CHOICES,verbose_name=_('Dentro o Afuera del Territorio'))
	periodo = models.CharField(max_length=50,
				choices=PERIODO_CHOICES,verbose_name=_('Periodo de relacion'))
	profundidad = models.CharField(max_length=50,
					choices=PROFUNDIDAD_CHOICES,verbose_name=_('Profundidad de relacion'))
	tema = models.ManyToManyField(Tema_Relacion, 
				verbose_name=_('Razón o temas de la relacion'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Relación con las organizaciones'
		#verbose_name_plural = 'Relaciones con las organizaciones que radican en los territorios'


TEMA_CHOICES = (
    (1,_('Mayor y sostenible, Intensificación ecológica')),
    (2,_('Manejo sostenible de los recursos naturales de las fincas y cuencas')),
    (3,_('Mejorar la comercialización y acceso a mercados juntos')),
    (4,_('Aumento de ingreso y reduccion de pobreza')),
    (5,_('Mejorada de Seguridad alimentaria y nutrición')),
    (6,_('Empoderamiento de las mujeres y jóvenes')),
    (7,_('Innovación local e innovación a través  de políticas e instituciones')),
    )

PRIORIDAD_CHOICES = (
	('alta',_('Alta')),
	('baja',_('Baja')),
	('media',_('Media')),
	)

PAPEL_CHOICES = (
	('facilitador',_('Facilitador')),
	('neutro',_('Neutro')),
	('bloqueador',_('Bloqueador')),
	)
AUTO_EVALUACION_CHOICES = (
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
	)

class Pregunta_9(models.Model):
	tema = models.IntegerField(choices=TEMA_CHOICES, verbose_name=_('Temas'))
	prioridad = models.CharField(max_length=50,
				choices=PRIORIDAD_CHOICES,verbose_name=_('Prioridad Organizacional'))
	papel = models.CharField(max_length=50,
				choices=PAPEL_CHOICES,verbose_name=_('Papel de la organizacion en el territorio'))
	conocimiento = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text=_('Escala de valor: 1 (debilidad) hasta 5 (fuerte)'))
	experiencia = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text=_('Escala de valor: 1 (debilidad) hasta 5 (fuerte)'))
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Análisis de capacidad de las organizaciones'
		#verbose_name_plural = 'Análisis de capacidad de las organizaciones'

SOBRE_CHOICES = (
	(1,_('Situación de las fincas (producción y biodivarsidad)')),
	(2,_('Situación de los recursos naturales y manejo de ellos')),
	(3,_('Situación de comerzialización y acceso a mercados')),
	(4,_('Situación de organización de las comunidades y capacidad de aprendizaje')),
	(5,_('Situación de equidad de género y generacional')),
	(6,_('Situación de seguridad alimentaria y nutricional')),
	(7,_('Situación de ingreso familiar y pobreza'))
	)

DISPONIBILIDAD_CHOICES = (
	('informe tecnico',_('Informé técnico')),
	('informe ejecutivo',_('Informé ejecutivo')),
	('base de datos',_('Base de datos')),
	('sistema en linea',_('Sistema en línea')),
	)

TIPO_ESTUDIO_CHOICES = (
	(1,_('Estudio linea base')),
	(2,_('Estudio de impacto')),
	(3,_('Diagnóstico de datos')),
	(4,_('Estudio de casos')),
	(5,_('Tesis')),
	(6,_('Otros')),
	)

class Pregunta_11(models.Model):
	sobre = models.IntegerField(choices=SOBRE_CHOICES)
	#tipo_estudio = models.IntegerField(verbose_name='Tipo de estudio',choices=TIPO_ESTUDIO_CHOICES)
	tipo_estudio1 = models.IntegerField(verbose_name=_('Tipo de estudio'),choices=TIPO_ESTUDIO_CHOICES)
	calendario = models.IntegerField(verbose_name=_('Año'))
	disponibilidad = models.CharField(max_length=100,choices=DISPONIBILIDAD_CHOICES)
	entrevistado = models.ForeignKey(Entrevista)

	#class Meta:
		#verbose_name = 'Datos que tiene la organización para análisis de datos secundarios'
		#verbose_name_plural = 'Datos que tiene la organización para análisis de datos secundarios'

