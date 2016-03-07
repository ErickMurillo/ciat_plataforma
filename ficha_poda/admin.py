from django.contrib import admin
from .models import Ficha, AnalisisPoda, Punto1A, Punto1B, Punto1C, Punto2A, Punto2B, Punto2C, Punto3A, Punto3B, Punto3C
from .forms import ProductorAdminForm

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


class FichaAdmin(admin.ModelAdmin):
    form = ProductorAdminForm
    inlines = [Punto1AInline, Punto1BInline, Punto1CInline,
                     Punto2AInline, Punto2BInline, Punto2CInline,
                     Punto3AInline, Punto3BInline, Punto3CInline,
                     AnalisisPodaInline]
    list_display = ('fecha_visita', 'productor', 'tecnico',)
    search_fields = ('productor__nombre',)
    date_hierarchy = 'fecha_visita'

    class Media:
        css = {
           'all': ('monitoreo/css/adminPoda.css',)
       }
        js = ('monitoreo/js/fichaPoda.js',)


# Register your models here.
admin.site.register(Ficha, FichaAdmin)
