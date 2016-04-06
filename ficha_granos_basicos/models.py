# -*- coding: utf-8 -*-
from django.db import models
from multiselectfield import MultiSelectField
from mapeo.models import Persona

# Create your models here.

#Inicio Ficha de control de gastos ---------------------------------
RUBRO_CHOICES = (
    (1,'Maíz'),
    (2,'Frijol'),
)

class Gastos(models.Model):
    productor = models.ForeignKey(Persona)
    fecha_siembra = models.DateField()
    rubro = models.IntegerField(choices=RUBRO_CHOICES)

    class Meta:
        verbose_name_plural = 'Registro de Gastos'

ACTIVIDAD_CHOICES = (
    (1,'Preparación de suelo'),
    (2,'Siembra'),
    (3,'Aplicación de Agroquímico'),
    (4,'Limpia de maleza'),
    (5,'Arrancar'),
    (6,'Doblar'),
    (7,'Aporrear'),
    (8,'Transporte'),
    (9,'Materiales/Herramientas'),
)

class TablaGastos(models.Model):
    fecha = models.DateField()
    actividad = models.IntegerField(choices=ACTIVIDAD_CHOICES)
    hombres = models.IntegerField()
    mujeres = models.IntegerField()
    dias_persona = models.IntegerField()
    valor = models.IntegerField(verbose_name='Valor en C$')
    descripcion = models.TextField()
    gastos = models.ForeignKey(Gastos)

#Fin Ficha de control de gastos -----------------------------------

#Inicio Ficha toma de decisiones ----------------------------------
VISITA2_CHOICES = (
    (1,'Visita 1 / Pre Siembra'),
    (2,'Visita 2 / Post Siembra'),
    (3,'Visita 3 / Desarrollo Vegetativo'),
    (4,'Visita 4 / Maduración'),
    (5,'Visita 5 / Post Cosecha - Almacenamiento'),
)

AREAS_DECISIONES_CHOICES = (
    (1,'Semillas'),
    (2,'Fertilidad del Suelo'),
    (3,'Macrofauna del Suelo'),
    (4,'Malezas'),
    (5,'Vigor'),
    (6,'Plagas y Enfermedades'),
    (7,'Población'),
    (8,'Estimado de Cosecha'),
    (9,'Almacenamiento'),
)

SI_NO_CHOICES = (
    (1,'Si'),
    (2,'No'),
)

class TomaDecisiones(models.Model):
    productor = models.ForeignKey(Persona)

    class Meta:
        verbose_name_plural = 'Registro y Monitoreo de Cumplimiento'

class TablaDecisiones(models.Model):
    visita = models.IntegerField(choices=VISITA2_CHOICES)
    area = models.IntegerField(choices=AREAS_DECISIONES_CHOICES)
    decision = models.TextField(verbose_name='Decisión/Recomendación')
    seleccion = models.IntegerField(choices=SI_NO_CHOICES,verbose_name='¿Se Hizo?')
    porque = models.TextField(verbose_name='¿Porqué?')
    toma_deciciones = models.ForeignKey(TomaDecisiones)

#Fin Ficha toma de decisiones -------------------------------------

#Inicio Ficha monitoreo 1 -----------------------------------------
VISITA_CHOICES = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)

AREAS_CHOICES = (
    (1,'Semillas'),
    (2,'Suelo'),
    (3,'Macrofauna del Suelo'),
    (4,'Malezas'),
    (5,'Vigor'),
    (6,'Plagas y Enfermedades'),
    (7,'Población'),
    (8,'Estimado de Cosecha'),
    (9,'Almacenamiento'),
)

class InfoGeneral(models.Model):
    productor = models.ForeignKey(Persona)
    fecha = models.DateField()
    visita = models.IntegerField(choices=VISITA_CHOICES)
    areas = MultiSelectField(choices=AREAS_CHOICES)

    class Meta:
        abstract = True

CICLO_CHOICES = (
    (1,'Primera'),
    (2,'Postrera'),
)

CULTIVO_CHOICES = (
    (1,'Maíz'),
    (2,'Frijol'),
    (3,'Maíz y Frijol'),
)
#datos del monitoreo ------------------------------
class DatosMonitoreo(InfoGeneral):
    ciclo_productivo = models.IntegerField(choices=CICLO_CHOICES)
    cultivo = models.IntegerField(choices=CULTIVO_CHOICES)
    fecha_siembra = models.DateField()
    fecha_cosecha = models.DateField()

    class Meta:
        verbose_name_plural = 'II. Datos del Monitoreo'

DIRECCION_CHOICES = (
    (1,'N'),
    (2,'NE'),
    (3,'E'),
    (4,'SE'),
    (5,'S'),
    (6,'SO'),
    (7,'O'),
    (8,'NO'),
)

FERTILIDAD_CHOICES = (
    (1,'Fértil'),
    (2,'Med. Fértil'),
    (3,'Pobre'),
)

ACCESO_AGUA_CHOICES = (
    (1,'Pozo'),
    (2,'Quebrada'),
    (3,'Río'),
    (4,'Ojo de agua'),
)

class DatosParcela(models.Model):
    nombre = models.CharField(max_length=100)
    edad_parcela = models.FloatField()
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    direccion_viento = models.IntegerField(choices=DIRECCION_CHOICES)
    percepcion_fertilidad = models.IntegerField(choices=FERTILIDAD_CHOICES)
    tamano_parcela = models.FloatField(verbose_name='Tamaño de la parcela (mz)')
    profundidad_capa = models.FloatField(verbose_name='Profundidad de capa arable (cm)')
    acceso_agua = models.IntegerField(choices=SI_NO_CHOICES,verbose_name='¿Tiene acceso a agua en su parcela?')
    fuente_agua = MultiSelectField(choices=ACCESO_AGUA_CHOICES,verbose_name='Como tiene acceso a agua')
    distancia = models.FloatField(verbose_name='¿A qué distancia tiene la fuente de agua?')
    datos_monitoreo = models.ForeignKey(DatosMonitoreo)

    class Meta:
        verbose_name_plural = 'Datos de la parcela'

DISTRIBUCION_CHOICES = (
    (1,'% Área'),
    (2,'% Inclinación'),
)

class DistribucionPendiente(models.Model):
    seleccion = models.IntegerField(choices=DISTRIBUCION_CHOICES)
    inclinado = models.FloatField()
    plano = models.FloatField()
    ondulado = models.FloatField()
    datos_monitoreo = models.ForeignKey(DatosMonitoreo)

    class Meta:
        verbose_name_plural = 'Distribución de la Pendiente/Inclinación'

RESPUESTA_CHOICES = (
    (1,'Propio'),
    (2,'Crédito'),
    (3,'Propio y Crédito'),
)

class RecursosSiembra(models.Model):
    rubro = models.IntegerField(choices=RUBRO_CHOICES)
    respuesta = models.IntegerField(choices=RESPUESTA_CHOICES)
    datos_monitoreo = models.ForeignKey(DatosMonitoreo)

    class Meta:
        verbose_name_plural = 'Recursos para la siembra'

ANIO_CHOICES = (
    (1,'2014'),
    (2,'2015'),
    (3,'2016'),
    (4,'2017'),
    (5,'2018'),
    (6,'2019'),
    (7,'2020'),
)

class HistorialRendimiento(models.Model):
    rubro = models.IntegerField(choices=RUBRO_CHOICES)
    ciclo_productivo = models.IntegerField(choices=CICLO_CHOICES)
    anio = models.IntegerField(choices=ANIO_CHOICES)
    rendimiento = models.FloatField()
    datos_monitoreo = models.ForeignKey(DatosMonitoreo)

    class Meta:
        verbose_name_plural = 'Historial de rendimiento'
#fin datos del monitoreo ------------------------------

#semilla ---------------------------------------------
TIPO_SEMILLA_CHOICES = (
    (1,'Criolla'),
    (2,'Acriollada'),
    (3,'Mejorada'),
)

class Semillas(InfoGeneral):
    semilla_frijol = models.IntegerField(choices=TIPO_SEMILLA_CHOICES)
    semilla_maiz = models.IntegerField(choices=TIPO_SEMILLA_CHOICES)

    class Meta:
        verbose_name_plural = 'IV. Semilla'

class NombreSemilla(models.Model):
    rubro = models.IntegerField(choices=RUBRO_CHOICES)
    nombre = models.CharField(max_length=100)
    semillas = models.ForeignKey(Semillas)

    class Meta:
        verbose_name_plural = 'Nombre semillas'

PROCEDENCIA_CHOICES = (
    (1,'Cosecha anterior'),
    (2,'Productor/a de la comunidad'),
    (3,'Productor/a de otra comunidad'),
    (4,'Cooperativa o Agroservicio'),
    (5,'ONG'),
    (6,'Gobierno'),
)

class ProcedenciaSemilla(models.Model):
    rubro = models.IntegerField(choices=RUBRO_CHOICES)
    procedencia = models.IntegerField(choices=PROCEDENCIA_CHOICES)
    semillas = models.ForeignKey(Semillas)

    class Meta:
        verbose_name_plural = 'Procedencia de la semilla'

class PruebaGerminacion(models.Model):
    rubro = models.IntegerField(choices=RUBRO_CHOICES)
    respuesta = models.IntegerField(choices=SI_NO_CHOICES)
    porcentaje = models.FloatField()
    semillas = models.ForeignKey(Semillas)

    class Meta:
        verbose_name_plural = 'Prueba de germinación'
#fin semilla -----------------------------------------

#Inicio suelo ----------------------------------------
UNIDADES_CHOICES = (
    (1,'%'),
    (2,'ppm'),
    (3,'meq/100'),
    (4,'gr/cm3'),
)

class ParametrosSuelo(models.Model):
    parametro = models.CharField(max_length=100)
    unidad = models.IntegerField(choices=UNIDADES_CHOICES,blank=True,null=True)
    nivel_critico = models.FloatField(blank=True,null=True)
    nivel_suficiencia = models.FloatField(blank=True,null=True)

    def __unicode__(self):
		return self.parametro

    class Meta:
        verbose_name_plural = 'Parámetros de suelo'

class Suelo(models.Model):
    productor = models.ForeignKey(Persona)
    fecha = models.DateField()
    visita = models.IntegerField(choices=VISITA_CHOICES)
    areas = MultiSelectField(choices=AREAS_CHOICES)

    class Meta:
        verbose_name_plural = 'V. Suelo'

class TablaSuelo(models.Model):
    parametro = models.ForeignKey(ParametrosSuelo)
    resultado = models.FloatField()
    suelo = models.ForeignKey(Suelo)
#fin  suelo ------------------------------------------------------

#inicio macrofauna -----------------------------------------------
class Macrofauna(models.Model):
    productor = models.ForeignKey(Persona)
    fecha = models.DateField()
    visita = models.IntegerField(choices=VISITA_CHOICES)
    areas = MultiSelectField(choices=AREAS_CHOICES)

    class Meta:
        verbose_name_plural = 'VI. Macrofauna de Suelo y Malezas'

ESPECIES_CHOICES = (
    (1,'Cuerudo'),
    (2,'Gusano Alambre'),
    (3,'Zompopos'),
    (4,'Tortuguilla'),
    (5,'Coralillo'),
    (6,'Gallina Ciega (Larva grande)'),
    (7,'Gallina Ciega (Larva pequeña)'),
)

class TablaMacrofauna(models.Model):
    especie = models.IntegerField(choices=ESPECIES_CHOICES)
    est1 = models.IntegerField()
    est2 = models.IntegerField()
    est3 = models.IntegerField()
    est4 = models.IntegerField()
    est5 = models.IntegerField()
    promedio = models.FloatField(editable=False)
    macrofauna = models.ForeignKey(Macrofauna)

    def save(self, *args, **kwargs):
        self.promedio = (self.est1 + self.est2 + self.est3 + self.est4 + self.est5) / float(5)
        super(TablaMacrofauna, self).save(*args, **kwargs)
#fin macrofauna --------------------------------------------------

#inicio malezas --------------------------------------------------

#fin malezas -----------------------------------------------------

#Fin Ficha monitoreo 1 --------------------------------------------
