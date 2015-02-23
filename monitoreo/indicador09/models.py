# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.monitoreo.models import *

# Create your models here.

# Indicador 9. Cultivos en la finca (periodo de referencia de mayo 2009 a abril 2010)

class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s - %s' % (self.nombre,self.unidad)

    class Meta:
        verbose_name_plural = "CultivosFinca-Cultivos"
        ordering = ['nombre']

CHOICES_QUIEN = (
                    (1, 'Hombre'),
                    (2, 'Mujer'),
                    (3, 'Ambos'),
                    (4, 'Hijas'),
                    (5, 'Hijos'),
                    (6, 'Otros'),
                    (7, 'Familiares'),
                )

class CultivosFinca(models.Model):
    ''' indicador cultivos en la finca
    '''
    cultivos = models.ForeignKey(Cultivos)
    area =  models.FloatField('Área/Mz')
    total = models.FloatField('Total producción por año')
    consumo = models.FloatField('Consumo por año')
    venta_libre = models.FloatField('Venta libre por año')
    venta_organizada = models.FloatField('Venta organizada por año')
    quien = models.IntegerField(choices=CHOICES_QUIEN, 
                                verbose_name='Quien maneja el cultivo', 
                                null=True, blank=True)      
    encuesta = models.ForeignKey(Encuesta)
    
    #campo oculto para calcular la productividad
    productivos = models.FloatField(editable=False)
    
    def save(self):
        try:
            self.productivos = self.total / self.area
        except:
            self.productivos = 0 
        super(CultivosFinca, self).save()

    def __unicode__(self):
        return u'%s' % self.cultivos.nombre
    
    class Meta:
        verbose_name_plural = "Cultivos en la finca"
        
    def nombre_encuestado(self):
        nombre_encuesta = Encuesta.objects.filter(id=self.encuesta.id).values_list('nombre', 'id')
        #return '<a href="%s">%s</a>' % (nombre_encuesta[0][1],nombre_encuesta[0][0])
        return u'<a href="/admin/simas/encuesta/%s">%s</a>' % (nombre_encuesta[0][1],nombre_encuesta[0][0])
        #return nombre_encuesta[0][1]
    nombre_encuestado.allow_tags = True
    nombre_encuestado.short_description = 'Encuestado'
#-------------------------------------------------------------------------------
