# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from analysis.configuration.models  import *
from comunicacion.lugar.models import *
from mapeo.models import *
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import GroupedForeignKey
#from django.utils.translation import ugettext_lazy as _

# Create your models here.

ALCANCE_CHOICES = (	
				    (1, ('National')),
				    (2, ('Territorial')),
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
	nombre = models.CharField((u'Name'), max_length=200)
	posicion = models.CharField((u'Position'), max_length=200)
	email = models.EmailField((u'Email'))
	organizacion = models.ForeignKey(Organizaciones, verbose_name= (u'Organization'),related_name='Org')
	pais = models.ForeignKey(Pais, verbose_name= (u'Country'),related_name='Pais')
	departamento = models.ManyToManyField(Departamento,verbose_name='Department',related_name='Deparment')
	telefono = models.IntegerField((u'Phone'))
	#fecha = models.IntegerField(_(u'Fecha'),choices=FECHA_CHOICES)
	fecha1 = models.IntegerField((u'Date'),choices=FECHA_CHOICES)
	slug = models.SlugField(editable=False)
	alcance1 = models.IntegerField((u'Scope'),choices=ALCANCE_CHOICES)
	tipo_estudio = models.ForeignKey(Tipo_Estudio, verbose_name=(u'Type of study'))
	usuario = models.ForeignKey(User,related_name='Usuario')

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not  self.id:
			self.slug = slugify(self.nombre)
		super(Entrevista, self).save(*args, **kwargs)

	class Meta:
			verbose_name = (u'Interview')
			verbose_name_plural = (u'Interviews')

ESTADO_CHOICES = (
	(1,(u'Activo')),
	(2,(u'Finalizado')),
	)

class Pregunta_1(models.Model):
	proyecto = models.CharField(max_length=250, verbose_name= (u'Projects and initiatives'))
	estado1 = models.IntegerField((u'Status'),choices=ESTADO_CHOICES)
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=(u'Location(s)'),related_name='Location')
	socio = models.ManyToManyField(Organizaciones,verbose_name=(u'Partner(s)'),related_name='Partner')
	tema = models.ManyToManyField(Tema,verbose_name=(u'Themes'))
	slug = models.SlugField(editable=False)
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.proyecto

	class Meta:
		verbose_name = (u'Projects and initiatives has your organization carried out over the last five years')
		verbose_name_plural = (u'Projects and initiatives has your organization carried out over the last five years')

PREGUNTA2_CHOICES = (
    (1,(u'Technicians')),
    (2,(u'Promoters ')),
    (3,(u'Researchers')),
    (4,(u'Makers')),
    (5,(u'Administrative')),
    )

class Pregunta_2(models.Model):
	seleccion1 = models.IntegerField(choices=PREGUNTA2_CHOICES,verbose_name=(u'Charges'))
	hombre = models.IntegerField(verbose_name=(u'Number of Male(s)'))
	mujer = models.IntegerField(verbose_name=(u'Number of Women ( s)'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Human resources')
		verbose_name_plural = (u'Human resources does your organization have')

	def __unicode__(self):
		return self.seleccion1

class Pregunta_3(models.Model):
	grupo = models.ManyToManyField(Grupo,verbose_name=(u'Groups'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'What groups benefit your organization')
		verbose_name_plural = (u'What groups benefit your organization')



class Pregunta_4(models.Model):
	impacto = models.CharField(max_length=250, verbose_name=(u'Impact(s)'))
	grupo_beneficiario = models.ManyToManyField(Grupo,verbose_name=(u'Main beneficiaries groups of this impact'))
	tema = models.ManyToManyField(Tema,verbose_name=(u'Themes'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Organizational impacts')
		verbose_name_plural = (u'Types of organizational impacts that your organization has done in the last five yearss')

	def __unicode__(self):
		return self.impacto

PRIORITIZADO_CHOICES = (
	(1,(u'Yes')),
	(0,(u'No')),
	)

class Pregunta_5a(models.Model):
	innovacion = models.CharField(max_length=250, verbose_name=(u'Innovation(s)'))
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=(u'Location(s)'),related_name='Departamento')
	socio = models.ManyToManyField(Organizaciones, verbose_name=(u'Partner(s)'),related_name='Socio')
	tema = models.ManyToManyField(Tema, verbose_name=(u'Themes'))
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES, verbose_name=(u'Prioritized'))
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.innovacion

	class Meta:
		verbose_name = (u'Productive innovation or organizational ')
		verbose_name_plural = (u'Has your organization participated in any productive or organizational innovation in the region')

class Pregunta_5c(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=(u'Innovation'))
	entrevistado = models.ForeignKey(Entrevista)


	class Meta:
		verbose_name = (u'Role that play your organization')
		verbose_name_plural = (u'Role that play your organization and other partners in relation to each innovation')

	def __unicode__(self):
		return self.innovacion

class Pregunta_5c_nested(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=(u'Organizations'),related_name='Organization')
	papel_1 = models.ManyToManyField(Papel,verbose_name=(u'Role'))
	pregunta_5c = models.ForeignKey(Pregunta_5c)

	class Meta:
		verbose_name = (u'Collaborative organizations of innovation ')
		verbose_name_plural = (u'Collaborative organizations of innovation ')

	def __unicode__(self):
		return self.organizacion.nombre

class Pregunta_5d(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=(u'Innovation'))
	categoria = models.ManyToManyField(Categoria,verbose_name=(u'Categories'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Limitations')
		verbose_name_plural = (u'Principals limitations  affecting the success of these innovations')

	def __unicode__(self):
		return self.innovacion

class Pregunta_5e(models.Model):
	innovacion = models.ForeignKey(Pregunta_5a,verbose_name=(u'Innovation'))
	fuente = models.CharField(max_length=200, verbose_name=(u'Source of Learning of Innovation'))
	categoria_fuente = models.ManyToManyField(Categoria_Fuente,verbose_name=(u'Source category'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Source category')
		verbose_name_plural = (u'Most important sources of learning and consultation within and outside the region')

	def __unicode__(self):
		return self.innovacion

class Pregunta_6a(models.Model):
	innovacion = models.CharField(max_length=200, verbose_name=(u'Innovation(s)'))
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=(u'Location(s)'),related_name='Municipio')
	tema = models.ManyToManyField(Tema, verbose_name=(u'Themes'))
	prioritizado = models.IntegerField(choices=PRIORITIZADO_CHOICES, verbose_name=(u'Prioritized'))
	entrevistado = models.ForeignKey(Entrevista)

	def __unicode__(self):
		return self.innovacion
		
	class Meta:
		verbose_name = (u'Innovations')
		verbose_name_plural = (u'Innovations would your organization like to work on in the next 5–10 years')

class Pregunta_6c(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=(u'Innovation'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Partners or contributors')
		verbose_name_plural = (u'Key partners or contributors to carry out innovations')

	def __unicode__(self):
		return self.innovacion

class Pregunta_6c_nested(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=(u'Organization'),related_name='Orga')
	papel = models.ManyToManyField(Papel,verbose_name=(u'Role'))
	pregunta_6c = models.ForeignKey(Pregunta_6c)

	class Meta:
		verbose_name = (u'Collaborative organizations of innovation')
		verbose_name_plural = (u'Collaborative organizations of innovation')

	def __unicode__(self):
		return self.organizacion

class Pregunta_6d(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=(u'Innovation'))
	categoria = models.ManyToManyField(Categoria,verbose_name=(u'Categories'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Possible limitations')
		verbose_name_plural = (u'Possible limitations to carry out these changes in the region')
	
	def __unicode__(self):
		return self.innovacion

class Pregunta_6e(models.Model):
	innovacion = models.ForeignKey(Pregunta_6a,verbose_name=(u'Innovation'))
	conocimient = models.CharField(max_length=200, verbose_name=(u'Key Knowledge for Innovation missing'))
	categoria_innovacio = models.ForeignKey(Categoria_Innovacion,verbose_name=(u'Innovation category'))
	categoria_conocimient = models.ManyToManyField(Categoria_Conocimiento,verbose_name=(u'Knowledge category'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Key information needed to perform innovations')
		verbose_name_plural = (u'Key information needed to perform innovations')

	def __unicode__(self):
		return self.innovacion

class Pregunta_7a(models.Model):
	ubicacion =  models.ManyToManyField(Municipio, verbose_name=(u'Location(s)'),related_name='Ubicacion')
	seleccion = models.ManyToManyField(Seleccion_7a, verbose_name=(u'Selection'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Field sites')
		verbose_name_plural = (u'Field sites where Humidtropics should develop activities with local partners')

class Pregunta_7b(models.Model):
	seleccion = models.ManyToManyField(Seleccion_7b, verbose_name=(u'Selection'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Role that could play your organization in selectes field sites/Humidtropics')
		verbose_name_plural = (u'Role that could play your organization in selectes field sites/Humidtropics')

TERRITORIO_CHOICES = (
    (1,(u'Inside')),
    (2,(u'Outside')),
    )

PERIODO_CHOICES = (
    (1,(u'Recent')),
    (2,(u'Medium')),
    (3,(u'Long')),
    )

PROFUNDIDAD_CHOICES = (
    (1,(u'Sporadic')),
    (2,(u'Casualty')),
    (3,(u'Strategic')),
    )

class Pregunta_8(models.Model):
	organizacion = models.ForeignKey(Organizaciones,verbose_name=(u'Organization'),related_name='Organizacion')
	territorio1 = models.IntegerField(choices=TERRITORIO_CHOICES,verbose_name=(u'Inside or Outside the Territory'))
	periodo1 = models.IntegerField(choices=PERIODO_CHOICES,verbose_name=(u'Relationship period'))
	profundidad1 = models.IntegerField(choices=PROFUNDIDAD_CHOICES,verbose_name=(u'Relationship'))
	tema = models.ManyToManyField(Tema_Relacion,verbose_name=(u'Relationship themes'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Relationship with organizations')
		verbose_name_plural = (u'Relations with organizations based in the territories')

	def __unicode__(self):
		return self.organizacion

TEMA_CHOICES = (
    (1,(u'Higher and sustainable , ecological intensification')),
    (2,(u'Sustainable management of natural resources and watershed farms')),
    (3,(u'Improve marketing and market access together')),
    (4,(u'Increased income and poverty reduction')),
    (5,(u'Improved food security and nutrition')),
    (6,(u'Empowerment of women and youth')),
    (7,(u'Local innovation and innovation through policies and institutions')),
    )

PRIORIDAD_CHOICES = (
	(1,(u'High')),
	(2,(u'Low')),
	(3,(u'Medium')),
	)

PAPEL_CHOICES = (
	(1,(u'Facilitator')),
	(2,(u'Neutral')),
	(3,(u'Blocker')),
	)
AUTO_EVALUACION_CHOICES = (
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
	)

class Pregunta_9(models.Model):
	tema = models.IntegerField(choices=TEMA_CHOICES, verbose_name=(u'Themes'))
	prioridad1 = models.IntegerField(choices=PRIORIDAD_CHOICES,verbose_name=(u'Organizational priority'))
	papel1 = models.IntegerField(choices=PAPEL_CHOICES,verbose_name=('Role of the organization in the territory'))
	conocimiento = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text=(u'Scale value : 1 (weak) to 5 (strong)'))
	experiencia = models.IntegerField(choices=AUTO_EVALUACION_CHOICES,help_text=(u'Scale value : 1 (weak) to 5 (strong)'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Analysis of capacity of the organizations')
		verbose_name_plural = (u'Analysis of capacity of the organizations')

	def __unicode__(self):
		return self.tema

SOBRE_CHOICES = (
	(1,(u'Situation of farms (production and biodiversity)')),
	(2,(u'Situation of natural resources and handling them')),
	(3,(u'Marketing situation and market access')),
	(4,(u'Situation organization of communities and learning ability')),
	(5,(u'Situation of gender and generational equity')),
	(6,(u'Situation of food and nutritional security')),
	(7,(u'Situation of family income and poverty')),
	)

DISPONIBILIDAD_CHOICES = (
	(1,(u'Technical report')),
	(2,(u'Executive report')),
	(3,(u'Database')),
	(4,(u'Online system')),
	(5,(u'Internet')),
	)

TIPO_ESTUDIO_CHOICES = (
	(1,(u'Base line study')),
	(2,(u'Impact study')),
	(3,(u'Diagnostic data')),
	(4,(u'Case studies')),
	(5,(u'Thesis')),
	(6,(u'Others')),
	)

class Pregunta_11(models.Model):
	sobre = models.IntegerField(choices=SOBRE_CHOICES,verbose_name=(u'About'))
	#tipo_estudio = models.IntegerField(verbose_name='Tipo de estudio',choices=TIPO_ESTUDIO_CHOICES)
	tipo_estudio1 = models.IntegerField(choices=TIPO_ESTUDIO_CHOICES,verbose_name=(u'Type of study'))
	calendario = models.IntegerField(verbose_name=(u'Year'))
	disponibilidad1 = models.IntegerField(choices=DISPONIBILIDAD_CHOICES,verbose_name=(u'Availability'))
	entrevistado = models.ForeignKey(Entrevista)

	class Meta:
		verbose_name = (u'Data that has the organization for analysis of secondary data')
		verbose_name_plural = (u'Data that has the organization for analysis of secondary data')

	def __unicode__(self):
		return self.sobre