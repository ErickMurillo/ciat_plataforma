# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from analysis.configuration.models  import *
from comunicacion.lugar.models import *
from mapeo.models import *
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import GroupedForeignKey
from django.utils.translation import ugettext_lazy as _

# Create your models here.

ALCANCE_CHOICES = (	
				    (1,_('National')),
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
	nombre = models.CharField('Name', max_length=200)
	posicion = models.CharField(_(u'Position'), max_length=200)
	email = models.EmailField(_(u'Email'))
	organizacion = models.ForeignKey(Organizaciones, verbose_name= _(u'Organization'),related_name='Org')
	pais = models.ForeignKey(Pais, verbose_name= _(u'Country'),related_name='Pais')
	departamento = models.ManyToManyField(Departamento,verbose_name='Department',related_name='Deparment')
	telefono = models.IntegerField(_(u'Phone'))
	#fecha = models.IntegerField(_(u'Fecha'),choices=FECHA_CHOICES)
	fecha1 = models.IntegerField(_(u'Date'),choices=FECHA_CHOICES)
	slug = models.SlugField(editable=False)
	alcance1 = models.IntegerField(_(u'Scope'),choices=ALCANCE_CHOICES)
	tipo_estudio = models.ForeignKey(Tipo_Estudio, verbose_name=_(u'Type of study'))
	usuario = models.ForeignKey(User,related_name='Usuario')

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not  self.id:
			self.slug = slugify(self.nombre)
		super(Entrevista, self).save(*args, **kwargs)

	class Meta:
			verbose_name = _(u'Interview')
			verbose_name_plural = _(u'Interviews')

ESTADO_CHOICES = (
	(1,_(u'Activo')),
	(2,_(u'Finalizado')),
	)

class Pregunta_1(models.Model):
	proyecto = models.CharField(max_length=250, verbose_name= _(u'Projects and initiatives'))
	estado1 = models.IntegerField(_(u'Status'),choices=ESTADO_CHOICES)
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_(u'Location(s)'),related_name='Location')
	socio = models.ManyToManyField(Organizaciones,verbose_name=_(u'Partner(s)'),related_name='Partner')
	tema = models.ManyToManyField(Tema,verbose_name=_(u'Themes'))
	slug = models.SlugField(editable=False)
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.proyecto

	class Meta:
		verbose_name = _(u'Projects and initiatives has your organization carried out over the last five years')
		verbose_name_plural = _(u'Projects and initiatives has your organization carried out over the last five years')

PREGUNTA2_CHOICES = (
    (1,_(u'Technicians')),
    (2,_(u'Promoters ')),
    (3,_(u'Researchers')),
    (4,_(u'Makers')),
    (5,_(u'Administrative')),
    )

class Pregunta_2(models.Model):
	seleccion1 = models.IntegerField(choices=PREGUNTA2_CHOICES,verbose_name=_(u'Charges'))
	hombre = models.IntegerField(verbose_name=_(u'Number of Male(s)'))
	mujer = models.IntegerField(verbose_name=_(u'Number of Women ( s)'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Human resources')
		verbose_name_plural = _(u'Human resources does your organization have')

	def __unicode__(self):
		return self.seleccion1

class Pregunta_3(models.Model):
	grupo = models.ManyToManyField(Grupo,verbose_name=_(u'Groups'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'What groups benefit your organization')
		verbose_name_plural = _(u'What groups benefit your organization')



class Pregunta_4(models.Model):
	impacto = models.CharField(max_length=250, verbose_name=_(u'Impact(s)'))
	grupo_beneficiario = models.ManyToManyField(Grupo,verbose_name=_(u'Main beneficiaries groups of this impact'))
	tema = models.ManyToManyField(Tema,verbose_name=_(u'Themes'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Organizational impacts')
		verbose_name_plural = _(u'Types of organizational impacts that your organization has done in the last five yearss')

	def __unicode__(self):
		return self.impacto

PRIORITIZADO_CHOICES = (
	(1,_(u'Yes')),
	(0,_(u'No')),
	)

class Pregunta_5a(models.Model):
	innovacion = models.CharField(max_length=250, verbose_name=_(u'Innovation(s)'))
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_(u'Location(s)'),related_name='Departamento')
	socio = models.ManyToManyField(Organizaciones, verbose_name=_(u'Partner(s)'),related_name='Socio')
	tema = models.ManyToManyField(Tema, verbose_name=_(u'Themes'))
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES, verbose_name=_(u'Prioritized'))
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.innovacion

	class Meta:
		verbose_name = _(u'Productive innovation or organizational ')
		verbose_name_plural = _(u'Has your organization participated in any productive or organizational innovation in the region')

class Pregunta_5c(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=_(u'Innovation'))
	entrevistado = models.ForeignKey(Entrevista)


	class Meta:
		verbose_name = _(u'Role that play your organization')
		verbose_name_plural = _(u'Role that play your organization and other partners in relation to each innovation')

	def __unicode__(self):
		return self.innovacion

class Pregunta_5c_nested(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=_(u'Organizations'),related_name='Organization')
	papel_1 = models.ManyToManyField(Papel,verbose_name=_(u'Role'))
	pregunta_5c = models.ForeignKey(Pregunta_5c)

	class Meta:
		verbose_name = _(u'Collaborative organizations of innovation ')
		verbose_name_plural = _(u'Collaborative organizations of innovation ')

	def __unicode__(self):
		return self.organizacion.nombre

class Pregunta_5d(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=_(u'Innovation'))
	categoria = models.ManyToManyField(Categoria,verbose_name=_(u'Categories'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Limitations')
		verbose_name_plural = _(u'Principals limitations  affecting the success of these innovations')

	def __unicode__(self):
		return self.innovacion

class Pregunta_5e(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=_(u'Innovation'))
	fuente = models.CharField(max_length=200, verbose_name=_(u'Source of Learning of Innovation'))
	categoria_fuente = models.ManyToManyField(Categoria_Fuente,verbose_name=_(u'Source category'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Source category')
		verbose_name_plural = _(u'Most important sources of learning and consultation within and outside the region')

	def __unicode__(self):
		return self.innovacion

class Pregunta_6a(models.Model):
	innovacion = models.CharField(max_length=200, verbose_name=_(u'Innovation(s)'))
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_(u'Location(s)'),related_name='Municipio')
	tema = models.ManyToManyField(Tema, verbose_name=_(u'Themes'))
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES, verbose_name=_(u'Prioritized'))
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.innovacion
		
	class Meta:
		verbose_name = _(u'Innovations')
		verbose_name_plural = _(u'Innovations would your organization like to work on in the next 5–10 years')

class Pregunta_6c(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=_(u'Innovation'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Partners or contributors')
		verbose_name_plural = _(u'Key partners or contributors to carry out innovations')

	def __unicode__(self):
		return self.innovacion

class Pregunta_6c_nested(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=_(u'Organization'),related_name='Orga')
	papel = models.ManyToManyField(Papel,verbose_name=_(u'Role'))
	pregunta_6c = models.ForeignKey(Pregunta_6c)

	class Meta:
		verbose_name = _(u'Collaborative organizations of innovation')
		verbose_name_plural = _(u'Collaborative organizations of innovation')

	def __unicode__(self):
		return self.organizacion

class Pregunta_6d(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=_(u'Innovation'))
	categoria = models.ManyToManyField(Categoria,verbose_name=_(u'Categories'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Possible limitations')
		verbose_name_plural = _(u'Possible limitations to carry out these changes in the region')
	
	def __unicode__(self):
		return self.innovacion

class Pregunta_6e(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=_(u'Innovation'))
	conocimient = models.CharField(max_length=200, verbose_name=_(u'Key Knowledge for Innovation missing'))
	categoria_innovacio = models.ForeignKey(Categoria_Innovacion,verbose_name=_(u'Innovation category'))
	categoria_conocimient = models.ManyToManyField(Categoria_Conocimiento,verbose_name=_(u'Knowledge category'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Key information needed to perform innovations')
		verbose_name_plural = _(u'Key information needed to perform innovations')

	def __unicode__(self):
		return self.innovacion

class Pregunta_7a(models.Model):
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=_(u'Location(s)'),related_name='Ubicacion')
	seleccion = models.ManyToManyField(Seleccion_7a, verbose_name=_(u'Selection'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Field sites')
		verbose_name_plural = _(u'Field sites where Humidtropics should develop activities with local partners')

class Pregunta_7b(models.Model):
	seleccion = models.ManyToManyField(Seleccion_7b, verbose_name=_(u'Selection'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Role that could play your organization in selectes field sites/Humidtropics')
		verbose_name_plural = _(u'Role that could play your organization in selectes field sites/Humidtropics')

TERRITORIO_CHOICES = (
    (1,_(u'Inside')),
    (2,_(u'Outside')),
    )

PERIODO_CHOICES = (
    (1,_(u'Recent')),
    (2,_(u'Medium')),
    (3,_(u'Long')),
    )

PROFUNDIDAD_CHOICES = (
    (1,_(u'Sporadic')),
    (2,_(u'Casualty')),
    (3,_(u'Strategic')),
    )

class Pregunta_8(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=_(u'Organization'),related_name='Organizacion')
	territorio1 = models.IntegerField(choices=TERRITORIO_CHOICES,verbose_name=_(u'Inside or Outside the Territory'))
	periodo1 = models.IntegerField(choices=PERIODO_CHOICES,verbose_name=_(u'Relationship period'))
	profundidad1 = models.IntegerField(choices=PROFUNDIDAD_CHOICES,verbose_name=_(u'Relationship'))
	tema = models.ManyToManyField(Tema_Relacion,verbose_name=_(u'Relationship themes'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Relationship with organizations')
		verbose_name_plural = _(u'Relations with organizations based in the territories')

	def __unicode__(self):
		return self.organizacion

TEMA_CHOICES = (
    (1,_(u'Higher and sustainable , ecological intensification')),
    (2,_(u'Sustainable management of natural resources and watershed farms')),
    (3,_(u'Improve marketing and market access together')),
    (4,_(u'Increased income and poverty reduction')),
    (5,_(u'Improved food security and nutrition')),
    (6,_(u'Empowerment of women and youth')),
    (7,_(u'Local innovation and innovation through policies and institutions')),
    )

PRIORIDAD_CHOICES = (
	(1,_(u'High')),
	(2,_(u'Low')),
	(3,_(u'Medium')),
	)

PAPEL_CHOICES = (
	(1,_(u'Facilitator')),
	(2,_(u'Neutral')),
	(3,_(u'Blocker')),
	)
AUTO_EVALUACION_CHOICES = (
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
	)

class Pregunta_9(models.Model):
	tema = models.IntegerField(choices=TEMA_CHOICES, verbose_name=_(u'Themes'))
	prioridad1 = models.IntegerField(choices=PRIORIDAD_CHOICES,verbose_name=_(u'Organizational priority'))
	papel1 = models.IntegerField(choices=PAPEL_CHOICES,verbose_name=_('Role of the organization in the territory'))
	conocimiento = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text=_(u'Scale value : 1 (weak) to 5 (strong)'))
	experiencia = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text=_(u'Scale value : 1 (weak) to 5 (strong)'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Analysis of capacity of the organizations')
		verbose_name_plural = _(u'Analysis of capacity of the organizations')

	def __unicode__(self):
		return self.tema

SOBRE_CHOICES = (
	(1,_(u'Situation of farms (production and biodiversity)')),
	(2,_(u'Situation of natural resources and handling them')),
	(3,_(u'Marketing situation and market access')),
	(4,_(u'Situation organization of communities and learning ability')),
	(5,_(u'Situation of gender and generational equity')),
	(6,_(u'Situation of food and nutritional security')),
	(7,_(u'Situation of family income and poverty')),
	)

DISPONIBILIDAD_CHOICES = (
	(1,_(u'Technical report')),
	(2,_(u'Executive report')),
	(3,_(u'Database')),
	(4,_(u'Online system')),
	(5,_(u'Internet')),
	)

TIPO_ESTUDIO_CHOICES = (
	(1,_(u'Base line study')),
	(2,_(u'Impact study')),
	(3,_(u'Diagnostic data')),
	(4,_(u'Case studies')),
	(5,_(u'Thesis')),
	(6,_(u'Others')),
	)

class Pregunta_11(models.Model):
	sobre = models.IntegerField(choices=SOBRE_CHOICES,verbose_name=_(u'About'))
	#tipo_estudio = models.IntegerField(verbose_name='Tipo de estudio',choices=TIPO_ESTUDIO_CHOICES)
	tipo_estudio1 = models.IntegerField(choices=TIPO_ESTUDIO_CHOICES,verbose_name=_(u'Type of study'))
	calendario = models.IntegerField(verbose_name=_(u'Year'))
	disponibilidad1 = models.IntegerField(choices=DISPONIBILIDAD_CHOICES,verbose_name=_(u'Availability'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = _(u'Data that has the organization for analysis of secondary data')
		verbose_name_plural = _(u'Data that has the organization for analysis of secondary data')

	def __unicode__(self):
		return self.sobre