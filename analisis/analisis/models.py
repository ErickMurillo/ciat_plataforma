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
				    (1,_('Nacional')),
				    (2,_('Territorial')),
    			)

FECHA_CHOICES = (
					(2014,2014),
					(2015,2015),
					(2016,2016),
					(2017,2017),
					(2018,2018),
					(2019,2019),
					(2020,2020),
					(2021,2021),
					(2022,2022),
					(2023,2023),
					(2024,2024),
				)

class Entrevista(models.Model):
	nombre = models.CharField(_(u'Nombre'), max_length=200)
	posicion = models.CharField(_(u'Posicion'), max_length=200)
	email = models.EmailField(_(u'Correo'))
	organizacion = models.ForeignKey(Organizaciones, verbose_name= _(u'Organizacion'))
	pais = models.ForeignKey(Pais, verbose_name= _(u'Pais'))
	departamento = models.ManyToManyField(Departamento)
	telefono = models.IntegerField(_(u'Telefono'))
	#fecha = models.IntegerField(_(u'Fecha'),choices=FECHA_CHOICES)
	fecha1 = models.IntegerField(_(u'Fecha'),choices=FECHA_CHOICES)
	slug = models.SlugField(editable=False)
	alcance1 = models.IntegerField(_(u'Alcance'),choices=ALCANCE_CHOICES)
	tipo_estudio = models.ForeignKey(Tipo_Estudio, verbose_name=_(u'Tipo de estudio'))
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not  self.id:
			self.slug = slugify(self.nombre)
		super(Entrevista, self).save(*args, **kwargs)



ESTADO_CHOICES = (
	(1,_(u'Activo')),
	(2,_(u'Finalizado')),
	)

class Pregunta_1(models.Model):
	proyecto = models.CharField(max_length=250, verbose_name= _(u'Proyecto(s) e iniciativa(s)'))
	estado1 = models.IntegerField(_(u'Estado'),choices=ESTADO_CHOICES)
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_(u'Municipio'))
	socio = models.ManyToManyField(Organizaciones,verbose_name=_(u'Socios'))
	tema = models.ManyToManyField(Tema,verbose_name=_(u'Temas'))
	slug = models.SlugField(editable=False)
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.proyecto

	class Meta:
		verbose_name = _(u'Proyectos e iniciativas que ha llevado su organizacion en los ultimos 5 years')
		verbose_name_plural = _(u'Proyectos e iniciativas que ha llevado su organizacion en los ultimos 5 años')

PREGUNTA2_CHOICES = (
    (1,_(u'Tecnicos')),
    (2,_(u'Promotores ')),
    (3,_(u'Invetigadores')),
    (4,_(u'Decisores')),
    (5,_(u'Administrativos')),
    )

class Pregunta_2(models.Model):
	seleccion1 = models.IntegerField(choices=PREGUNTA2_CHOICES,verbose_name=_(u'Cargos'))
	hombre = models.IntegerField(verbose_name=_(u'Numero de Hombre(s)'))
	mujer = models.IntegerField(verbose_name=_(u'Numero de Mujer(es)'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Recursos humanos')
		verbose_name_plural = _(u'Recursos humanos que tiene su organización')

	def __unicode__(self):
		return self.seleccion1

class Pregunta_3(models.Model):
	grupo = models.ManyToManyField(Grupo,verbose_name=_(u'Grupos'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'A que grupos beneficia su organización')
		verbose_name_plural = _(u'A que grupos beneficia su organización')



class Pregunta_4(models.Model):
	impacto = models.CharField(max_length=250, verbose_name=_(u'Impacto(s)'))
	grupo_beneficiario = models.ManyToManyField(Grupo,verbose_name=_(u'Grupos beneficiarios principales de este impacto'))
	tema = models.ManyToManyField(Tema,verbose_name=_(u'Temas'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Impactos Organizacionales')
		verbose_name_plural = _(u'Tipos de impactos organizacionales que ha hecho su organización en los ultimos 5 años')

	def __unicode__(self):
		return self.impacto

PRIORITIZADO_CHOICES = (
	(1,_(u'Si')),
	(0,_(u'No')),
	)

class Pregunta_5a(models.Model):
	innovacion = models.CharField(max_length=250, verbose_name=_(u'Innovacion(es)'))
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_(u'ubicacion'))
	socio = models.ManyToManyField(Organizaciones, verbose_name=_(u'socio'))
	tema = models.ManyToManyField(Tema, verbose_name=_(u'Temas'))
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES, verbose_name=_(u'Prioritizado'))
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.innovacion

	class Meta:
		verbose_name = _(u'Innovación productiva u organizacional')
		verbose_name_plural = _(u'Ha participado su organización en alguna innovación productiva u organizacional en la región')

class Pregunta_5c(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=_(u'Innovacion'))
	entrevistado = models.ForeignKey(Entrevista)


	class Meta:
		verbose_name = _(u'Papel que juega su organización')
		verbose_name_plural = _(u'Papel que juega su organización y otros socios en relación a cada innovación')

	def __unicode__(self):
		return self.innovacion

class Pregunta_5c_nested(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=_(u'Organizaciones'))
	papel_1 = models.ManyToManyField(Papel,verbose_name=_(u'Papel'))
	pregunta_5c = models.ForeignKey(Pregunta_5c)

	class Meta:
		verbose_name = _(u'Organizaciones colaborativas de innovación')
		verbose_name_plural = _(u'Organizaciones colaborativas de innovación')

	def __unicode__(self):
		return self.organizacion

class Pregunta_5d(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=_(u'Innovación'))
	categoria = models.ManyToManyField(Categoria,verbose_name=_(u'Categorias'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Limitaciones')
		verbose_name_plural = _(u'Principales limitaciones que afectaron el éxito de estas innovaciones')

	def __unicode__(self):
		return self.innovacion

class Pregunta_5e(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=_(u'Innovación'))
	fuente = models.CharField(max_length=200, verbose_name=_(u'Fuente de aprendizaje de Innovación'))
	categoria_fuente = models.ManyToManyField(Categoria_Fuente,verbose_name=_(u'Categoria de Fuente'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Fuentes de aprendizaje')
		verbose_name_plural = _(u'Fuentes mas importantes de aprendizaje y consulta dentro y fuera de la región')

	def __unicode__(self):
		return self.innovacion

class Pregunta_6a(models.Model):
	innovacion = models.CharField(max_length=200, verbose_name=_(u'Innovación(es)'))
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_(u'Ubicación'))
	tema = models.ManyToManyField(Tema, verbose_name=_(u'Temas'))
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES, verbose_name=_(u'Prioritizado'))
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.innovacion
		
	class Meta:
		verbose_name = _(u'Innovaciones')
		verbose_name_plural = _(u'Innovaciones en las que le gustaría trabajar a su organización en los proximas 5-10 años')

class Pregunta_6c(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=_(u'Innovación'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Socios o colaboradores')
		verbose_name_plural = _(u'Socios o colaboradores claves para llevar a cabo las innovaciones')

	def __unicode__(self):
		return self.innovacion

class Pregunta_6c_nested(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=_(u'Organizaciones'))
	papel = models.ManyToManyField(Papel,verbose_name=_(u'Papel'))
	pregunta_6c = models.ForeignKey(Pregunta_6c)

	class Meta:
			verbose_name = _(u'Organizaciones colaborativas de innovación')
			verbose_name_plural = _(u'Organizaciones colaborativas de innovación')

	def __unicode__(self):
		return self.organizacion

class Pregunta_6d(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=_(u'Innovación'))
	categoria = models.ManyToManyField(Categoria,verbose_name=_(u'Categorias'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Posibles limitaciones')
		verbose_name_plural = _(u'Posibles limitaciones para llevar a cabo estos cambios en la región')
	
	def __unicode__(self):
		return self.innovacion

class Pregunta_6e(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=_(u'Innovacion'))
	conocimient = models.CharField(max_length=200, verbose_name=_(u'Conocimiento clave faltante para Innovacion'))
	categoria_innovacio = models.ForeignKey(Categoria_Innovacion,verbose_name=_(u'Categoria de Innovacion'))
	categoria_conocimient = models.ManyToManyField(Categoria_Conocimiento,verbose_name=_(u'Categoria de Conocimiento'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Información necesaria o clave para la realización de las innovaciones')
		verbose_name_plural = _(u'Información necesaria o clave para la realización de las innovaciones')

	def __unicode__(self):
		return self.innovacion

class Pregunta_7a(models.Model):
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_(u'Ubicación'))
	seleccion = models.ManyToManyField(Seleccion_7a, verbose_name=_(u'Selección'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Sitios de campo')
		verbose_name_plural = _(u'Sitios de campo donde Humidtropics debería desarrollar actividades con socios locales')

class Pregunta_7b(models.Model):
	seleccion = models.ManyToManyField(Seleccion_7b, verbose_name=_(u'Selección'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Papel que podría jugar su organización en los sitios de campo seleccionados/Humidtropics')
		verbose_name_plural = _(u'Papel que podría jugar su organización en los sitios de campo seleccionados/Humidtropics')

TERRITORIO_CHOICES = (
    (1,_(u'Dentro')),
    (2,_(u'Afuera')),
    )

PERIODO_CHOICES = (
    (1,_(u'Reciente')),
    (2,_(u'Mediano')),
    (3,_(u'Largo')),
    )

PROFUNDIDAD_CHOICES = (
    (1,_(u'Esporádica')),
    (2,_(u'Fortuita')),
    (3,_(u'Estratégica')),
    )

class Pregunta_8(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=_(u'Organización'))
	territorio1 = models.IntegerField(choices=TERRITORIO_CHOICES,verbose_name=_(u'Dentro o Afuera del Territorio'))
	periodo1 = models.IntegerField(choices=PERIODO_CHOICES,verbose_name=_(u'Periodo de relación'))
	profundidad1 = models.IntegerField(choices=PROFUNDIDAD_CHOICES,verbose_name=_(u'Profundidad de relación'))
	tema = models.ManyToManyField(Tema_Relacion, 
				verbose_name=_(u'Razón o temas de la relación'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Relación con las organizaciones')
		verbose_name_plural = _(u'Relaciones con las organizaciones que radican en los territorios')

	def __unicode__(self):
		return self.organizacion

TEMA_CHOICES = (
    (1,_(u'Mayor y sostenible, Intensificación ecológica')),
    (2,_(u'Manejo sostenible de los recursos naturales de las fincas y cuencas')),
    (3,_(u'Mejorar la comercialización y acceso a mercados juntos')),
    (4,_(u'Aumento de ingreso y reducción de pobreza')),
    (5,_(u'Mejorada de Seguridad alimentaria y nutrición')),
    (6,_(u'Empoderamiento de las mujeres y jóvenes')),
    (7,_(u'Innovación local e innovación a través  de políticas e instituciones')),
    )

PRIORIDAD_CHOICES = (
	(1,_(u'Alta')),
	(2,_(u'Baja')),
	(3,_(u'Media')),
	)

PAPEL_CHOICES = (
	(1,_(u'Facilitador')),
	(2,_(u'Neutro')),
	(3,_(u'Bloqueador')),
	)
AUTO_EVALUACION_CHOICES = (
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
	)

class Pregunta_9(models.Model):
	tema = models.IntegerField(choices=TEMA_CHOICES, verbose_name=_(u'Temas'))
	prioridad1 = models.IntegerField(choices=PRIORIDAD_CHOICES,verbose_name=_(u'Prioridad Organizacional'))
	papel1 = models.IntegerField(choices=PAPEL_CHOICES,verbose_name=_('Papel de la organización en el territorio'))
	conocimiento = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text=_(u'Escala de valor: 1 (debilidad) hasta 5 (fuerte)'))
	experiencia = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text=_(u'Escala de valor: 1 (debilidad) hasta 5 (fuerte)'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Análisis de capacidad de las organizaciones')
		verbose_name_plural = _(u'Análisis de capacidad de las organizaciones')

	def __unicode__(self):
		return self.tema

SOBRE_CHOICES = (
	(1,_(u'Situación de las fincas (producción y biodivarsidad)')),
	(2,_(u'Situación de los recursos naturales y manejo de ellos')),
	(3,_(u'Situación de comercialización y acceso a mercados')),
	(4,_(u'Situación de organización de las comunidades y capacidad de aprendizaje')),
	(5,_(u'Situación de equidad de género y generacional')),
	(6,_(u'Situación de seguridad alimentaria y nutricional')),
	(7,_(u'Situación de ingreso familiar y pobreza')),
	)

DISPONIBILIDAD_CHOICES = (
	(1,_(u'Informé técnico')),
	(2,_(u'Informé ejecutivo')),
	(3,_(u'Base de datos')),
	(4,_(u'Sistema en línea')),
	(5,_(u'Internet')),
	)

TIPO_ESTUDIO_CHOICES = (
	(1,_(u'Estudio linea base')),
	(2,_(u'Estudio de impacto')),
	(3,_(u'Diagnóstico de datos')),
	(4,_(u'Estudio de casos')),
	(5,_(u'Tesis')),
	(6,_(u'Otros')),
	)

class Pregunta_11(models.Model):
	sobre = models.IntegerField(choices=SOBRE_CHOICES,verbose_name=_(u'Sobre'))
	#tipo_estudio = models.IntegerField(verbose_name='Tipo de estudio',choices=TIPO_ESTUDIO_CHOICES)
	tipo_estudio1 = models.IntegerField(choices=TIPO_ESTUDIO_CHOICES,verbose_name=_(u'Tipo de estudio'))
	calendario = models.IntegerField(verbose_name=_(u'Año'))
	disponibilidad1 = models.IntegerField(choices=DISPONIBILIDAD_CHOICES,verbose_name=_(u'Disponibilidad'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Datos que tiene la organización para análisis de datos secundarios')
		verbose_name_plural = _(u'Datos que tiene la organización para análisis de datos secundarios')

	def __unicode__(self):
		return self.sobre