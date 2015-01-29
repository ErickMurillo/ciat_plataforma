# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import	*
from django.forms import CheckboxSelectMultiple
from .forms import *
from comunicacion.lugar.models import *


# Register your models here.
class Pregunta_1_Inline(admin.TabularInline):
	model = Pregunta_1
	max_num = 1
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
	extra = 1
	max_num = 20
	can_delete = True


class Pregunta_2_Inline(admin.TabularInline):
	model = Pregunta_2
	extra = 1
	max_num = 4
	can_delete = True

class Pregunta_3_Inline(admin.TabularInline):
	model = Pregunta_3 
	max_num = 1
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_4_Inline(admin.TabularInline):
	model = Pregunta_4
	max_num = 10
	extra = 1
	can_delete = True
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_5a_Inline(admin.TabularInline):
	model = Pregunta_5a
	form = Pregunta_5aForm
	extra = 1
	can_delete = True
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}

	class Media:
		js = ('analisis/js/custom.js',)
	# 	css = {
 #            'all': ('analisis/css/admin.css',)
 #        }

class Pregunta_5c_Inline(admin.TabularInline):
	model = Pregunta_5c
	# form = Pregunta_5cForm
	max_num = 2
	can_delete = False
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'innovacion':
			urlactual=request.get_full_path()
			urlactual=urlactual.split('/')
			if urlactual[4]!='add':
				_identrevista=int(urlactual[4])
				kwargs["queryset"] = Pregunta_5a.objects.filter(prioritizado='1',entrevistado__pk=_identrevista)
			else:
				kwargs["queryset"] = Pregunta_5a.objects.filter(prioritizado='2')	
		return super(Pregunta_5c_Inline, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
class Pregunta_5d_Inline(admin.TabularInline):
	model = Pregunta_5d
	# form = Pregunta_5dForm
	max_num = 2
	extra = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'innovacion':
			urlactual=request.get_full_path()
			urlactual=urlactual.split('/')
			if urlactual[4]!='add':
				_identrevista=int(urlactual[4])
				kwargs["queryset"] = Pregunta_5a.objects.filter(prioritizado='1',entrevistado__pk=_identrevista)
			else:
				kwargs["queryset"] = Pregunta_5a.objects.filter(prioritizado='2')	
		return super(Pregunta_5d_Inline, self).formfield_for_foreignkey(db_field, request, **kwargs)

class Pregunta_5e_Inline(admin.TabularInline):
	model = Pregunta_5e
	# form = Pregunta_5eForm
	max_num = 2
	extra = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'innovacion':
			urlactual=request.get_full_path()
			urlactual=urlactual.split('/')
			if urlactual[4]!='add':
				_identrevista=int(urlactual[4])
				kwargs["queryset"] = Pregunta_5a.objects.filter(prioritizado='1',entrevistado__pk=_identrevista)
			else:
				kwargs["queryset"] = Pregunta_5a.objects.filter(prioritizado='2')	
		return super(Pregunta_5e_Inline, self).formfield_for_foreignkey(db_field, request, **kwargs)

class Pregunta_6a_Inline(admin.TabularInline):
	model = Pregunta_6a
	form = Pregunta_6aForm
	extra = 1
	can_delete = True
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_6c_Inline(admin.TabularInline):
	model = Pregunta_6c
	max_num = 2
	extra = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'innovacion':
			urlactual=request.get_full_path()
			urlactual=urlactual.split('/')
			if urlactual[4]!='add':
				_identrevista=int(urlactual[4])
				kwargs["queryset"] = Pregunta_6a.objects.filter(prioritizado='1',entrevistado__pk=_identrevista)
			else:
				kwargs["queryset"] = Pregunta_6a.objects.filter(prioritizado='2')	
		return super(Pregunta_6c_Inline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class Pregunta_6d_Inline(admin.TabularInline):
	model = Pregunta_6d
	max_num = 2
	extra = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'innovacion':
			urlactual=request.get_full_path()
			urlactual=urlactual.split('/')
			if urlactual[4]!='add':
				_identrevista=int(urlactual[4])
				kwargs["queryset"] = Pregunta_6a.objects.filter(prioritizado='1',entrevistado__pk=_identrevista)
			else:
				kwargs["queryset"] = Pregunta_6a.objects.filter(prioritizado='2')	
		return super(Pregunta_6d_Inline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class Pregunta_6e_Inline(admin.TabularInline):
	model = Pregunta_6e
	max_num = 2
	extra = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }	

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'innovacion':
			urlactual=request.get_full_path()
			urlactual=urlactual.split('/')
			if urlactual[4]!='add':
				_identrevista=int(urlactual[4])
				kwargs["queryset"] = Pregunta_6a.objects.filter(prioritizado='1',entrevistado__pk=_identrevista)
			else:
				kwargs["queryset"] = Pregunta_6a.objects.filter(prioritizado='2')	
		return super(Pregunta_6e_Inline, self).formfield_for_foreignkey(db_field, request, **kwargs)

class Pregunta_7a_Inline(admin.TabularInline):
	model = Pregunta_7a
	extra = 1
	max_num = 10
	can_delete = True
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_7b_Inline(admin.TabularInline):
	model = Pregunta_7b
	max_num = 1
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }	

class Pregunta_8_Inline(admin.TabularInline):
	model = Pregunta_8
	max_num = 10
	extra = 1
	can_delete = True
	fields = (('organizacion','territorio'),('periodo','profundidad'),('tema'))	
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_9_Inline(admin.TabularInline):
	model = Pregunta_9
	extra = 7
	max_num = 7
	can_delete = False
	# fieldsets = [
	# 	(None, {'fields' : ('tema','prioridad','papel')}),
	# 	('Auto-evaluación de la capacidad de la organización', {'fields' : ('conocimiento','experiencia')}),
	# ]

class Pregunta_11_Inline(admin.TabularInline):
	model = Pregunta_11
	extra = 7
	max_num = 7
	can_delete = False

class EntrevistaAdmin(admin.ModelAdmin):
	fieldsets = [
		('Información de la persona entrevistada', {'fields' : (('nombre','posicion','email','organizacion','pais','departamento','telefono'),('fecha','alcance','tipo_estudio'))}),
	]
	inlines = [Pregunta_1_Inline, Pregunta_2_Inline, Pregunta_3_Inline, Pregunta_4_Inline, 
			   Pregunta_5a_Inline, Pregunta_5c_Inline, Pregunta_5d_Inline, Pregunta_5e_Inline,
			   Pregunta_6a_Inline, Pregunta_6c_Inline,Pregunta_6d_Inline,Pregunta_6e_Inline,
			   Pregunta_7a_Inline,Pregunta_7b_Inline,Pregunta_8_Inline,Pregunta_9_Inline,Pregunta_11_Inline]

	def save_model(self, request, obj, form, change):
		instance = form.save(commit=False)
		if instance.id is None:
			instance.usuario = request.user
			instance.save()
		return instance


	def get_queryset(self, request):
		qs = super(EntrevistaAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(usuario=request.user)

admin.site.register(Entrevista,EntrevistaAdmin)

