# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import *
from mapeo.models import *
from django.core import serializers
from django.http import HttpResponse
from .forms import *
from django.db.models import Count
import json as simplejson

#Inicio del filtro para la consultas del front-end

def _queryset_filtrado(request):
	params = {}
	if 'fecha' in request.session:
		params['fecha1__in'] = request.session['fecha']

	if 'area_accion' in request.session:
		params['organizacion__area_accion'] = request.session['area_accion']

	if 'sitio_accion' in request.session:
		params['organizacion__sitio_accion'] = request.session['sitio_accion']

	if 'tipo_estudio' in request.session:
		params['tipo_estudio'] = request.session['tipo_estudio']

	if 'plataforma' in request.session:
		params['organizacion__plataforma'] = request.session['plataforma']

	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)

	for key in unvalid_keys:
		del params[key]

	return Entrevista.objects.filter(**params)

def inicio(request, template='analysis/inicio.html'):

	if request.method == 'POST':
		mensaje = None
		form = EntrevistaConsulta(request.POST)
		if form.is_valid():
			request.session['fecha'] = form.cleaned_data['fecha']
			request.session['area_accion'] = form.cleaned_data['area_accion']
			request.session['sitio_accion'] = form.cleaned_data['sitio_accion']
			request.session['tipo_estudio'] = form.cleaned_data['tipo_estudio']
			request.session['plataforma'] = form.cleaned_data['plataforma']

			mensaje = "Todas las variables estan correctamente :)"
			request.session['activo'] = True
			centinela = 1
		else:
			centinela = 0   
		   
	else:
		form = EntrevistaConsulta()
		mensaje = "Existen alguno errores"
		centinela = 0
		try:
			del request.session['fecha']
			del request.session['area_accion']
			del request.session['sitio_accion']
			del request.session['tipo_estudio']
		except:
			pass

	return render(request, template, locals())

def output1(request, template="analysis/salida1.html"):
	filtro = _queryset_filtrado(request)

	sectores = {}
	sectores1 = {}
	for x in Sector_en.objects.all():
		cont_organizacion = filtro.filter(organizacion__sector_en=x).distinct('organizacion').count()
		sectores[x.nombre] = cont_organizacion

		cont_organizacion1 = filtro.filter(organizacion__sector_en=x).distinct('organizacion')
		sectores1[x.nombre] = cont_organizacion1
		
	return render(request,template, locals())

def output2(request, template="analysis/salida2.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	proyectos = {}
	valores1 = []
	valores2 = []
	valores3 = []

	for choice in Sector_en.objects.all():
		query = filtro.filter(pregunta_1__entrevistado__organizacion__sector_en=choice)
		cont_organizacion = filtro.filter(organizacion__sector_en=choice).distinct('organizacion').count()

		cont_organizacion1 = filtro.filter(organizacion__sector_en=choice).distinct('organizacion')
		t = []

		for x in cont_organizacion1:
			prueba = Pregunta_1.objects.filter(entrevistado=filtro,entrevistado__organizacion=x.organizacion).count()
			t.append(prueba)

		resultados = query.count()

		if len(t) >= 3:
			mediana = calcular_mediana(t)
		else:
			mediana = '--'

		fila = [choice.nombre,cont_organizacion,resultados,promedio(resultados,cont_organizacion),mediana]

		tabla.append(fila)
		proyectos[choice.nombre] = promedio(resultados,cont_organizacion)

		valores1.append(cont_organizacion)
		valores2.append(resultados)
		valores3.append(float(promedio(resultados,cont_organizacion)))
		
	total1 = sumarLista(valores1)
	total2 = sumarLista(valores2)
	try:
		total3 = total2/float(total1)
	except:
		total3 = 0
		
	return render(request,template, locals())

def output3(request, template="analysis/salida3.html"):
	filtro = _queryset_filtrado(request)
	
	temas = {}
	sectores = {}
	lista_sectores = {}

	for y in Tema.objects.all():
		contador_pregunta1 = Pregunta_1.objects.filter(tema=y, entrevistado=filtro).count()
		temas[y.tema] = contador_pregunta1



	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Tema.objects.all():
			entrevista = Pregunta_1.objects.filter(tema=x, entrevistado=filtro,entrevistado__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		
		lista = []
		for x,y in zx.items():
			lista.append(y)
			
		lista_sectores[z] = lista

	return render(request,template, locals())

def output4(request, template="analysis/salida4.html"):
	filtro = _queryset_filtrado(request)

	impactos = {}
	tabla = []
	valores1 = []
	valores2 = []
	valores3 = []
	
	for imp in Sector_en.objects.all():
		preg_4 = filtro.filter(pregunta_4__entrevistado__organizacion__sector_en=imp).count()
		cont_organizacion = filtro.filter(organizacion__sector_en=imp).distinct('organizacion').count()

		cont_organizacion1 = filtro.filter(organizacion__sector_en=imp).distinct('organizacion')
		lista = []

		for x in cont_organizacion1:
			prueba = Pregunta_4.objects.filter(entrevistado=filtro,entrevistado__organizacion=x.organizacion).count()
			lista.append(prueba)

		if len(lista) >= 3:
			mediana = calcular_mediana(lista)
		else:
			mediana = '--'

		
		fila = [imp.nombre,cont_organizacion,preg_4,promedio(preg_4,cont_organizacion),mediana]

		tabla.append(fila)
		impactos[imp.nombre] = promedio(preg_4,cont_organizacion)

		valores1.append(cont_organizacion)
		valores2.append(preg_4)
		valores3.append(float(promedio(preg_4,cont_organizacion)))
		
	total1 = sumarLista(valores1)
	total2 = sumarLista(valores2)
	try:
		total3 = total2/float(total1)
	except:
		total3 = 0
		
	return render(request,template, locals())


def output5(request, template="analysis/salida5.html"):
	filtro = _queryset_filtrado(request)

	tematicas = {}
	datos = []
	sectores = {}
	lista_sectores = {}
	
	for obj in Tema.objects.all():
		count_impacts = filtro.filter(pregunta_4__tema=obj).count()
		count_projects = filtro.filter(pregunta_1__tema=obj).count()

		fila = [obj.tema,count_projects,count_impacts]
		datos.append(fila)

	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Tema.objects.all():
			entrevista = Pregunta_4.objects.filter(tema=x, entrevistado=filtro,entrevistado__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		for x,y in zx.items():
			lista.append(y)
		lista_sectores[z] = lista

	return render(request, template, locals())

def output5b(request, template="analysis/salida5b.html"):
	filtro = _queryset_filtrado(request)

	beneficiario = {}
	sectores = {}
	lista_sectores = {}

	for obj in Grupo.objects.all():
		count_beneficiario = filtro.filter(pregunta_4__grupo_beneficiario=obj).count()
		beneficiario[obj] = count_beneficiario

	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Grupo.objects.all():
			entrevista = Pregunta_4.objects.filter(grupo_beneficiario=x, entrevistado=filtro,entrevistado__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		for x,y in zx.items():
			lista.append(y)
		lista_sectores[z] = lista

	return render(request, template, locals())

def output6(request, template="analysis/salida6.html"):
	filtro = _queryset_filtrado(request)

	datos = {}
	lista = []
	valores1 = []
	valores2 = []
	valores3 = []

	for obj in Sector_en.objects.all():
		count_organization = filtro.filter(organizacion__sector_en=obj).distinct('organizacion').count()
		count_innovation = filtro.filter(pregunta_5a__entrevistado__organizacion__sector_en=obj).count()

		cont_organizacion1 = filtro.filter(organizacion__sector=obj).distinct('organizacion')
		t = []

		for x in cont_organizacion1:
			prueba = Pregunta_5a.objects.filter(entrevistado=filtro,entrevistado__organizacion=x.organizacion).count()
			t.append(prueba)
			print t

		if len(t) >= 3:
			mediana = calcular_mediana(t)
		else:
			mediana = '--'

		try:
			avg_total = promedio(count_innovation,count_organization)
		except:
			avg_total = 0
		lista.append(count_innovation)

		
		datos[obj] = (count_organization,count_innovation, avg_total, mediana)

		valores1.append(count_organization)
		valores2.append(count_innovation)
		valores3.append(float(promedio(count_innovation,count_organization)))
		
	total1 = sumarLista(valores1)
	total2 = sumarLista(valores2)
	try:
		total3 = total2/float(total1)
	except:
		total3 = 0


	return render(request, template, locals())


def output7(request, template="analysis/salida7.html"):
	filtro = _queryset_filtrado(request)

	datos = {}
	sectores = {}
	lista_sectores = {}

	for obj in Tema.objects.all():
		count_projects = filtro.filter(pregunta_1__tema=obj).count()
		count_tema = filtro.filter(pregunta_5a__tema=obj).count()
		datos[obj] = (count_projects,count_tema)

	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Tema.objects.all():
			entrevista = Pregunta_5a.objects.filter(tema=x, entrevistado=filtro,entrevistado__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		for x,y in zx.items():
			lista.append(y)
		lista_sectores[z] = lista

	return render(request, template, locals())

def output8(request, template="analysis/salida8.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	sectores = {}
	lista_sectores = {}

	for p in Papel.objects.all():
		socio = filtro.filter(pregunta_5c__pregunta_5c_nested__papel_1=p).count()
		prioritizado = Pregunta_5a.objects.filter(entrevistado=filtro,prioritizado='1').count()
		
		try:
			avg_total = promedio(socio,prioritizado)
		except:
			avg_total = 0

		fila = [p.nombre,prioritizado,socio,avg_total]
		tabla.append(fila)

	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Papel.objects.all():
			entrevista = Pregunta_5c.objects.filter(pregunta_5c_nested__papel_1=x, entrevistado=filtro,pregunta_5c_nested__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		for x,y in zx.items():
			lista.append(y)
		lista_sectores[z] = lista

	return render(request,template, locals())

def output9(request, template="analysis/salida9.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	datos = {}
	valores1 = []
	valores2 = []
	valores3 = []

	for x in Sector_en.objects.all():
		cont_organizacion = filtro.filter(organizacion__sector_en=x).distinct('organizacion').count()
		cont_socios = Pregunta_8.objects.filter(entrevistado=filtro,entrevistado__organizacion__sector_en=x).count()
		cont_socios_graf = Pregunta_8.objects.filter(entrevistado=filtro,organizacion__sector_en=x).distinct('organizacion').count()

		cont_organizacion1 = filtro.filter(organizacion__sector_en=x).distinct('organizacion')
		t = []

		for xz in cont_organizacion1:
			prueba = Pregunta_8.objects.filter(entrevistado=filtro,entrevistado__organizacion=xz.organizacion).count()
			t.append(prueba)
			print t

		if len(t) >= 3:
			mediana = calcular_mediana(t)
		else:
			mediana = '--'

		try:
			avg_total = promedio(cont_socios,cont_organizacion)
		except:
			avg_total = 0


		fila = [x,cont_organizacion,cont_socios,avg_total,mediana]
		tabla.append(fila)
		datos[x] = cont_socios_graf

		valores1.append(cont_organizacion)
		valores2.append(cont_socios)
		valores3.append(float(promedio(cont_socios,cont_organizacion)))
		
	total1 = sumarLista(valores1)
	total2 = sumarLista(valores2)
	try:
		total3 = total2/float(total1)
	except:
		total3 = 0

	#salida 11
	sectores = {}
	lista_sectores = {}

	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Sector_en.objects.all():
			entrevista = Pregunta_5c.objects.filter(entrevistado__organizacion__sector_en=x,entrevistado=filtro,pregunta_5c_nested__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		for x,y in zx.items():
			lista.append(y)
		lista_sectores[z] = lista
	return render(request,template, locals())

def output10(request, template="analysis/salida10.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	datos = {}
	datos1 = {}

	for x in Sector_en.objects.all():
		cont_socio_1 = Pregunta_1.objects.filter(entrevistado=filtro,socio__sector_en=x).distinct('socio')
		cont_socio_2 = Pregunta_5a.objects.filter(entrevistado=filtro,socio__sector_en=x).distinct('socio')
		for y in cont_socio_1:
			for z in y.socio.all():
				tabla.append(z)

		for yx in cont_socio_2:
			for zx in y.socio.all():
				tabla.append(zx)
		
		datos[x] = list(set(tabla))
	#salida 12
	sectores = {}
	lista_sectores = {}
	lista_sectores2 = {}

	for y in Sector.objects.all():
		sectores[y] = {}

		for x in Sector.objects.all():
			entrevista = Pregunta_5c.objects.filter(entrevistado__organizacion__sector_en=x,entrevistado=filtro,pregunta_5c_nested__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		lista2 = []
		lista3 = []
		for x,y in zx.items():
			lista.append(y)

		sum_fila = sumarLista(lista)
 
		for i in lista:
			try:
				result = (i/float(sum_fila))*100
			except:
				result = 0.0
			lista2.append((i,result))
			lista3.append(i)

		lista_sectores[z] = (lista2,sum_fila)

		lista_sectores2[z] = lista3

	#sumatoria totales matriz
	mat = []
	for key,value in lista_sectores2.items():
		mat.append(value)

	lista_totales = []
	for x in range(0,len(mat)):
		sumacolumna = 0 
		for y in range(0,len(mat)):
			sumacolumna += mat[y][x]
			
		lista_totales.append((sumacolumna))

	total = sumarLista(lista_totales)
	return render(request,template, locals())

def output11(request, template="analysis/salida11.html"):
	filtro = _queryset_filtrado(request)

	sectores = {}
	lista_sectores = {}

	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Sector_en.objects.all():
			entrevista = Pregunta_5c.objects.filter(entrevistado__organizacion__sector_en=x,entrevistado=filtro,pregunta_5c_nested__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		for x,y in zx.items():
			lista.append(y)
		lista_sectores[z] = lista

	return render(request,template, locals())

def output12(request, template="analysis/salida12.html"):
	filtro = _queryset_filtrado(request)

	sectores = {}
	lista_sectores = {}

	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Sector_en.objects.all():
			entrevista = Pregunta_5c.objects.filter(entrevistado__organizacion__sector_en=x,entrevistado=filtro,pregunta_5c_nested__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		lista2 = []
		for x,y in zx.items():
			lista.append(y)
		asd = sumarLista(lista)
		for i in lista:
			try:
				lista2.append((i/float(asd))*100)
			except:
				lista2.append(0.0)


		lista_sectores[z] = lista2
			
	return render(request,template, locals())

def output13(request, template="analysis/salida13.html"):
	filtro = _queryset_filtrado(request)

	temas = {}
	lista_sectores = {}
	sectores = Sector_en.objects.all()

	for y in Tema.objects.all():
		temas[y] = {}

		for x in Sector.objects.all():
			entrevista = Pregunta_5a.objects.filter(tema=y,entrevistado=filtro,entrevistado__organizacion__sector_en=x).count()
			temas[y][x] = entrevista

	for z,zx in temas.items():
		lista = []
		for x,y in zx.items():
			lista.append(y)
		lista_sectores[z] = (lista,sumarLista(lista))
			
	return render(request,template, locals())


def output14(request, template="analysis/salida14.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	proyectos = {}
	valores1 = []
	valores2 = []
	valores3 = []

	for choice in Sector_en.objects.all():
		innovaciones = filtro.filter(pregunta_6a__entrevistado__organizacion__sector_en=choice).count()
		cont_organizacion = filtro.filter(organizacion__sector_en=choice).distinct('organizacion').count()

		cont_organizacion1 = filtro.filter(organizacion__sector_en=choice).distinct('organizacion')
		t = []

		for x in cont_organizacion1:
			prueba = Pregunta_6c_nested.objects.filter(pregunta_6c__entrevistado=filtro,pregunta_6c__entrevistado__organizacion=x.organizacion).count()
			t.append(prueba)
			print t

		if len(t) >= 3:
			mediana = calcular_mediana(t)
		else:
			mediana = '--'

		fila = [choice.nombre,cont_organizacion,innovaciones,promedio(innovaciones,cont_organizacion),mediana]

		tabla.append(fila)
		proyectos[choice.nombre] = promedio(innovaciones,cont_organizacion)

		valores1.append(cont_organizacion)
		valores2.append(innovaciones)
		valores3.append(float(promedio(innovaciones,cont_organizacion)))
		
	total1 = sumarLista(valores1)
	total2 = sumarLista(valores2)
	try:
		total3 = total2/float(total1)
	except:
		total3 = 0
		
	return render(request,template, locals())

def output15(request, template="analysis/salida15.html"):
	#falta grafica
	filtro = _queryset_filtrado(request)

	temas = {}
	sectores = {}
	lista_sectores = {}  
	
	for y in Tema.objects.all():
		contador_pregunta1 = filtro.filter(pregunta_6a__tema=y).count()
		temas[y.tema] = contador_pregunta1
		
	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Tema.objects.all():
			entrevista = Pregunta_6a.objects.filter(tema=x, entrevistado=filtro,entrevistado__organizacion__sector_en=y).count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		for x,y in zx.items():
			lista.append(y)
		lista_sectores[z] = lista

	return render(request,template, locals())

def output16(request, template="analysis/salida16.html"):
	filtro = _queryset_filtrado(request)

	datos = {}
	grafica = {}
	sectores = {}
	lista_sectores = {} 

	for x in Sector_en.objects.all():
		socio = Pregunta_6c_nested.objects.filter(pregunta_6c__entrevistado=filtro,organizacion__sector_en=x).distinct('organizacion')
		cont_socio = Pregunta_6c_nested.objects.filter(pregunta_6c__entrevistado=filtro,organizacion__sector_en=x).distinct('organizacion').count()
		
		datos[x] = socio
		grafica[x] = cont_socio

	for y in Sector_en.objects.all():
		sectores[y] = {}

		for x in Sector_en.objects.all():
			entrevista = Pregunta_6c_nested.objects.filter(organizacion__sector_en=x,pregunta_6c__entrevistado=filtro,pregunta_6c__entrevistado__organizacion__sector_en=y).distinct('organizacion').count()
			sectores[y][x] = entrevista

	for z,zx in sectores.items():
		lista = []
		for x,y in zx.items():
			lista.append(y)
		lista_sectores[z] = lista
	
	return render(request,template, locals())


def output17(request, template="analysis/salida17.html"):
	filtro = _queryset_filtrado(request)

	sectores = {}
	pregunta_1 = {}
	pregunta_5 = {}
	pregunta_6 = {}
	  

	for y in Sector_en.objects.all():
		org = filtro.filter(organizacion__sector_en=y).distinct('organizacion')
		cont_org = filtro.filter(organizacion__sector_en=y).distinct('organizacion').count()
		
		for x in org:
			project_partners = Pregunta_1.objects.filter(entrevistado=filtro,entrevistado__organizacion=x.organizacion).distinct('socio')
			tabla = []
			for z in project_partners:
				for xc in z.socio.all():
					tabla.append(xc)

			pregunta_1[x.organizacion] = list(set(tabla))
			

			project_partners1 = Pregunta_5c_nested.objects.filter(pregunta_5c__entrevistado=filtro,pregunta_5c__pregunta_5c_nested__pregunta_5c__entrevistado__organizacion=x.organizacion).distinct('organizacion')
			pregunta_5[x.organizacion] = project_partners1

			project_partners2 = Pregunta_6c_nested.objects.filter(pregunta_6c__entrevistado=filtro,pregunta_6c__pregunta_6c_nested__pregunta_6c__entrevistado__organizacion=x.organizacion).distinct('organizacion')
			pregunta_6[x.organizacion] = project_partners2


		sectores[y] = (org,pregunta_1,pregunta_5,pregunta_6,cont_org + 1)
		   

	# for key,value in pregunta_1.items():
	#     print "organizacion:%s " % (key) 
	#     for x in value:
	#         for asd in x.socio.all():
	#              print asd
	

		
	return render(request,template, locals())

def output18(request, template="analysis/salida18.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	valores1 = []
	valores2 = []
	valores3 = []
	cat_fuente = {}

	for choice in Sector_en.objects.all():
		fuentes_aprendizaje = filtro.filter(pregunta_5e__entrevistado__organizacion__sector_en=choice).count()
		cont_organizacion = filtro.filter(organizacion__sector_en=choice).distinct('organizacion').count()

		cont_organizacion1 = filtro.filter(organizacion__sector_en=choice).distinct('organizacion')
		t = []

		for x in cont_organizacion1:
			prueba = Pregunta_5e.objects.filter(entrevistado__organizacion=x.organizacion).count()
			t.append(prueba)
			print t

		if len(t) >= 3:
			mediana = calcular_mediana(t)
		else:
			mediana = '--'

		fila = [choice.nombre,cont_organizacion,fuentes_aprendizaje,promedio(fuentes_aprendizaje,cont_organizacion),mediana]

		tabla.append(fila)

		valores1.append(cont_organizacion)
		valores2.append(fuentes_aprendizaje)
		valores3.append(float(promedio(fuentes_aprendizaje,cont_organizacion)))
		
	total1 = sumarLista(valores1)
	total2 = sumarLista(valores2)
	try:
		total3 = total2/float(total1)
	except:
		total3 = 0

	for x in Categoria_Fuente.objects.all():
		cont_categoria_fuente = filtro.filter(pregunta_5e__categoria_fuente=x).distinct('organizacion').count()

		cat_fuente[x.nombre] = (cont_categoria_fuente)

	return render(request,template, locals())

def output19(request, template="analysis/salida19.html"):
	filtro = _queryset_filtrado(request)

	sectores = {}
	lista_sectores = {} 

	for y in Tema.objects.all():
		sectores[y] = {}

		for x in Categoria.objects.all():
			entrevista = Pregunta_6d.objects.filter(categoria=x,entrevistado=filtro,entrevistado__pregunta_6a__tema=y).distinct('categoria').count()
			sectores[y][x] = entrevista
	
	return render(request,template, locals())

def output20(request, template="analysis/salida20.html"):
	filtro = _queryset_filtrado(request)

	categoria = {}

	for x in Categoria.objects.all():
		cont_categoria = filtro.filter(pregunta_5d__categoria=x).distinct('organizacion').count()
		cont_categoria1 = filtro.filter(pregunta_6d__categoria=x).distinct('organizacion').count()

		categoria[x.nombre] = (cont_categoria,cont_categoria1,x.categoria)
	print categoria

	return render(request,template, locals())

###########################################################################################

# ----------- funciones utilitarias --------

def get_fecha(request):
    years = []
    for en in Entrevista.objects.order_by('fecha1').values_list('fecha1', flat=True):
        years.append((en))
    lista = sorted(set(years))
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')

def sumarLista(lista):
	sum=0
	for i in range(0,len(lista)):
		sum=sum+lista[i]
 
	return sum


def promedio(x,y):
	if y != 0:
		promedio = x/float(y)
	else:
		promedio = 0
	return '%.2f' % promedio


#------- Mediana ------------
def calcular_promedio(lista):
	n = len(lista)
	total_suma = sum(lista)
	try:
		return round(total_suma/n, 2)
	except:
		return 0 

def calcular_mediana(lista):
	n = len(lista)
	lista = sorted(lista)
	
	#calcular si lista es odd or even
	if (n%2) == 1:
		try:
			index = (n+1)/2
		except:
			index = 0
		return lista[index-1]
	else:
		index_1 = (n/2)
		index_2 = index_1+1
		try:
			return calcular_promedio([lista[index_1-1], lista[index_2-1]])
		except:
			return 0

class BusquedaPaisView(TemplateView):
	 
	def get(self, request, *args, **kwargs):
		id_pais = request.GET['id']
		departamento = Departamento.objects.filter(pais__id=id_pais)
		data = serializers.serialize('json',departamento,fields=('nombre',))
		return HttpResponse(data,mimetype='application/json')


def get_fecha(request):
    years = []
    for en in Entrevista.objects.order_by('fecha1').values_list('fecha1', flat=True):
        years.append((en))
    lista = list(sorted(set(years)))
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')

def get_sitio_accion(request):
    ids = request.GET.get('ids', '')
    if ids:
        lista = ids.split(',')
    results = []
    sitios = SitioAccion.objects.filter(area_accion__pk__in=lista).order_by('nombre').values('id', 'nombre')

    return HttpResponse(simplejson.dumps(list(sitios)), content_type='application/json')

def get_plataforma(request):
    ids = request.GET.get('ids', '')
    if ids:
        lista = ids.split(',')
    results = []
    sitios = Plataforma.objects.filter(sitio_accion__pk__in=lista).order_by('nombre').values('id', 'nombre')

    return HttpResponse(simplejson.dumps(list(sitios)), content_type='application/json')