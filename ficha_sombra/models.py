# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from mapeo.models import Persona
from sorl.thumbnail import ImageField

# Create your models here.


class Ficha(models.Model):
    productor = models.ForeignKey(
        Persona,
        verbose_name='Nombre de productor o productora',
        related_name='persona_productor')
    tecnico = models.ForeignKey(
        Persona,
        verbose_name='Nombre de técnico',
        related_name='persona_tecnico')
    fecha_visita = models.DateField()

    def __unicode__(self):
        return self.productor.nombre


class Foto1(models.Model):
    """docstring for Foto1"""
    foto = ImageField(upload_to='foto1Sombra')
    ficha = models.ForeignKey(Ficha)


class Especies(models.Model):
    nombre = models.CharField('Nombre de la especie', max_length=250)

    def __unicode__(self):
        return self.nombre

CHOICE_TIPO_PUNTO = (
    (1, 'Perennifolia'),
    (2, 'Caducifolia'),
)

CHOICE_TIPO_COPA_PUNTO = (
    (1, 'Copa ancha'),
    (2, 'Copa angosta'),
    (3, 'Copa mediana'),
)

CHOICE_TIPO_USO_PUNTO = (
    (1, 'Leña'),
    (2, 'Fruta'),
    (3, 'Madera'),
    (4, 'Sombra'),
    (5, 'Nutrientes'),
)


class Punto1(models.Model):
    especie = models.ForeignKey(Especies)
    pequena = models.FloatField(verbose_name='Pequeña')
    mediana = models.FloatField(verbose_name='Mediana')
    grande = models.FloatField(verbose_name='Grande')
    tipo = models.IntegerField(choices=CHOICE_TIPO_PUNTO)
    tipo_de_copa = models.IntegerField(choices=CHOICE_TIPO_COPA_PUNTO)
    uso = models.IntegerField(choices=CHOICE_TIPO_USO_PUNTO)

    ficha = models.ForeignKey(Ficha)

    class Meta:
        verbose_name_plural = "Punto1"


class Cobertura1(models.Model):
    cobertura = models.FloatField('% de cobertura de sombra')
    ficha = models.ForeignKey(Ficha)

#------------------- fin de punto 1 --------------------------------------


class Foto2(models.Model):
    """docstring for Foto2"""
    foto = ImageField(upload_to='foto2Sombra')
    ficha = models.ForeignKey(Ficha)


class Punto2(models.Model):
    especie = models.ForeignKey(Especies)
    pequena = models.FloatField(verbose_name='Pequeña')
    mediana = models.FloatField(verbose_name='Mediana')
    grande = models.FloatField(verbose_name='Grande')
    tipo = models.IntegerField(choices=CHOICE_TIPO_PUNTO)
    tipo_de_copa = models.IntegerField(choices=CHOICE_TIPO_COPA_PUNTO)
    uso = models.IntegerField(choices=CHOICE_TIPO_USO_PUNTO)

    ficha = models.ForeignKey(Ficha)

    class Meta:
        verbose_name_plural = "Punto2"


class Cobertura2(models.Model):
    cobertura = models.FloatField('% de cobertura de sombra')
    ficha = models.ForeignKey(Ficha)

#------------------- fin de punto 2 --------------------------------------


class Foto3(models.Model):
    """docstring for Foto3"""
    foto = ImageField(upload_to='foto3Sombra')
    ficha = models.ForeignKey(Ficha)


class Punto3(models.Model):
    especie = models.ForeignKey(Especies)
    pequena = models.FloatField(verbose_name='Pequeña')
    mediana = models.FloatField(verbose_name='Mediana')
    grande = models.FloatField(verbose_name='Grande')
    tipo = models.IntegerField(choices=CHOICE_TIPO_PUNTO)
    tipo_de_copa = models.IntegerField(choices=CHOICE_TIPO_COPA_PUNTO)
    uso = models.IntegerField(choices=CHOICE_TIPO_USO_PUNTO)

    ficha = models.ForeignKey(Ficha)

    class Meta:
        verbose_name_plural = "Punto3"


class Cobertura3(models.Model):
    cobertura = models.FloatField('% de cobertura de sombra')
    ficha = models.ForeignKey(Ficha)

#------------------- fin de punto 3 --------------------------------------


class AnalisisSombra(models.Model):
    densidad = models.IntegerField(
        choices=(
            (1,
             'Alta'),
            (2,
             'Adecuada'),
            (3,
             'Baja'),
        ),
        verbose_name='Densidad de árboles de sombra ')
    forma_copa = models.IntegerField(
        choices=(
            (1,
             'Ancha'),
            (2,
             'Adecuada'),
            (3,
             'Angosta'),
        ),
        verbose_name='Forma de copa de árboles de sombra ')
    arreglo = models.IntegerField(choices=((1, 'Uniforme'), (2, 'Desuniforme'),),
                                  verbose_name='Arreglo de árboles ')
    hojarasca = models.IntegerField(
        choices=(
            (1,
             'Suficiente'),
            (2,
             'No Suficiente'),
        ),
        verbose_name='Cantidad de hojarasca ')
    calidad_hojarasca = models.IntegerField(
        choices=(
            (1,
             'Rico en nutrientes'),
            (2,
             'Pobre en nutriente'),
        ),
        verbose_name='Calidad de hojarasca ')
    competencia = models.IntegerField(
        choices=(
            (1,
             'Fuerte'),
            (2,
             'Mediana'),
            (3,
             'Leve'),
        ),
        verbose_name='Competencia de árboles con cacao ')
    Problema = models.IntegerField(
        choices=(
            (1,
             'Cobertura'),
            (2,
             'Mal arreglo'),
            (3,
             'Competencia'),
            (4,
             'Densidad Tipo de árboles'),
            (5,
             'Ninguno')),
        verbose_name='Problema de sombra ')
    ficha = models.ForeignKey(Ficha)

    class Meta:
        verbose_name_plural = "Análisis sobre sombra y árboles de sombra"

CHOICE_ACCIONES_SOMBRA = (
    (1, 'Reducir la sombra'),
    (2, 'Aumentar la sombra'),
    (3, 'Ninguna'),
)

CHOICE_PODA = (
    (1, 'Si'),
    (2, 'No'),
)

CHOICE_TODO = (
    (1, 'En todo la parcela '),
    (2, 'Solo en una parte de la parcela'),
)


class AccionesSombra(models.Model):
    accion = models.IntegerField(
        choices=CHOICE_ACCIONES_SOMBRA,
        verbose_name="Que acciones hay que realizar ")
    ficha = models.ForeignKey(Ficha)


class ReducirSombra(models.Model):
    poda = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Podando árboles")
    poda_cuales = models.CharField(max_length=350)
    eliminando = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Eliminando árboles ")
    eliminando_cuales = models.CharField(max_length=350)
    todo = models.IntegerField(
        choices=CHOICE_TODO,
        verbose_name="Todo o partes")
    que_parte = models.CharField(max_length=250)
    ficha = models.ForeignKey(Ficha)

    class Meta:
        verbose_name_plural = "Si marca reducir la sombra"


class AumentarSombra(models.Model):
    sembrando = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Sembrando árboles")
    sembrando_cuales = models.CharField(max_length=350)
    cambiando = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Eliminando árboles ")
    cambiando_cuales = models.CharField(max_length=350)
    todo = models.IntegerField(
        choices=CHOICE_TODO,
        verbose_name="En todo la parcela o Solo en una parte de la parcela")
    que_parte = models.CharField(max_length=250)
    ficha = models.ForeignKey(Ficha)

    class Meta:
        verbose_name_plural = "Si marca aumentar la sombra"


class Manejo(models.Model):
    herramientas = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene herramienta para manejo de sombra? ")
    formacion = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene formación para manejo de sombra? ")
    ficha = models.ForeignKey(Ficha)

    class Meta:
        verbose_name = "Herramienta y formación de sombras"
