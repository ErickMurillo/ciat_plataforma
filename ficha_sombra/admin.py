from django.contrib import admin
from .forms import ProductorAdminForm, TecnicoAdminForm
from .models import *


class Foto1Inline(admin.TabularInline):
    model = Foto1
    extra = 1
    max_num = 1

class Punto1Inline(admin.TabularInline):
    model = Punto1
    extra = 1
    max_num = 12

class Cobertura1Inline(admin.TabularInline):
    model = Cobertura1
    extra = 1
    max_num = 1

#----------------------------------------------------------------

class Foto2Inline(admin.TabularInline):
    model = Foto2
    extra = 1
    max_num = 1

class Punto2Inline(admin.TabularInline):
    model = Punto2
    extra = 1
    max_num = 12

class Cobertura2Inline(admin.TabularInline):
    model = Cobertura2
    extra = 1
    max_num = 1

#----------------------------------------------------------------

class Foto3Inline(admin.TabularInline):
    model = Foto3
    extra = 1
    max_num = 1

class Punto3Inline(admin.TabularInline):
    model = Punto3
    extra = 1
    max_num = 12

class Cobertura3Inline(admin.TabularInline):
    model = Cobertura3
    extra = 1
    max_num = 1

#----------------------------------------

class AnalisisSombraInline(admin.TabularInline):
    model = AnalisisSombra
    extra = 1
    max_num = 1

class AccionesSombraInline(admin.TabularInline):
    model = AccionesSombra
    extra = 1
    max_num = 1

class ReducirSombraInline(admin.TabularInline):
    model = ReducirSombra
    extra = 1
    max_num = 1

class AumentarSombraInline(admin.TabularInline):
    model = AumentarSombra
    extra = 1
    max_num = 1

class ManejoInline(admin.TabularInline):
    model = Manejo
    extra = 1
    max_num = 1

class FichaAdmin(admin.ModelAdmin):
    form = ProductorAdminForm
    inlines = [Foto1Inline,Punto1Inline,Cobertura1Inline,
                      Foto2Inline,Punto2Inline,Cobertura2Inline,
                      Foto3Inline,Punto3Inline,Cobertura3Inline,
                      AnalisisSombraInline,AccionesSombraInline,
                      ReducirSombraInline,AumentarSombraInline,
                      ManejoInline]
    list_display = ('fecha_visita', 'productor', 'tecnico',)
    search_fields = ('productor__nombre',)
    date_hierarchy = 'fecha_visita'

    class Media:
        css = {
           'all': ('monitoreo/css/adminSombra.css',)
       }
        js = ('monitoreo/js/fichaSombra.js',)

# Register your models here.
admin.site.register(Ficha, FichaAdmin)
admin.site.register(Especies)
