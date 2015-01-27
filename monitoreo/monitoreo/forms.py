# -*- coding: utf-8 -*-
from django import forms
from monitoreo.monitoreo.models import *
from comunicacion.lugar.models import *
from mapeo.models import Organizaciones

CHOICE_OPCION_F = (('','----'),(1,'Si'),(2,'No'))
CHOICE_DESDE_F = (('','----'),(1,"Menos de 5 año"),(2,"Mas de 5 años"))
CHOICE_DUENO_F = (('','----'),(1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),(5,"Colectivo"),(6,"No hay"))

def fecha_choice():
    years = []
    for en in Encuesta.objects.order_by('year').values_list('year', flat=True):
        years.append((en,en))
    return list(set(years))

def departamentos():   
    foo = Encuesta.objects.all().order_by('productor__comunidad__municipio__departamento__nombre').distinct().values_list('productor__comunidad__municipio__departamento__id', flat=True)
    return Departamento.objects.filter(id__in=foo)

class MonitoreoForm(forms.Form):
    fecha = forms.MultipleChoiceField(choices=fecha_choice())
    departamento = forms.ModelMultipleChoiceField(queryset=departamentos(), required=False, label=u'Departamentos')
    organizacion = forms.ModelMultipleChoiceField(queryset=Organizaciones.objects.all().order_by('nombre'), required=False, label=u'Organización')
    municipio = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all().order_by('nombre'), required=False)
    comunidad = forms.ModelMultipleChoiceField(queryset=Comunidad.objects.all(), required=False)
    socio = forms.ChoiceField(choices = CHOICE_OPCION_F , required=False, label="Socio Gremial")
    desde = forms.ChoiceField(choices = CHOICE_DESDE_F , required=False)
    dueno = forms.ChoiceField(label = 'Dueño', choices = CHOICE_DUENO_F , required=False)