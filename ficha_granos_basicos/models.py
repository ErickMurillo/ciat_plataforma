# -*- coding: utf-8 -*-
from django.db import models
from multiselectfield import MultiSelectField
from mapeo.models import Persona
from comunicacion.utils import *
from sorl.thumbnail import ImageField

# Create your models here.
#Inicio Ficha monitoreo 1 -----------------------------------------
SI_NO_CHOICES = (
    (1,'Si'),
    (2,'No'),
)

RUBRO_CHOICES = (
    (1,'Maíz'),
    (2,'Frijol'),
)

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

class Monitoreo(models.Model):
    productor = models.ForeignKey(Persona)
    fecha = models.DateField()
    visita = models.IntegerField(choices=VISITA_CHOICES)
    areas = MultiSelectField(choices=AREAS_CHOICES)

    def __unicode__(self):
		return '%s - Visita #%s' % (self.productor, self.visita)

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
class DatosMonitoreo(models.Model):
    ciclo_productivo = models.IntegerField(choices=CICLO_CHOICES)
    cultivo = models.IntegerField(choices=CULTIVO_CHOICES)
    fecha_siembra = models.DateField()
    fecha_cosecha = models.DateField()
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Datos del Monitoreo'

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
    monitoreo = models.ForeignKey(Monitoreo)

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
    monitoreo = models.ForeignKey(Monitoreo)

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
    monitoreo = models.ForeignKey(Monitoreo)

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
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Historial de rendimiento'
#fin datos del monitoreo ------------------------------

# #semilla ---------------------------------------------
TIPO_SEMILLA_CHOICES = (
    (1,'Criolla'),
    (2,'Acriollada'),
    (3,'Mejorada'),
)

class Semillas(models.Model):
    semilla_frijol = models.IntegerField(choices=TIPO_SEMILLA_CHOICES)
    semilla_maiz = models.IntegerField(choices=TIPO_SEMILLA_CHOICES)
    nombre_frijol = models.CharField(max_length=100)
    nombre_maiz = models.CharField(max_length=100)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Semilla'

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
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Procedencia de la semilla'

class PruebaGerminacion(models.Model):
    rubro = models.IntegerField(choices=RUBRO_CHOICES)
    respuesta = models.IntegerField(choices=SI_NO_CHOICES)
    porcentaje = models.FloatField(blank=True,null=True)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Prueba de germinación'
# #fin semilla -----------------------------------------
#
# #Inicio suelo ----------------------------------------
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
    parametro = models.ForeignKey(ParametrosSuelo)
    resultado = models.FloatField()
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Suelo'
# #fin  suelo ------------------------------------------------------
#
# #inicio macrofauna -----------------------------------------------
# ESPECIES_CHOICES = (
#     (1,'Cuerudo'),
#     (2,'Gusano Alambre'),
#     (3,'Zompopos'),
#     (4,'Tortuguilla'),
#     (5,'Coralillo'),
#     (6,'Gallina Ciega (Larva grande)'),
#     (7,'Gallina Ciega (Larva pequeña)'),
# )
TIPO_PLAGA_CHOICES = (
    (1,'Plaga'),
    (2,'Enfermedad'),
)

CULTIVO2_CHOICES = (
    (1,'Maíz'),
    (2,'Frijol'),
    (3,'Maíz y Frijol'),
)

UMBRAL_CHOICES = (
    (1,'Rango'),
    (2,'Comentario'),
)

class Especies(models.Model):
    nombre_popular = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=100,blank=True,null=True)
    reconocimiento = models.CharField(max_length=200,blank=True,null=True)
    control_cultural = models.CharField(max_length=200,blank=True,null=True)
    control_biologico = models.CharField(max_length=200,blank=True,null=True)
    control_quimico = models.CharField(max_length=200,blank=True,null=True)
    tipo = models.IntegerField(choices=TIPO_PLAGA_CHOICES)
    rubro = models.IntegerField(choices=CULTIVO2_CHOICES)
    umbral = models.IntegerField(choices=UMBRAL_CHOICES)
    rango_min = models.FloatField(blank=True,null=True)
    rango_max = models.FloatField(blank=True,null=True)
    descripcion = models.CharField(max_length=150,blank=True,null=True)

    def __unicode__(self):
		return self.nombre_popular

    class Meta:
        verbose_name_plural = 'Especies'

class FotosEspecies(models.Model):
    foto = ImageField(upload_to=get_file_path)
    especie = models.ForeignKey(Especies)

    fileDir = 'granos_basicos/especies/'

    class Meta:
        verbose_name_plural = 'Fotos Especies'

class Macrofauna(models.Model):
    especie = models.ForeignKey(Especies)
    est1 = models.IntegerField()
    est2 = models.IntegerField()
    est3 = models.IntegerField()
    est4 = models.IntegerField()
    est5 = models.IntegerField()
    promedio = models.FloatField(editable=False)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Macrofauna de Suelo y Malezas'

    def save(self, *args, **kwargs):
        self.promedio = (self.est1 + self.est2 + self.est3 + self.est4 + self.est5) / float(5)
        super(TablaMacrofauna, self).save(*args, **kwargs)
#fin macrofauna --------------------------------------------------

#inicio malezas --------------------------------------------------
COBERTURA_CHOICES = (
    (1,'Cobertura total 1'),
    (2,'Cobertura total 2'),
    (3,'Cobertura total 3'),
    (4,'Cobertura total 4'),
    (5,'Cobertura total 5'),
)

class MonitoreoMalezas(models.Model):
    cobertura = models.IntegerField(choices=COBERTURA_CHOICES)
    gramineas = models.FloatField('% de Gramíneas')
    hoja_ancha   = models.FloatField('% de Hoja Ancha')
    ciperaceas = models.FloatField('% de Ciperáceas')
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Malezas'

MALEZAS_CHOICES = (
    (1,'Gramíneas'),
    (2,'Hoja Ancha'),
    (3,'Ciperáceas'),
)

CICLO2_CHOICES = (
    (1,'Perenne'),
    (2,'Anual'),
)

class TiposMalezas(models.Model):
    nombre_popular = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=MALEZAS_CHOICES)
    ciclo = models.IntegerField(choices=CICLO2_CHOICES)

    class Meta:
        verbose_name_plural = 'Tipos de malezas'

class TablaMalezas(models.Model):
    maleza = models.ForeignKey(TiposMalezas)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Tres malezas más representativas'
#fin malezas -----------------------------------------------------

#Fin Ficha monitoreo 1 --------------------------------------------

#Inicio monitoreo 2 -----------------------------------------------
class Poblacion(models.Model):
    distancia_frijol = models.FloatField()
    distancia_maiz = models.FloatField()
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Población'

class TablaPoblacion(models.Model):
    rubro = models.IntegerField(choices=RUBRO_CHOICES)
    est1 = models.IntegerField()
    est2 = models.IntegerField()
    est3 = models.IntegerField()
    est4 = models.IntegerField()
    est5 = models.IntegerField()
    promedio = models.FloatField(editable=False)
    #Calculado la población
    numero_surcos = models.FloatField()
    metros_lineales = models.FloatField()
    poblacion = models.FloatField()
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Población'

    def save(self, *args, **kwargs):
        self.promedio = (self.est1 + self.est2 + self.est3 + self.est4 + self.est5) / float(5)
        super(TablaMacrofauna, self).save(*args, **kwargs)

#Vigor ------------------------
VIGOR_CHOICES = (
    (1,'Saludables'),
    (2,'Regulares'),
    (3,'Deficientes'),
)

class VigorFrijol(models.Model):
    plantas = models.IntegerField(choices=VIGOR_CHOICES)
    est1 = models.IntegerField()
    est2 = models.IntegerField()
    est3 = models.IntegerField()
    est4 = models.IntegerField()
    est5 = models.IntegerField()
    promedio = models.FloatField(editable=False)
    estimado_plantas = models.FloatField(editable=False)
    porcentaje = models.FloatField(editable=False)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Vigor Frijol'

    def save(self, *args, **kwargs):
        poblacion = self.est1 + self.est2 + self.est3 + self.est4 + self.est5
        promedio = poblacion / float(5)
        self.promedio = promedio
        estimado_plantas = (poblacion / float(20)) * promedio
        self.estimado_plantas = estimado_plantas
        self.porcentaje = (estimado_plantas / poblacion) * float(100)
        super(VigorFrijol, self).save(*args, **kwargs)

class VigorMaiz(models.Model):
    plantas = models.IntegerField(choices=VIGOR_CHOICES)
    est1 = models.IntegerField()
    est2 = models.IntegerField()
    est3 = models.IntegerField()
    est4 = models.IntegerField()
    est5 = models.IntegerField()
    promedio = models.FloatField(editable=False)
    estimado_plantas = models.FloatField(editable=False)
    porcentaje = models.FloatField(editable=False)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Vigor Maíz'

    def save(self, *args, **kwargs):
        poblacion = self.est1 + self.est2 + self.est3 + self.est4 + self.est5
        promedio = poblacion / float(5)
        self.promedio = promedio
        estimado_plantas = (poblacion / float(20)) * promedio
        self.estimado_plantas = estimado_plantas
        self.porcentaje = (estimado_plantas / poblacion) * float(100)
        super(VigorMaiz, self).save(*args, **kwargs)
#fin Vigor --------------------

#Plagas y enfermedades-------------------
class PlagasFrijol(models.Model):
    plaga = models.ForeignKey(Especies)
    presencia_1 = models.FloatField('Presencia 1')
    presencia_2 = models.FloatField('Presencia 2')
    presencia_3 = models.FloatField('Presencia 3')
    presencia_4 = models.FloatField('Presencia 4')
    presencia_5 = models.FloatField('Presencia 5')
    promedio_presencia = models.FloatField(editable=False)
    #Porcentaje daño
    porcentaje_dano_1 = models.FloatField('Porcentaje de Daño 1')
    porcentaje_dano_2 = models.FloatField('Porcentaje de Daño 2')
    porcentaje_dano_3 = models.FloatField('Porcentaje de Daño 3')
    porcentaje_dano_4 = models.FloatField('Porcentaje de Daño 4')
    porcentaje_dano_5 = models.FloatField('Porcentaje de Daño 5')
    promedio_dano = models.FloatField(editable=False)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Plagas en Frijol'

    def save(self, *args, **kwargs):
        sumatoria_presencia = self.presencia_1 + self.presencia_2 + self.presencia_3 + self.presencia_4 + self.presencia_5
        promedio = sumatoria_presencia / float(5)
        self.promedio_presencia = promedio / float(20)

        suma_porcentaje = self.porcentaje_dano_1 + self.porcentaje_dano_2 + self.porcentaje_dano_3 + self.porcentaje_dano_4 + self.porcentaje_dano_5
        promedio_d = suma_porcentaje / float(5)
        self.promedio_dano = promedio_d / float(20)

        super(PlagasFrijol, self).save(*args, **kwargs)

class PlagasMaiz(models.Model):
    plaga = models.ForeignKey(Especies)
    presencia_1 = models.FloatField('Presencia 1')
    presencia_2 = models.FloatField('Presencia 2')
    presencia_3 = models.FloatField('Presencia 3')
    presencia_4 = models.FloatField('Presencia 4')
    presencia_5 = models.FloatField('Presencia 5')
    promedio_presencia = models.FloatField(editable=False)
    #Porcentaje daño
    porcentaje_dano_1 = models.FloatField('Porcentaje de Daño 1')
    porcentaje_dano_2 = models.FloatField('Porcentaje de Daño 2')
    porcentaje_dano_3 = models.FloatField('Porcentaje de Daño 3')
    porcentaje_dano_4 = models.FloatField('Porcentaje de Daño 4')
    porcentaje_dano_5 = models.FloatField('Porcentaje de Daño 5')
    promedio_dano = models.FloatField(editable=False)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Plagas en Maíz'

    def save(self, *args, **kwargs):
        sumatoria_presencia = self.presencia_1 + self.presencia_2 + self.presencia_3 + self.presencia_4 + self.presencia_5
        promedio = sumatoria_presencia / float(5)
        self.promedio_presencia = promedio / float(20)

        suma_porcentaje = self.porcentaje_dano_1 + self.porcentaje_dano_2 + self.porcentaje_dano_3 + self.porcentaje_dano_4 + self.porcentaje_dano_5
        promedio_d = suma_porcentaje / float(5)
        self.promedio_dano = promedio_d / float(20)

        super(PlagasMaiz, self).save(*args, **kwargs)

class EnfermedadesFrijol(models.Model):
    enfermedad = models.ForeignKey(Especies)
    planta_1 = models.IntegerField(verbose_name='Plantas afectadas 1')
    planta_2 = models.IntegerField(verbose_name='Plantas afectadas 2')
    planta_3 = models.IntegerField(verbose_name='Plantas afectadas 3')
    planta_4 = models.IntegerField(verbose_name='Plantas afectadas 4')
    planta_5 = models.IntegerField(verbose_name='Plantas afectadas 5')
    promedio = models.FloatField(editable=False)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Enfermedades en Frijol'

    def save(self, *args, **kwargs):
        self.promedio = (self.planta_1 + self.planta_2 + self.planta_3 + self.planta_4 + self.planta_5) / float(5)
        super(EnfermmedadesFrijol, self).save(*args, **kwargs)

class EnfermedadesMaiz(models.Model):
    enfermedad = models.ForeignKey(Especies)
    planta_1 = models.IntegerField(verbose_name='Plantas afectadas 1')
    planta_2 = models.IntegerField(verbose_name='Plantas afectadas 2')
    planta_3 = models.IntegerField(verbose_name='Plantas afectadas 3')
    planta_4 = models.IntegerField(verbose_name='Plantas afectadas 4')
    planta_5 = models.IntegerField(verbose_name='Plantas afectadas 5')
    promedio = models.FloatField(editable=False)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Enfermedades en Maíz'

    def save(self, *args, **kwargs):
        self.promedio = (self.planta_1 + self.planta_2 + self.planta_3 + self.planta_4 + self.planta_5) / float(5)
        super(EnfermmedadesFrijol, self).save(*args, **kwargs)
#FIn monitoreo 2 --------------------------------------------------

#Ficha monitoreo 4 ------------------------------------------------
ESTACION_CHOICES = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)

class EstimadoCosechaFrijol(models.Model):
    estacion = models.IntegerField(choices=ESTACION_CHOICES)
    planta_1 = models.IntegerField()
    planta_2 = models.IntegerField()
    planta_3 = models.IntegerField()
    planta_4 = models.IntegerField()
    planta_5 = models.IntegerField()
    promedio = models.FloatField(editable=False)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Estimado de Cosecha Frijol'

    def save(self, *args, **kwargs):
        self.promedio = (self.planta_1 + self.planta_2 + self.planta_3 + self.planta_4 + self.planta_5) / float(5)
        super(EstimadoCosechaFrijol, self).save(*args, **kwargs)

class GranosPlanta(models.Model):
    cantidad = models.FloatField()
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Cantidad de granos por planta'

MAZORCA_CHOICES = (
    (1,'Grande'),
    (2,'Mediana'),
    (3,'Pequeña'),
)

class EstimadoCosechaMaiz(models.Model):
    mazorca = models.IntegerField(choices=MAZORCA_CHOICES)
    estacion_1 = models.IntegerField()
    estacion_2 = models.IntegerField()
    estacion_3 = models.IntegerField()
    estacion_4 = models.IntegerField()
    estacion_5 = models.IntegerField()
    promedio = models.FloatField(editable=False)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Estimado de Cosecha Maíz'

    def save(self, *args, **kwargs):
        self.promedio = (self.estacion_1 + self.estacion_2 + self.estacion_3 + self.estacion_4 + self.estacion_5) / float(5)
        super(EstimadoCosechaMaiz, self).save(*args, **kwargs)

class EstimadoCosechaMaiz2(models.Model):
    mazorca = models.IntegerField(choices=MAZORCA_CHOICES)
    peso = models.FloatField(verbose_name='Peso en lb')
    peso_promedio = models.IntegerField(verbose_name='Peso en lb x Promedio de Mazorcas')
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Estimado de Cosecha Maíz'
#fin ficha monitoreo 4 --------------------------------------------

#ficha monitoreo 5 ------------------------------------------------
class SobreCosecha(models.Model):
    rubro = models.IntegerField(choices=RUBRO_CHOICES)
    cosecha = models.FloatField()
    venta = models.FloatField()
    almacenamiento = models.FloatField()
    precio_mercado = models.FloatField()
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Sobre la Cosecha'

class TratamientoSemilla(models.Model):
    nombre = models.CharField(max_length=100)
    dosis = models.CharField(max_length=150)
    preparacion = models.TextField(blank=True)

    def __unicode__(self):
		return self.nombre

    class Meta:
        verbose_name_plural = 'Tratamiento de semilla'

class CuradoSemilla(models.Model):
    tratamiento = models.ManyToManyField(TratamientoSemilla)
    monitoreo = models.ForeignKey(Monitoreo)

    class Meta:
        verbose_name_plural = 'Curado de semilla'
#fin ficha monitoreo 5 --------------------------------------------

#Inicio Ficha de control de gastos ---------------------------------

class Gastos(models.Model):
    productor = models.ForeignKey(Monitoreo)
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

PROD_CATEGORIA_CHOICES = (
    (1,'Fertilizante'),
    (2,'Fungicida'),
    (3,'Insecticida'),
    (4,'Herbicidas'),
)

PRESENTACION_CHOICES = (
    (1,'liquido- cc/b'),
    (2,'hidrosoluble- gr/b'),
    (3,'granulado- qq/mz'),
)

class Productos(models.Model):
    nombre_comercial = models.CharField(max_length=100)
    principio_activo = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=PROD_CATEGORIA_CHOICES)
    presentacion = models.IntegerField(choices=PRESENTACION_CHOICES)

    def __unicode__(self):
		return self.nombre_comercial

    class Meta:
        verbose_name_plural = 'Productos'
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

class TomaDecisiones(models.Model):
    productor = models.ForeignKey(Monitoreo)

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
