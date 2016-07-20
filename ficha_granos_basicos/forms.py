# -*- coding: utf-8 -*-
from django import forms
from lookups import *
import selectable.forms as selectable
from .models import *
from comunicacion.lugar.models import *

class MonitoreoAdminForm(forms.ModelForm):

    class Meta(object):
        model = Monitoreo
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
        }

class VisitasAdminForm(forms.ModelForm):

    class Meta(object):
        model = Visitas
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=MonitoreoLookup),
        }

class ProductorMonitoreoAdminForm(forms.ModelForm):

    class Meta(object):
        model = Gastos
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=MonitoreoLookup),
        }

class InsumosAdminForm(forms.ModelForm):

    class Meta(object):
        model = Insumos
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=MonitoreoLookup),
        }

#filtros-----------
def fecha_choice():
    years = []
    for en in Monitoreo.objects.order_by('anio').values_list('anio', flat=True):
        years.append((en,en))
    return list(sorted(set(years)))

def municipios():
    foo = Monitoreo.objects.all().order_by('productor__comunidad__municipio__nombre').distinct().values_list('productor__comunidad__municipio__id', flat=True)
    return Municipio.objects.filter(id__in=foo)

CICLO_CHOICES = (('','Ambos'),(1,'Primera'),(2,'Postrera'))

class Consulta(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Consulta, self).__init__(*args, **kwargs)
        self.fields['year'] = forms.ChoiceField(choices=fecha_choice(),required=True,label=u'Años')
        self.fields['municipio'] = forms.ModelMultipleChoiceField(queryset=municipios(), required=False)
        self.fields['comunidad'] = forms.ModelMultipleChoiceField(queryset=Comunidad.objects.all(), required=False)
        self.fields['ciclo'] = forms.ChoiceField(label=u'Ciclo productivo',choices=CICLO_CHOICES,required=False)
        self.fields['rubro'] = forms.ChoiceField(label=u'Rubro',choices=CULTIVO_CHOICES,required=False)
