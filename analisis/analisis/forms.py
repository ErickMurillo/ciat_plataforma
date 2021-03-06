# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms
from django.forms import ModelForm
from ajax_select import make_ajax_field
from comunicacion.lugar.models import Pais
from analisis.configuracion.models import SitioAccion, Tipo_Estudio

class Pregunta_5aForm(forms.ModelForm):
    #prioritizado = forms.IntegerField(widget=forms.Select(attrs={'class':'select-evt'}))

    class Meta:
        model = Pregunta_5a
        widgets = {'prioritizado': forms.Select(attrs={'class':'select-evt'})}


class Pregunta_6aForm(forms.ModelForm):

    class Meta:
        model = Pregunta_6a
        widgets = {'prioritizado': forms.Select(attrs={'class':'select-evt'})}

def fecha_choice():
    years = []
    for en in Entrevista.objects.order_by('fecha1').values_list('fecha1', flat=True):
        years.append((en,en))
    return list(sorted(set(years)))

class EntrevistaConsulta(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(EntrevistaConsulta, self).__init__(*args, **kwargs)
        self.fields['fecha'] = forms.MultipleChoiceField(choices=fecha_choice(),required=True,label=u'Fecha')

        self.fields['area_accion'] = forms.ModelChoiceField(queryset=AreaAccion.objects.order_by('nombre'), 
                                      required=False, 
                                      label=u'Área de acción')
        self.fields['sitio_accion'] = forms.ModelChoiceField(queryset=SitioAccion.objects.order_by('nombre'), 
                                      required=False, 
                                      label=u'Sitio de acción')
        self.fields['tipo_estudio'] = forms.ModelChoiceField(queryset=Tipo_Estudio.objects.order_by('nombre'), 
                                      required=False, 
                                      label=u'Tipo de estudio')
        self.fields['plataforma'] = forms.ModelChoiceField(queryset=Plataforma.objects.exclude(id=8).order_by('nombre'), 
                                      required=False, 
                                      label=u'Plataforma')




