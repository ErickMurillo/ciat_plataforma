from django.contrib import admin
from .models import Organizaciones, Persona

class OrganizacionesAdmin(admin.ModelAdmin):
	list_display = ('id','siglas','nombre','area_accion','sitio_accion','plataforma','sector')
	list_display_links = ('id','siglas','nombre')

# Register your models here.
admin.site.register(Organizaciones, OrganizacionesAdmin)
admin.site.register(Persona)