# -*- coding: utf-8 -*-
from django.contrib import admin
from .forms import ProductorSombraAdminForm, TecnicoAdminForm, ProductorPodaAdminForm, ProductorPlagaAdminForm, ProductorPisoAdminForm
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

class ManejoSombraInline(admin.TabularInline):
    model = ManejoSombra
    extra = 1
    max_num = 1

class FichaSombraAdmin(admin.ModelAdmin):
    form = ProductorSombraAdminForm
    inlines = [Foto1Inline,Punto1Inline,Cobertura1Inline,
                      Foto2Inline,Punto2Inline,Cobertura2Inline,
                      Foto3Inline,Punto3Inline,Cobertura3Inline,
                      AnalisisSombraInline,AccionesSombraInline,
                      ReducirSombraInline,AumentarSombraInline,
                      ManejoSombraInline]
    list_display = ('fecha_visita', 'productor', 'tecnico',)
    search_fields = ('productor__nombre',)
    date_hierarchy = 'fecha_visita'

    class Media:
        css = {
           'all': ('monitoreo/css/adminSombra.css',)
       }
        js = ('monitoreo/js/fichaSombra.js',)

# Register your models here.
admin.site.register(FichaSombra, FichaSombraAdmin)

#--------------------- admin ficha poda ---------------------------

class Punto1AInline(admin.TabularInline):
    model = Punto1A
    extra = 1
    max_num = 2

class Punto1BInline(admin.TabularInline):
    model = Punto1B
    extra = 1
    max_num = 7

class Punto1CInline(admin.TabularInline):
    model = Punto1C
    extra = 1
    max_num = 1

class Punto2AInline(admin.TabularInline):
    model = Punto2A
    extra = 1
    max_num = 2

class Punto2BInline(admin.TabularInline):
    model = Punto2B
    extra = 1
    max_num = 7

class Punto2CInline(admin.TabularInline):
    model = Punto2C
    extra = 1
    max_num = 1

class Punto3AInline(admin.TabularInline):
    model = Punto3A
    extra = 1
    max_num = 2

class Punto3BInline(admin.TabularInline):
    model = Punto3B
    extra = 1
    max_num = 7

class Punto3CInline(admin.TabularInline):
    model = Punto3C
    extra = 1
    max_num = 1

class AnalisisPodaInline(admin.TabularInline):
    model = AnalisisPoda
    extra = 1
    max_num = 1

class ManejoPodaInline(admin.TabularInline):
    model = ManejoPoda
    extra = 1
    max_num = 1

class FichaPodaAdmin(admin.ModelAdmin):
    form = ProductorPodaAdminForm
    inlines = [Punto1AInline, Punto1BInline, Punto1CInline,
                     Punto2AInline, Punto2BInline, Punto2CInline,
                     Punto3AInline, Punto3BInline, Punto3CInline,
                     AnalisisPodaInline, ManejoPodaInline]
    list_display = ('fecha_visita', 'productor', 'tecnico',)
    search_fields = ('productor__nombre',)
    date_hierarchy = 'fecha_visita'

    class Media:
        css = {
           'all': ('monitoreo/css/adminPoda.css',)
       }
        js = ('monitoreo/js/fichaPoda.js',)


# Register your models here.
admin.site.register(FichaPoda, FichaPodaAdmin)


#--------  admin ficha plaga ----------

class PlagasEnfermedadInline(admin.TabularInline):
    model = PlagasEnfermedad
    extra = 1
    max_num = 13

class AccionesEnfermedadInline(admin.TabularInline):
    model = AccionesEnfermedad
    extra = 1
    max_num = 9

class OrientacionInline(admin.TabularInline):
    model = Orientacion
    extra = 1
    max_num = 1

class ObservacionPunto1Inline(admin.TabularInline):
    model = ObservacionPunto1
    extra = 1
    max_num = 13

class ObservacionPunto1NivelInline(admin.TabularInline):
    model = ObservacionPunto1Nivel
    extra = 1
    max_num = 1

class ObservacionPunto2Inline(admin.TabularInline):
    model = ObservacionPunto2
    extra = 1
    max_num = 13

class ObservacionPunto2NivelInline(admin.TabularInline):
    model = ObservacionPunto2Nivel
    extra = 1
    max_num = 1

class ObservacionPunto3Inline(admin.TabularInline):
    model = ObservacionPunto3
    extra = 1
    max_num = 13

class ObservacionPunto3NivelInline(admin.TabularInline):
    model = ObservacionPunto3Nivel
    extra = 1
    max_num = 1

class ProblemasPrincipalesInline(admin.TabularInline):
    model = ProblemasPrincipales
    extra = 1
    max_num = 1

class Punto6PlagasInline(admin.TabularInline):
    model = Punto6Plagas
    extra = 1
    max_num = 1

class Punto7PlagasInline(admin.TabularInline):
    model = Punto7Plagas
    extra = 1
    max_num = 9

class Punto8y9PlagasInline(admin.TabularInline):
    model = Punto8y9Plagas
    extra = 1
    max_num = 1

class FichaPlagaAdmin(admin.ModelAdmin):
    form = ProductorPlagaAdminForm
    inlines = [PlagasEnfermedadInline,AccionesEnfermedadInline,OrientacionInline,
                ObservacionPunto1Inline,ObservacionPunto1NivelInline,
                ObservacionPunto2Inline,ObservacionPunto2NivelInline,
                ObservacionPunto3Inline,ObservacionPunto3NivelInline,
                ProblemasPrincipalesInline,Punto6PlagasInline,Punto7PlagasInline,
                Punto8y9PlagasInline]
    list_display = ('fecha_visita', 'productor', 'tecnico',)
    search_fields = ('productor__nombre',)
    date_hierarchy = 'fecha_visita'

    class Media:
        css = {
           'all': ('monitoreo/css/adminPlaga.css',)
       }
        js = ('monitoreo/js/fichaPlaga.js',)

admin.site.register(FichaPlaga, FichaPlagaAdmin)

# ----------------- ficha piso -------------------------------

class PisoPunto1Inline(admin.TabularInline):
    model = PisoPunto1
    extra = 1
    max_num = 1

class PisoPunto3Inline(admin.TabularInline):
    model = PisoPunto3
    extra = 1
    max_num = 8

class PisoPunto4Inline(admin.TabularInline):
    model = PisoPunto4
    extra = 1
    max_num = 1

class PisoPunto5Inline(admin.TabularInline):
    model = PisoPunto5
    extra = 1
    max_num = 13

class PisoPunto6Inline(admin.TabularInline):
    model = PisoPunto6
    extra = 1
    max_num = 1

class PisoPunto7Inline(admin.TabularInline):
    model = PisoPunto7
    extra = 1
    max_num = 1

class PisoPunto8Inline(admin.TabularInline):
    model = PisoPunto8
    extra = 1
    max_num = 8

class PisoPunto10Inline(admin.TabularInline):
    model = PisoPunto10
    extra = 1
    max_num = 1


class FichaPisoAdmin(admin.ModelAdmin):
    form = ProductorPisoAdminForm
    inlines = [PisoPunto1Inline,PisoPunto3Inline,PisoPunto4Inline, PisoPunto5Inline,
                PisoPunto6Inline,PisoPunto7Inline,PisoPunto8Inline,PisoPunto10Inline]
    list_display = ('fecha_visita', 'productor', 'tecnico',)
    search_fields = ('productor__nombre',)
    date_hierarchy = 'fecha_visita'

    class Media:
        css = {
           'all': ('monitoreo/css/adminPiso.css',)
       }
        js = ('monitoreo/js/fichaPiso.js',)

admin.site.register(FichaPiso, FichaPisoAdmin)

class EspeciesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('nombre', 'tipo', 'foto' )
        }),
        ('PEQUEÑO', {
            'classes': ('collapse',),
            'fields': ('p_altura', 'p_diametro', 'p_ancho'),
        }),
        ('MEDIANO', {
            'classes': ('collapse',),
            'fields': ('m_altura', 'm_diametro', 'm_ancho'),
        }),
        ('GRANDE', {
            'classes': ('collapse',),
            'fields': ('g_altura', 'g_diametro', 'g_ancho'),
        }),
    )


admin.site.register(Especies, EspeciesAdmin)
