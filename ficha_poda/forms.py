# -*- coding: utf-8 -*-
from django import forms
from lookups import ProductorLookup, TecnicoLookup
import selectable.forms as selectable
from .models import Ficha

class ProductorAdminForm(forms.ModelForm):

    class Meta(object):
        model = Ficha
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }
