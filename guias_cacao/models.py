# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from mapeo.models import Persona
from sorl.thumbnail import ImageField
from multiselectfield import MultiSelectField

# Create your models here.
class FichaSombra(models.Model):
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

    class Meta:
        verbose_name = "Ficha sombra"
        verbose_name_plural = "Fichas sombras"


class Foto1(models.Model):
    """docstring for Foto1"""
    foto = ImageField(upload_to='foto1Sombra')
    ficha = models.ForeignKey(FichaSombra)


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

    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Punto1"


class Cobertura1(models.Model):
    cobertura = models.FloatField('% de cobertura de sombra')
    ficha = models.ForeignKey(FichaSombra)

#------------------- fin de punto 1 --------------------------------------


class Foto2(models.Model):
    """docstring for Foto2"""
    foto = ImageField(upload_to='foto2Sombra')
    ficha = models.ForeignKey(FichaSombra)


class Punto2(models.Model):
    especie = models.ForeignKey(Especies)
    pequena = models.FloatField(verbose_name='Pequeña')
    mediana = models.FloatField(verbose_name='Mediana')
    grande = models.FloatField(verbose_name='Grande')
    tipo = models.IntegerField(choices=CHOICE_TIPO_PUNTO)
    tipo_de_copa = models.IntegerField(choices=CHOICE_TIPO_COPA_PUNTO)
    uso = models.IntegerField(choices=CHOICE_TIPO_USO_PUNTO)

    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Punto2"


class Cobertura2(models.Model):
    cobertura = models.FloatField('% de cobertura de sombra')
    ficha = models.ForeignKey(FichaSombra)

#------------------- fin de punto 2 --------------------------------------


class Foto3(models.Model):
    """docstring for Foto3"""
    foto = ImageField(upload_to='foto3Sombra')
    ficha = models.ForeignKey(FichaSombra)


class Punto3(models.Model):
    especie = models.ForeignKey(Especies)
    pequena = models.FloatField(verbose_name='Pequeña')
    mediana = models.FloatField(verbose_name='Mediana')
    grande = models.FloatField(verbose_name='Grande')
    tipo = models.IntegerField(choices=CHOICE_TIPO_PUNTO)
    tipo_de_copa = models.IntegerField(choices=CHOICE_TIPO_COPA_PUNTO)
    uso = models.IntegerField(choices=CHOICE_TIPO_USO_PUNTO)

    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Punto3"


class Cobertura3(models.Model):
    cobertura = models.FloatField('% de cobertura de sombra')
    ficha = models.ForeignKey(FichaSombra)

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
    ficha = models.ForeignKey(FichaSombra)

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
    ficha = models.ForeignKey(FichaSombra)


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
    ficha = models.ForeignKey(FichaSombra)

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
    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Si marca aumentar la sombra"


class ManejoSombra(models.Model):
    herramientas = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene herramienta para manejo de sombra? ")
    formacion = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene formación para manejo de sombra? ")
    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name = "Herramienta y formación de sombras"

#-------------------------- fin ficha sombra ------------------------------

class FichaPoda(models.Model):
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
    )
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

    ficha = models.ForeignKey(FichaPoda)

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

    ficha = models.ForeignKey(FichaPoda)

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

    ficha = models.ForeignKey(FichaPoda)

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

    ficha = models.ForeignKey(FichaPoda)

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

    ficha = models.ForeignKey(FichaPoda)

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

    ficha = models.ForeignKey(FichaPoda)

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

    ficha = models.ForeignKey(FichaPoda)

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

    ficha = models.ForeignKey(FichaPoda)

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

    ficha = models.ForeignKey(FichaPoda)

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

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return 'Analisis'

    class Meta:
        verbose_name_plural = 'Análisis de poda y acciones'

class ManejoPoda(models.Model):
    herramientas = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene herramienta para manejo de poda? ")
    formacion = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene formación para manejo de poda? ")
    ficha = models.ForeignKey(FichaPoda)

    class Meta:
        verbose_name = "Herramienta y formación de poda"

# ---------------------------- fin de ficha poda ------------------------------

class FichaPlaga(models.Model):
    productor = models.ForeignKey(Persona,
            verbose_name='Nombre de productor o productora',
            related_name='persona_productor_plaga')
    tecnico = models.ForeignKey(Persona,
            verbose_name='Nombre de técnico',
            related_name='persona_tecnico_plaga')
    fecha_visita = models.DateField()

    def __unicode__(self):
        return self.productor.nombre

    class Meta:
        verbose_name = "Ficha plaga"
        verbose_name_plural = "Fichas plagas"


CHOICE_ENFERMEDADES_CACAOTALES = (
        (1, 'Monilia'),
        (2, 'Mazorca negra'),
        (3, 'Mal de machete'),
        (4, 'Mal de talluelo en el vivero'),
        (5, 'Barrenadores de tallo'),
        (6, 'Zompopos'),
        (7, 'Chupadores o áfidos'),
        (8, 'Escarabajos'),
        (9, 'Comején'),
        (10, 'Otros'),
    )

class PlagasEnfermedad(models.Model):
    plagas = models.IntegerField(choices=CHOICE_ENFERMEDADES_CACAOTALES,
                blank=True, null=True, verbose_name="Plagas y enfermedades")
    visto = models.IntegerField(choices=CHOICE_SI_NO,
                blank=True, null=True, verbose_name="He visto en mi cafetal")
    dano = models.IntegerField(choices=CHOICE_SI_NO,
                            blank=True, null=True, verbose_name="Hace daño año con año")
    promedio = forms.FloatField("¿Promedio nivel de daño en %?")

    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"PlagasEnfermedad"

CHOICE_ACCIONES_ENFERMEDADES = (
        (1, 'Recuento de plagas'),
        (2, 'Cortar las mazorcas enfermas'),
        (3, 'Abonar las plantas'),
        (4, 'Aplicar Caldos'),
        (5, 'Aplicar Fungicidas'),
        (6, 'Manejo de sombra'),
        (7, 'Podar las plantas de cacao'),
        (8, 'Aplicar venenos para Zompopo'),
        (9, 'Control de Comején'),
        (10, 'Otros'),
    )

class AccionesEnfermedad(models.Model):
    plagas_acciones = models.IntegerField(choices=CHOICE_ACCIONES_ENFERMEDADES,
                    blank=True, null=True, verbose_name="Plagas y enfermedades")
    realiza_manejo = models.IntegerField(choices=CHOICE_SI_NO,
                blank=True, null=True, verbose_name="Realiza en manejo")
    cuantas_veces = models.IntegerField(blank=True, null=True,
                verbose_name="Cuantas veces realizan el manejo")
    meses = MultiSelectField(choices=CHOICES_FECHA_PODA,
            verbose_name='En qué meses realizan el manejo')
    ficha = models.ForeignKey(FichaPlaga)


    def __unicode__(self):
        return u"AccionesEnfermedad"

CHOICE_ORIENTACION = (
    ("A", 'Técnico'),
    ("B", 'Casa comercial'),
    ("C", 'Cooperativa'),
    ("D", 'Otros productores'),
    ("E", 'Experiencia propia/costumbres'),
    ("F", 'Otros medio de comunicación'),
)

class Orientacion(models.Model):
    fuentes = MultiSelectField(choices=CHOICE_ORIENTACION,
            verbose_name='3. Las fuentes de orientación para manejo de las plagas y enfermedades')
    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"Orientacion"


CHOICE_OBSERVACION_PUNTO1 = (
        (1, 'Monilia'),
        (2, 'Mazorca Negra'),
        (3, 'Mal de machete'),
        (4, 'Daño de ardilla'),
        (5, 'Daño de barrenador'),
        (6, 'Chupadores'),
        (7, 'Daño de zompopo'),
        (8, 'Bejuco'),
        (9, 'Tanda'),
        (10, 'Otros'),
    )

class ObservacionPunto1(models.Model):
    planta = models.IntegerField(choices="CHOICE_OBSERVACION_PUNTO1",
                                blank=True, null=True)
    uno = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)

    ficha = models.ForeignKey(RELATED_MODEL)

    def __unicode__(self):
        return u"Punto1"

class ObservacionPunto1Nivel(models.Model):
    planta = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
     ficha = models.ForeignKey(RELATED_MODEL)


    def __unicode__(self):
        return u"Punto1 nivel produccion"


class ObservacionPunto2(models.Model):
    planta = models.IntegerField(choices="CHOICE_OBSERVACION_PUNTO1",
                                blank=True, null=True)
    uno = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)

    ficha = models.ForeignKey(RELATED_MODEL)

    def __unicode__(self):
        return u"Punto2"

class ObservacionPunto2Nivel(models.Model):
    planta = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)

    ficha = models.ForeignKey(RELATED_MODEL)


    def __unicode__(self):
        return u"Punto2 nivel produccion"

class ObservacionPunto3(models.Model):
    planta = models.IntegerField(choices="CHOICE_OBSERVACION_PUNTO1",
                                blank=True, null=True)
    uno = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)

    ficha = models.ForeignKey(RELATED_MODEL)

    def __unicode__(self):
        return u"Punto3"

class ObservacionPunto3Nivel(models.Model):
    planta = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)

    ficha = models.ForeignKey(RELATED_MODEL)


    def __unicode__(self):
        return u"Punto3 nivel produccion"

CHOICE_ENFERMEDADES = (
        ("A", 'Monilia'),
        ("B", 'Mazorca negra'),
        ("C", 'Mal de machete'),
        ("D", 'Mal de talluelo en el vivero'),
        ("E", 'Barrenadores de tallo'),
        ("F", 'Zompopos'),
        ("G", 'Chupadores o áfidos'),
        ("H", 'Escarabajos'),
        ("J", 'Comején'),
        ("k", 'Otros'),
    )

CHOICE_SITUACION_PLAGAS = (
        (1, 'Varias plagas en todos los puntos'),
        (2, 'Varias plagas en algunos puntos'),
        (3, 'Pocas plagas en todos los puntos'),
        (4, 'Pocas plagas en algunos puntos'),
        (5, 'Una plaga en todos los puntos'),
        (6, 'Una plaga en algunos puntos'),
    )

class ProblemasPrincipales(models.Model):
    observadas = MultiSelectField(choices=CHOICE_ENFERMEDADES,
            verbose_name='Las plagas y enfermedades observadas en la parcela')
    situacion = models.IntegerField(choices=CHOICE_SITUACION_PLAGAS,blank=True, null=True)
    principales = MultiSelectField(choices=CHOICE_ENFERMEDADES,
            verbose_name='Las plagas y enfermedades principales en la parcela')

    def __unicode__(self):
        return u"problemas principales"
