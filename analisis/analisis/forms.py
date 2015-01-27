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