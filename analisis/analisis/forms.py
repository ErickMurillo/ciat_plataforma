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


# class Pregunta_5cForm(forms.ModelForm):
#     def __init__(self,*args, **kwargs):
#         super(Pregunta_5cForm, self).__init__(*args, **kwargs)
#         self.fields['innovacion'].queryset = Pregunta_5a.objects.filter(prioritizado='1',entrevistado__pk='1')


# class Pregunta_5dForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(Pregunta_5dForm, self).__init__(*args, **kwargs)
#         self.fields['innovacion'].queryset = Pregunta_5a.objects.filter(prioritizado='1')

# class Pregunta_5eForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(Pregunta_5eForm, self).__init__(*args, **kwargs)
#         self.fields['innovacion'].queryset = Pregunta_5a.objects.filter(prioritizado='1')

FECHA_CHOICES = (
					(1,2014),
					(2,2015),
					(3,2016),
					(4,2017),
					(5,2018),
					(6,2019),
					(7,2020),
					(8,2021),
					(9,2022),
					(10,2023),
					(11,2024),
				)

class EntrevistaConsulta(forms.Form):
	fecha = forms.ChoiceField(choices=FECHA_CHOICES)
	pais = forms.ModelChoiceField(queryset=Pais.objects.order_by('-nombre'), 
								  required=False, 
			                      label=u'Pais')
	sitio_accion = forms.ModelChoiceField(queryset=SitioAccion.objects.order_by('-nombre'), 
								  required=False, 
			                      label=u'Sitio de acción')
	tipo_estudio = forms.ModelChoiceField(queryset=Tipo_Estudio.objects.order_by('-nombre'), 
								  required=False, 
			                      label=u'Tipo de estudio')


