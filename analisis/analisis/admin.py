# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import	*
from django.forms import CheckboxSelectMultiple
from .forms import *
from comunicacion.lugar.models import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from django.utils.translation import ugettext_lazy as _

# Register your models here.
class Pregunta_1_Inline(NestedTabularInline):
	model = Pregunta_1
	can_delete = False
	extra = 1
	can_delete = True
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

	def formfield_for_manytomany(self, db_field, request, **kwargs):
		urlactual=request.get_full_path()
		urlactual=urlactual.split('/')
		if urlactual[4]!='add':
			_identrevista=int(urlactual[4])
			try:
				a = Entrevista.objects.get(id=_identrevista)

				if db_field.name == 'ubicacion':	
					kwargs["queryset"] = Municipio.objects.filter(departamento__id__in=[x.id for x in a.departamento.all()])
			except Exception, e:
				pass
		else:
			kwargs["queryset"] = Municipio.objects.filter(departamento__id='0')
		
		return super(Pregunta_1_Inline, self).formfield_for_manytomany(db_field, request, **kwargs)
	


class Pregunta_2_Inline(NestedTabularInline):
	model = Pregunta_2
	extra = 1
	max_num = 4
	can_delete = True

class Pregunta_3_Inline(NestedTabularInline):
	model = Pregunta_3 
	max_num = 1
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_4_Inline(NestedTabularInline):
	model = Pregunta_4
	extra = 1
	can_delete = True
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_5a_Inline(NestedTabularInline):
	model = Pregunta_5a
	form = Pregunta_5aForm
	extra = 1
	can_delete = True
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}

	def formfield_for_manytomany(self, db_field, request, **kwargs):
		urlactual=request.get_full_path()
		urlactual=urlactual.split('/')
		if urlactual[4]!='add':
			_identrevista=int(urlactual[4])
			try:
				a = Entrevista.objects.get(id=_identrevista)
				if db_field.name == 'ubicacion':	
					kwargs["queryset"] = Municipio.objects.filter(departamento__id__in=[x.id for x in a.departamento.all()])
			except Exception, e:
				pass
		else:
			kwargs["queryset"] = Municipio.objects.filter(departamento__id='0')
		
		return super(Pregunta_5a_Inline, self).formfield_for_manytomany(db_field, request, **kwargs)
	

	class Media:
		js = ('analisis/js/custom.js',)
		css = {
            'all': ('analisis/css/admin.css',)
        }
class Pregunta_5c_nestedInline(NestedTabularInline):
	model = Pregunta_5c_nested
	extra = 1
	max_num = 5
	fk_name = 'pregunta_5c'
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}

class Pregunta_5c_Inline(NestedTabularInline):
	model = Pregunta_5c
	inlines = [Pregunta_5c_nestedInline]
	# form = Pregunta_5cForm
	max_num = 2
	can_delete = False
	

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


class Pregunta_5d_Inline(NestedTabularInline):
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

class Pregunta_5e_Inline(NestedTabularInline):
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

class Pregunta_6a_Inline(NestedTabularInline):
	model = Pregunta_6a
	form = Pregunta_6aForm
	extra = 1
	can_delete = True
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

	def formfield_for_manytomany(self, db_field, request, **kwargs):
		urlactual=request.get_full_path()
		urlactual=urlactual.split('/')
		if urlactual[4]!='add':
			_identrevista=int(urlactual[4])
			try:
				a = Entrevista.objects.get(id=_identrevista)
				if db_field.name == 'ubicacion':	
					kwargs["queryset"] = Municipio.objects.filter(departamento__id__in=[x.id for x in a.departamento.all()])
			except Exception, e:
				pass
		else:
			kwargs["queryset"] = Municipio.objects.filter(departamento__id='0')
		
		return super(Pregunta_6a_Inline, self).formfield_for_manytomany(db_field, request, **kwargs)
	
class Pregunta_6c_nestedInline(NestedTabularInline):
	model = Pregunta_6c_nested
	extra = 1
	max_num = 5
	fk_name = 'pregunta_6c'
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}

class Pregunta_6c_Inline(NestedTabularInline):
	model = Pregunta_6c
	inlines = [Pregunta_6c_nestedInline]
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


class Pregunta_6d_Inline(NestedTabularInline):
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


class Pregunta_6e_Inline(NestedTabularInline):
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

class Pregunta_7a_Inline(NestedTabularInline):
	model = Pregunta_7a
	extra = 1
	can_delete = True
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

	def formfield_for_manytomany(self, db_field, request, **kwargs):
		urlactual=request.get_full_path()
		urlactual=urlactual.split('/')
		if urlactual[4]!='add':
			_identrevista=int(urlactual[4])
			try:
				a = Entrevista.objects.get(id=_identrevista)
				if db_field.name == 'ubicacion':	
					kwargs["queryset"] = Municipio.objects.filter(departamento__id__in=[x.id for x in a.departamento.all()])
			except Exception, e:
				pass
		else:
			kwargs["queryset"] = Municipio.objects.filter(departamento__id='0')
		
		return super(Pregunta_7a_Inline, self).formfield_for_manytomany(db_field, request, **kwargs)

class Pregunta_7b_Inline(NestedTabularInline):
	model = Pregunta_7b
	max_num = 1
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }	

class Pregunta_8_Inline(NestedTabularInline):
	model = Pregunta_8
	extra = 1
	can_delete = True
	fields = (('organizacion','territorio1'),('periodo1','profundidad1'),('tema'))	
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_9_Inline(NestedTabularInline):
	model = Pregunta_9
	extra = 7
	max_num = 7
	can_delete = False
	# fieldsets = [
	# 	(None, {'fields' : ('tema','prioridad','papel')}),
	# 	('Auto-evaluación de la capacidad de la organización', {'fields' : ('conocimiento','experiencia')}),
	# ]

class Pregunta_11_Inline(NestedTabularInline):
	model = Pregunta_11
	extra = 7
	max_num = 7
	can_delete = False

class EntrevistaAdmin(NestedModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Entrevista.objects.all()
		return Entrevista.objects.filter(usuario=request.user)

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

	exclude = ('usuario',)
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
	fieldsets = [
		(_('Informacion de la persona entrevistada'), {'fields' : (('nombre','posicion','email','organizacion','pais','departamento','telefono'),('fecha1','alcance1','tipo_estudio',))}),
	]
	inlines = [Pregunta_1_Inline, Pregunta_2_Inline, Pregunta_3_Inline, Pregunta_4_Inline, 
			   Pregunta_5a_Inline, Pregunta_5c_Inline, Pregunta_5d_Inline, Pregunta_5e_Inline,
			   Pregunta_6a_Inline, Pregunta_6c_Inline,Pregunta_6d_Inline,Pregunta_6e_Inline,
			   Pregunta_7a_Inline,Pregunta_7b_Inline,Pregunta_8_Inline,Pregunta_9_Inline,Pregunta_11_Inline]


	# def formfield_for_manytomany(self, db_field, request, **kwargs):
	# 	urlactual=request.get_full_path()
	# 	urlactual=urlactual.split('/')
	# 	if urlactual[4]=='add':
	# 		kwargs["queryset"] = Departamento.objects.filter(pais='0')
	# 	return super(EntrevistaAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


	def formfield_for_manytomany(self, db_field, request, **kwargs):
		urlactual=request.get_full_path()
		urlactual=urlactual.split('/')
		if urlactual[4]!='add':
			_identrevista=int(urlactual[4])
			try:
				a = Entrevista.objects.get(id=_identrevista)
				if db_field.name == 'departamento':	
					kwargs["queryset"] = Departamento.objects.filter(pais=a.pais)
			except Exception, e:
				pass
		return super(EntrevistaAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)	
		# else:
		# 	kwargs["queryset"] = Departamento.objects.filter(pais='0')
			

admin.site.register(Entrevista,EntrevistaAdmin)

