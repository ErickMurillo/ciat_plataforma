# -*- coding: UTF-8 -*-

from django.db import models
from models import *
from django import forms
from django.forms import ModelForm

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
