from django.contrib import admin
from .models import	*

class Producto_ProcesoAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','url')

# Register your models here.
admin.site.register(Producto_Proceso,Producto_ProcesoAdmin)


