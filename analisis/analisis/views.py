# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import *
from mapeo.models import *
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
class IndexView(ListView):
	template_name = 'analisis/index.html'
	model = Sector

	def get_context_data(self,**kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		contador_org = Organizaciones.objects.count()

		sector = {}
		for x in Sector.objects.all():
			cont_org = Organizaciones.objects.filter(sector=x).count()
			sector[x.nombre] = cont_org
		context['contador_sector'] = sector

		tema = {}
		for y in Tema.objects.all():
			contador_pregunta1 = Pregunta_1.objects.filter(tema=y).count()
			tema[y.tema] = contador_pregunta1
		context['contador_tematica'] = tema
		
		prueba = {}
		for i in Sector.objects.all():
			conteo = Pregunta_1.objects.filter(entrevistado__organizacion__sector=i).count()
			prueba[i.nombre] = conteo
		context['proyectos'] = prueba
			
		impactos = {}
		for imp in Sector.objects.all():
			preg_4 = Pregunta_4.objects.filter(entrevistado__organizacion__sector=imp).count()
			impactos[imp.nombre] = preg_4
		context['impacto'] = impactos

		preg_4_tema = {}
		for y in Tema.objects.all():
			contador_pregunta4 = Pregunta_4.objects.filter(tema=y).count()
			preg_4_tema[y.tema] = contador_pregunta4
		context['impactos_tematica'] = preg_4_tema

		innocacion = {}
		for inno in Sector.objects.all():
			contador_pregunta5 = Pregunta_5a.objects.filter(entrevistado__organizacion__sector=inno).count()
			innocacion[inno.nombre] = contador_pregunta5
		context['innovacion_contador']  = innocacion

		tematica_innovacion = {}
		for ti in Tema.objects.all():
			contador_tematica_5a = Pregunta_5a.objects.filter(tema=ti).count()
			tematica_innovacion[ti.tema] = contador_tematica_5a
		context['tematica_innovacion_5a'] = tematica_innovacion

		return context

class BusquedaPaisView(TemplateView):
	 
	def get(self, request, *args, **kwargs):
		id_pais = request.GET['id']
		departamento = Departamento.objects.filter(pais__id=id_pais)
		data = serializers.serialize('json',departamento,fields=('nombre',))
		return HttpResponse(data,mimetype='application/json')
