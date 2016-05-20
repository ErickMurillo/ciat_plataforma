# -*- coding: utf-8 -*-
from django import forms
from lookups import ProductorLookup, TecnicoLookup
import selectable.forms as selectable
from .models import FichaSombra, FichaPoda, FichaPlaga, FichaPiso
from mapeo.models import Persona, CHOICE_TIPOLOGIA, CHOICE_SEXO, Organizaciones
from comunicacion.lugar.models import Pais, Departamento, Municipio, Comunidad

class ProductorSombraAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaSombra
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

class TecnicoAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaSombra
        widgets = {
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }


class ProductorPodaAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaPoda
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

class ProductorPlagaAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaPlaga
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }


class ProductorPisoAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaPiso
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

def fecha_choice():
    years = []
    for en in FichaSombra.objects.order_by('fecha_visita').values_list('fecha_visita', flat=True):
        years.append((en.year,en.year))
    return list(sorted(set(years)))

class ConsultaSombraForm(forms.Form):
    fecha = forms.ChoiceField(choices=fecha_choice(), label="Años", required=True)
    organizacion = forms.ModelChoiceField(queryset=Organizaciones.objects.all(), required=False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=False)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required=False)
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), required=False)
    comunidad = forms.ModelChoiceField(queryset=Comunidad.objects.all(), required=False)
    sexo = forms.ChoiceField(choices=CHOICE_SEXO, required=False)
    tipologia = forms.ChoiceField(choices=CHOICE_TIPOLOGIA, required=False)
