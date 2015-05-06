# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms
from django.forms import ModelForm
from ajax_select import make_ajax_field
from comunicacion.lugar.models import Pais
from analysis.configuration.models import SitioAccion, Tipo_Estudio

class Pregunta_5aForm(forms.ModelForm):
    #prioritizado = forms.IntegerField(widget=forms.Select(attrs={'class':'select-evt'}))

    class Meta:
    	model = Pregunta_5a
    	widgets = {'prioritizado': forms.Select(attrs={'class':'select-evt'})}


class Pregunta_6aForm(forms.ModelForm):

    class Meta:
    	model = Pregunta_6a
    	widgets = {'prioritizado': forms.Select(attrs={'class':'select-evt'})}

    
class EntrevistaConsulta(forms.Form):
    fecha = forms.CharField(required=True, 
                            label=u'Date',
                            widget=forms.Select)
    pais = forms.ModelChoiceField(queryset=Pais.objects.order_by('nombre'), 
								  required=False, 
			                      label=u'Country')
    sitio_accion = forms.ModelChoiceField(queryset=SitioAccion.objects.order_by('nombre'), 
								  required=False, 
			                      label=u'Area Site')
    tipo_estudio = forms.ModelChoiceField(queryset=Tipo_Estudio.objects.order_by('nombre'), 
								  required=False, 
			                      label=u'Type of study')
    plataforma = forms.ModelChoiceField(queryset=Plataforma.objects.order_by('nombre'), 
                                  required=False, 
                                  label=u'Platform')


