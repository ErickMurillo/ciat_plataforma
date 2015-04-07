# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import *
from mapeo.models import *
from django.core import serializers
from django.http import HttpResponse
from .forms import *

#Inicio del filtro para la consultas del front-end

def _queryset_filtrado(request):
    params = {}
    if 'fecha' in request.session:
        params['fecha1'] = request.session['fecha']

    if 'pais' in request.session:
        params['pais'] = request.session['pais']

    if 'sitio_accion' in request.session:
        params['organizacion__sitio_accion'] = request.session['sitio_accion']

    if 'tipo_estudio' in request.session:
        params['tipo_estudio'] = request.session['tipo_estudio']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    return Entrevista.objects.filter(**params)

def inicio(request, template='analisis/inicio.html'):

    if request.method == 'POST':
        mensaje = None
        form = EntrevistaConsulta(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['pais'] = form.cleaned_data['pais']
            request.session['sitio_accion'] = form.cleaned_data['sitio_accion']
            request.session['tipo_estudio'] = form.cleaned_data['tipo_estudio']

            mensaje = "Todas las variables estan correctamente :)"
            request.session['activo'] = True
            centinela = 1
        else:
            centinela = 0   
           
    else:
        form = EntrevistaConsulta()
        mensaje = "Existen alguno errores"
        centinela = 0
        if 'fecha' in request.session:
            del request.session['fecha']
            del request.session['pais']
            del request.session['sitio_accion']
            del request.session['tipo_estudio']
    
    return render(request, template, locals())


class IndexView(ListView):
	# template_name = 'analisis/index.html'
	# model = Sector

	def post(self, request, *args,**kwargs):
		fecha = request.POST['fecha']
		pais = request.POST['pais']
		sitio_accion = request.POST['sitio_accion']
		tipo_estudio = request.POST['tipo_estudio']

		template = 'analisis/index.html'
		
		sectores = {}
		for x in Sector.objects.all():
			cont_organizacion = Organizaciones.objects.filter(sector=x,sitio_accion=sitio_accion,pais=pais,
													 entrevista__tipo_estudio=tipo_estudio,
													 entrevista__fecha1=fecha).count()
			sectores[x.nombre] = cont_organizacion

		sectores1 = {}
		for x in Sector.objects.all():
			cont_organizacion = Organizaciones.objects.filter(sector=x,sitio_accion=sitio_accion,pais=pais)
			sectores1[x.nombre] = cont_organizacion	

	 	temas = {}
		for y in Tema.objects.all():
			contador_pregunta1 = Pregunta_1.objects.filter(tema=y,
														   entrevistado__organizacion__sitio_accion=sitio_accion,
														   entrevistado__organizacion__pais=pais,
														   entrevistado__fecha1=fecha).count()
			temas[y.tema] = contador_pregunta1

		proyectos = {}
		for i in Sector.objects.all():
			conteo = Pregunta_1.objects.filter(entrevistado__organizacion__sector=i,
											   entrevistado__organizacion__sitio_accion=sitio_accion,
											   entrevistado__organizacion__pais=pais,
											   entrevistado__fecha1=fecha).count()
			proyectos[i.nombre] = conteo

		impactos = {}
		for imp in Sector.objects.all():
			preg_4 = Pregunta_4.objects.filter(entrevistado__organizacion__sector=imp,
											   entrevistado__organizacion__sitio_accion=sitio_accion,
											   entrevistado__organizacion__pais=pais,
											   entrevistado__fecha1=fecha).count()
			impactos[imp.nombre] = preg_4


		return render(request, template, locals())

	# def get_context_data(self,**kwargs):
	# 	context = super(IndexView, self).get_context_data(**kwargs)
	# 	contador_org = Organizaciones.objects.count()


	# sector = {}
	# for x in Sector.objects.all():
	# 	cont_org = Organizaciones.objects.filter(sector=x).count()
	# 	sector[x.nombre] = cont_org
	# context['contador_sector'] = sector

	# 	tema = {}
	# 	for y in Tema.objects.all():
	# 		contador_pregunta1 = Pregunta_1.objects.filter(tema=y).count()
	# 		tema[y.tema] = contador_pregunta1
	# 	context['contador_tematica'] = tema
		
	# 	prueba = {}
	# 	for i in Sector.objects.all():
	# 		conteo = Pregunta_1.objects.filter(entrevistado__organizacion__sector=i).count()
	# 		prueba[i.nombre] = conteo
	# 	context['proyectos'] = prueba
			
	# 	impactos = {}
	# 	for imp in Sector.objects.all():
	# 		preg_4 = Pregunta_4.objects.filter(entrevistado__organizacion__sector=imp).count()
	# 		impactos[imp.nombre] = preg_4
	# 	context['impacto'] = impactos

	# 	preg_4_tema = {}
	# 	for y in Tema.objects.all():
	# 		contador_pregunta4 = Pregunta_4.objects.filter(tema=y).count()
	# 		preg_4_tema[y.tema] = contador_pregunta4
	# 	context['impactos_tematica'] = preg_4_tema

	# 	innocacion = {}
	# 	for inno in Sector.objects.all():
	# 		contador_pregunta5 = Pregunta_5a.objects.filter(entrevistado__organizacion__sector=inno).count()
	# 		innocacion[inno.nombre] = contador_pregunta5
	# 	context['innovacion_contador']  = innocacion

	# 	tematica_innovacion = {}
	# 	for ti in Tema.objects.all():
	# 		contador_tematica_5a = Pregunta_5a.objects.filter(tema=ti).count()
	# 		tematica_innovacion[ti.tema] = contador_tematica_5a
	# 	context['tematica_innovacion_5a'] = tematica_innovacion

	# 	return context

   

class BusquedaPaisView(TemplateView):
     
    def get(self, request, *args, **kwargs):
        id_pais = request.GET['id']
        departamento = Departamento.objects.filter(pais__id=id_pais)
        data = serializers.serialize('json',departamento,fields=('nombre',))
        return HttpResponse(data,mimetype='application/json')
