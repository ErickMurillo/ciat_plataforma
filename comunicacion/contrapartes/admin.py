from django.contrib import admin
from models import *
from comunicacion.contrapartes.forms import *

class ContraparteAdmin(admin.ModelAdmin):
	form = ContraparteForms

admin.site.register(Pais)
admin.site.register(UserProfile)
admin.site.register(Mensajero)