# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import	*
from django.forms import CheckboxSelectMultiple
from .forms import Pregunta_5aForm


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

class Pregunta_2_Inline(admin.TabularInline):
	model = Pregunta_2
	extra = 1
	max_num = 4

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
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_5a_Inline(admin.TabularInline):
	model = Pregunta_5a
	form = Pregunta_5aForm
	max_num = 10
	extra = 1
	can_delete = False
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}

	# class Media:
	# 	js = ('analisis/js/custom.js',)
	# 	css = {
 #            'all': ('analisis/css/admin.css',)
 #        }

class Pregunta_5c_Inline(admin.TabularInline):
	model = Pregunta_5c
	max_num = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
	
class Pregunta_5d_Inline(admin.TabularInline):
	model = Pregunta_5d
	max_num = 2
	extra = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_5e_Inline(admin.TabularInline):
	model = Pregunta_5e
	max_num = 2
	extra = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Pregunta_6a_Inline(admin.TabularInline):
	model = Pregunta_6a
	max_num = 10
	extra = 1
	can_delete = False
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

class Pregunta_6d_Inline(admin.TabularInline):
	model = Pregunta_6d
	max_num = 2
	extra = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class Pregunta_6e_Inline(admin.TabularInline):
	model = Pregunta_6e
	max_num = 2
	extra = 2
	can_delete = False
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }	

class Pregunta_7a_Inline(admin.TabularInline):
	model = Pregunta_7a
	extra = 1
	max_num = 10
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
	can_delete = False
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
		('Información de la persona entrevistada', {'fields' : (('nombre','posicion','email','organizacion','departamento','telefono'),('fecha','alcance','tipo_estudio'))}),
	]
	inlines = [Pregunta_1_Inline, Pregunta_2_Inline, Pregunta_3_Inline, Pregunta_4_Inline, 
			   Pregunta_5a_Inline, Pregunta_5c_Inline, Pregunta_5d_Inline, Pregunta_5e_Inline,
			   Pregunta_6a_Inline, Pregunta_6c_Inline,Pregunta_6d_Inline,Pregunta_6e_Inline,
			   Pregunta_7a_Inline,Pregunta_7b_Inline,Pregunta_8_Inline,Pregunta_9_Inline,Pregunta_11_Inline]

admin.site.register(Entrevista,EntrevistaAdmin)

