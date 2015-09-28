# -*- coding: UTF-8 -*-

from django import forms
from mapeo.models import Temas

class BibliotecaConsulta(forms.Form):
	q = forms.CharField()
	temas = forms.ModelChoiceField(queryset=Temas.objects.order_by('nombre'),
                                  required=False)