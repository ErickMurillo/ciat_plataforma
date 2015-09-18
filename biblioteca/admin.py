from django.contrib import admin
from .models import Biblioteca, ArchivoAdjunto

class InlineArchivoAdjunto(admin.TabularInline):
    model = ArchivoAdjunto
    extra = 1

class AdminBiblioteca(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    exclude = ('user',)
    inlines = [InlineArchivoAdjunto]
    filter_horizontal = ("proyecto","alianza","temas")
    list_display = ('titulo','autor', 'descripcion', 'fecha')
    list_filter = ('fecha','user')
    search_fields = ('titulo','autor','descripcion')

# Register your models here.
admin.site.register(Biblioteca, AdminBiblioteca)
