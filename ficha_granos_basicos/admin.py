from django.contrib import admin
from .models import *

# ficha registro de gastos ------------------------------------------------
class InlineTablaGastos(admin.TabularInline):
    model = TablaGastos
    extra = 1

class GastosAdmin(admin.ModelAdmin):
    list_display = ('productor', 'fecha_siembra', 'rubro')

    inlines = [InlineTablaGastos]

admin.site.register(Gastos,GastosAdmin)

#ficha Toma de decisiones --------------------------------------------------
class InlineTablaDecisiones(admin.TabularInline):
    model = TablaDecisiones
    extra = 1

class TomaDecisionesAdmin(admin.ModelAdmin):
    list_display = ('productor',)

    inlines = [InlineTablaDecisiones]

admin.site.register(TomaDecisiones,TomaDecisionesAdmin)

#ficha monitoreo #1 ---------------------------------------------------------
class InlineDatosParcela(admin.TabularInline):
    model = DatosParcela
    extra = 1

class InlineDistribucionPendiente(admin.TabularInline):
    model = DistribucionPendiente
    max_num = 2
    extra = 1

class InlineRecursosSiembra(admin.TabularInline):
    model = RecursosSiembra
    extra = 1
    max_num = 2

class InlineHistorialRendimiento(admin.TabularInline):
    model = HistorialRendimiento
    extra = 1

class DatosMonitoreoAdmin(admin.ModelAdmin):
    list_display = ('productor','ciclo_productivo','cultivo')

    inlines = [InlineDatosParcela,InlineDistribucionPendiente,
                InlineRecursosSiembra,InlineHistorialRendimiento]

admin.site.register(DatosMonitoreo,DatosMonitoreoAdmin)
