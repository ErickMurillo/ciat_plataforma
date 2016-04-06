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
class InlineDatosParcela(admin.StackedInline):
    model = DatosParcela
    max_num = 1
    can_delete = False

    fields = (
            ('nombre', 'edad_parcela'),
            ('latitud', 'longitud', 'direccion_viento'),
            ('percepcion_fertilidad','tamano_parcela','profundidad_capa'),
            ('acceso_agua', 'fuente_agua', 'distancia'),
        )

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

    fields = (
            ('productor', 'fecha', 'visita'),
            ('areas','ciclo_productivo','cultivo'),
            ('fecha_siembra', 'fecha_cosecha'),
        )

admin.site.register(DatosMonitoreo,DatosMonitoreoAdmin)

#siembra --------------------------------------------------------------------
class InlineNombreSemilla(admin.TabularInline):
    model = NombreSemilla
    extra = 1
    max_num = 2

class InlineProcedenciaSemilla(admin.TabularInline):
    model = ProcedenciaSemilla
    extra = 1
    max_num = 2

class InlinePruebaGerminacion(admin.TabularInline):
    model = PruebaGerminacion
    extra = 1
    max_num = 2

class SemillasAdmin(admin.ModelAdmin):
    list_display = ('productor','fecha','visita')

    inlines = [InlineNombreSemilla,InlineProcedenciaSemilla,
                InlinePruebaGerminacion]

    fields = (
            ('productor', 'fecha', 'visita'),
            ('areas','semilla_frijol','semilla_maiz'),
        )

admin.site.register(Semillas,SemillasAdmin)

#suelo ----------------------------------------------------------------------
class InlineTablaSuelo(admin.TabularInline):
    model = TablaSuelo
    extra = 1
    max_num = 21

class SueloAdmin(admin.ModelAdmin):
    list_display = ('productor','fecha','visita')

    inlines = [InlineTablaSuelo]

admin.site.register(Suelo,SueloAdmin)
admin.site.register(ParametrosSuelo)

#macrofauna ---------------------------------------------------------------
class InlineTablaMacrofauna(admin.TabularInline):
    model = TablaMacrofauna
    extra = 1

class MacrofaunaAdmin(admin.ModelAdmin):
    list_display = ('productor','fecha','visita')

    inlines = [InlineTablaMacrofauna]

admin.site.register(Macrofauna,MacrofaunaAdmin)
