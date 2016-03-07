# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from mapeo.models import Persona
from sorl.thumbnail import ImageField
from multiselectfield import MultiSelectField


class Ficha(models.Model):
    productor = models.ForeignKey(
        Persona,
        verbose_name='Nombre de productor o productora',
        related_name='setproductor')
    tecnico = models.ForeignKey(
        Persona,
        verbose_name='Nombre de técnico',
        related_name='settecnico')
    fecha_visita = models.DateField()

    def __unicode__(self):
        return self.productor.nombre

CHOICE_SI_NO = (
    (1, 'Si'),
    (2, 'No'),
)
CHOICE_PRODUCCION = (
    (1, 'Alta'),
    (2, 'Media'),
    (3, 'Baja'),
)
CHOICE_PLANTAS1 = (
    (1, 'Altura en mt'),
    (2, 'Ancho de copa mt'),
)
CHOICE_PLANTAS2 = (
    (1,
     'Formación de horqueta'),
    (2,
     'Ramas en contacto '),
    (3,
     'Ramas entrecruzadas'),
    (4,
     'Ramas cercanas al suelo'),
    (5,
     'Chupones'),
    (6,
     'Penetración de Luz'),
    (7,
     'Nivel de producción'))
CHOICE_PLANTAS3 = (
    (1, 'Nivel de producción'),
)


class Punto1A(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS1)
    uno = models.FloatField(verbose_name='1')
    dos = models.FloatField(verbose_name='2')
    tres = models.FloatField(verbose_name='3')
    cuatro = models.FloatField(verbose_name='4')
    cinco = models.FloatField(verbose_name='5')
    seis = models.FloatField(verbose_name='6')
    siete = models.FloatField(verbose_name='7')
    ocho = models.FloatField(verbose_name='8')
    nueve = models.FloatField(verbose_name='9')
    diez = models.FloatField(null=True, blank=True, verbose_name='10')

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto1B(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS2)
    uno = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto1C(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return self.get_plantas_display()

#----------------------------- fin del punto 1 ---------------------------


class Punto2A(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS1)
    uno = models.FloatField(verbose_name='1')
    dos = models.FloatField(verbose_name='2')
    tres = models.FloatField(verbose_name='3')
    cuatro = models.FloatField(verbose_name='4')
    cinco = models.FloatField(verbose_name='5')
    seis = models.FloatField(verbose_name='6')
    siete = models.FloatField(verbose_name='7')
    ocho = models.FloatField(verbose_name='8')
    nueve = models.FloatField(verbose_name='9')
    diez = models.FloatField(null=True, blank=True, verbose_name='10')

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto2B(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS2)
    uno = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto2C(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return self.get_plantas_display()

#------------ fin del punto 2 ----------------------------


class Punto3A(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS1)
    uno = models.FloatField(verbose_name='1')
    dos = models.FloatField(verbose_name='2')
    tres = models.FloatField(verbose_name='3')
    cuatro = models.FloatField(verbose_name='4')
    cinco = models.FloatField(verbose_name='5')
    seis = models.FloatField(verbose_name='6')
    siete = models.FloatField(verbose_name='7')
    ocho = models.FloatField(verbose_name='8')
    nueve = models.FloatField(verbose_name='9')
    diez = models.FloatField(null=True, blank=True, verbose_name='10')

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto3B(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS2)
    uno = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto3C(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return self.get_plantas_display()

# -------------------- fin punto 3 ----------------------------

CHOICES_PROBLEMA_PLANTA = (('A', 'Altura'),
                           ('B', 'Ancho'),
                           ('C', 'Ramas'),
                           ('D', 'Horqueta'),
                           ('E', 'Chupones'),
                           ('F', 'Poca entrada de Luz'),
                           ('G', 'Baja productividad'),
                           ('H', 'Ninguna'),
                           )
CHOICES_TIPO_PODA = (('A', 'Poda de copa'),
                     ('B', 'Poda de ramas'),
                     ('C', 'Ramas'),
                     ('D', 'Formar horquetas'),
                     ('E', 'Deschuponar'),
                     ('F', 'Ninguna'),
                     )

CHOICE_REALIZA_PODA = (
    (1, 'En toda la parcela'),
    (2, 'En Varios partes'),
    (3, 'En algunas partes'), )
CHOICE_VIGOR = (
    (1, 'Todas'),
    (2, 'Algunas'),
    (3, 'Ninguna'), )
CHOICE_ENTRADA_LUZ = (
    (1, 'Poda de copa'),
    (2, 'Quitar ramas entrecruzadas'),
    (3, 'Arreglar la sombra'),
)

CHOICES_FECHA_PODA = (('A', 'Enero'),
                      ('B', 'Febrero'),
                      ('C', 'Marzo'),
                      ('D', 'Abril'),
                      ('E', 'Mayo'),
                      ('F', 'Junio'),
                      ('G', 'Julio'),
                      ('H', 'Agosto'),
                      ('I', 'Septiembre'),
                      ('J', 'Octubre'),
                      ('K', 'Noviembre'),
                      ('L', 'Diciembre'),
                      )


class AnalisisPoda(models.Model):
    campo1 = MultiSelectField(choices=CHOICES_PROBLEMA_PLANTA, verbose_name='¿Cuáles son los problemas principales en cuanto a las estructuras de las plantas?')
    campo2 = MultiSelectField(choices=CHOICES_TIPO_PODA, verbose_name='¿Qué tipo de poda podemos aplicar para mejorar la estructura de las plantas?')
    campo3 = models.IntegerField(choices=CHOICE_REALIZA_PODA, verbose_name='¿Dónde se va a realizar la poda para mejorar la estructura de las plantas?')
    campo4 = models.IntegerField(choices=CHOICE_VIGOR, verbose_name='Las plantas tienen suficiente vigor, hojas y ramas para ser podadas?')
    campo5 = models.IntegerField(choices=CHOICE_ENTRADA_LUZ, verbose_name='¿Cómo podemos mejorar la entrada de luz en las plantas con la poda?')
    campo6 = MultiSelectField(choices=CHOICES_FECHA_PODA, verbose_name='¿Cuándo se van a realizar las podas?')

    ficha = models.ForeignKey(Ficha)

    def __unicode__(self):
        return 'Analisis'

    class Meta:
        verbose_name_plural = 'Análisis de poda y acciones'
