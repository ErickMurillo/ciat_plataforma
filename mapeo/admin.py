from django.contrib import admin
from .models import *


class OrganizacionesAdmin(admin.ModelAdmin):
	list_display = ('id','siglas','nombre','area_accion','sitio_accion','plataforma','sector')
	list_display_links = ('id','siglas','nombre')


class ProyectosAdmin(admin.ModelAdmin):
	filter_horizontal = ("alianza","influencia","socias")
	list_display = ('nombre', 'corto', 'codigo', 'inicio', 'finalizacion')

class InlineProductor(admin.TabularInline):
	model = Productor
	extra = 1

class InlineLideres(admin.TabularInline):
	model = Lideres
	extra = 1

class InlineTecnicoEspInvestigador(admin.TabularInline):
	model = TecnicoEspInvestigador
	extra = 1

class InlineDecisor(admin.TabularInline):
	model = Decisor
	extra = 1

class PersonaAdmin(admin.ModelAdmin):
	list_display = ('tipo_persona', 'nombre', 'sexo', 'pais')

	inlines = [InlineProductor, InlineLideres, InlineTecnicoEspInvestigador,
				InlineDecisor]

	class Media:
		js = ('/static/general/js/personaAdmin.js',)


# Register your models here.
admin.site.register(Organizaciones, OrganizacionesAdmin)
admin.site.register(Persona, PersonaAdmin)
#modelos utilitarios
admin.site.register(Proyectos, ProyectosAdmin)
admin.site.register(RubrosAgropecuarios)
admin.site.register(RubrosNoAgropecuarios)
admin.site.register(FuenteManoObra)
admin.site.register(FormaAtencion)
admin.site.register(Especialidades)
admin.site.register(Accionar)
admin.site.register(CampoAccion)
