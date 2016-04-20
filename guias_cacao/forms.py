# -*- coding: utf-8 -*-
from django import forms
from lookups import ProductorLookup, TecnicoLookup
import selectable.forms as selectable
from .models import FichaSombra, FichaPoda

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
