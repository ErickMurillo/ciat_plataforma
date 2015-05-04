# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import *
from mapeo.models import *
from django.core import serializers
from django.http import HttpResponse
from .forms import *
from django.db.models import Count

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

	if 'plataforma' in request.session:
		params['organizacion__plataforma'] = request.session['plataforma']

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
		# if 'fecha' in request.session:
		# 	del request.session['fecha']
		# 	del request.session['pais']
		# 	del request.session['sitio_accion']
		# 	del request.session['tipo_estudio']
	
	return render(request, template, locals())

def salida1(request, template="analisis/salida1.html"):
	filtro = _queryset_filtrado(request)

	sectores = {}
	sectores1 = {}
	for x in Sector.objects.all():
		cont_organizacion = filtro.filter(organizacion__sector=x).distinct('organizacion').count()
		sectores[x.nombre] = cont_organizacion

		cont_organizacion1 = filtro.filter(organizacion__sector=x).distinct('organizacion')
		sectores1[x.nombre] = cont_organizacion1
		
	return render(request,template, locals())

def salida2(request, template="analisis/salida2.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	proyectos = {}
	valores1 = []
	valores2 = []
	valores3 = []

	for choice in Sector.objects.all():
		query = filtro.filter(pregunta_1__entrevistado__organizacion__sector=choice)
		cont_organizacion = filtro.filter(organizacion__sector=choice).distinct('organizacion').count()

		cont_organizacion1 = filtro.filter(organizacion__sector=choice).distinct('organizacion')
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

def salida3(request, template="analisis/salida3.html"):
	filtro = _queryset_filtrado(request)
	
	temas = {}

	for y in Tema.objects.all():
		contador_pregunta1 = Pregunta_1.objects.filter(tema=y, entrevistado=filtro).count()
		temas[y.tema] = contador_pregunta1


	return render(request,template, locals())

def salida4(request, template="analisis/salida4.html"):
	filtro = _queryset_filtrado(request)

	impactos = {}
	tabla = []
	valores1 = []
	valores2 = []
	valores3 = []
	
	for imp in Sector.objects.all():
		preg_4 = filtro.filter(pregunta_4__entrevistado__organizacion__sector=imp).count()
		cont_organizacion = filtro.filter(organizacion__sector=imp).distinct('organizacion').count()

		cont_organizacion1 = filtro.filter(organizacion__sector=imp).distinct('organizacion')
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


def salida5(request, template="analisis/salida5.html"):
	filtro = _queryset_filtrado(request)

	tematicas = {}
	datos = []
	
	for obj in Tema.objects.all():
		count_impacts = filtro.filter(pregunta_4__tema=obj).count()
		count_projects = filtro.filter(pregunta_1__tema=obj).count()

		fila = [obj.tema,count_projects,count_impacts]
		datos.append(fila)

	return render(request, template, locals())

def salida5b(request, template="analisis/salida5b.html"):
	filtro = _queryset_filtrado(request)

	beneficiario = {}
	for obj in Grupo.objects.all():
		count_beneficiario = filtro.filter(pregunta_4__grupo_beneficiario=obj).count()
		beneficiario[obj] = count_beneficiario


	return render(request, template, locals())

def salida6(request, template="analisis/salida6.html"):
	filtro = _queryset_filtrado(request)

	datos = {}
	lista = []
	valores1 = []
	valores2 = []
	valores3 = []

	for obj in Sector.objects.all():
		count_organization = filtro.filter(organizacion__sector=obj).distinct('organizacion').count()
		count_innovation = filtro.filter(pregunta_5a__entrevistado__organizacion__sector=obj).count()

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


def salida7(request, template="analisis/salida7.html"):
	filtro = _queryset_filtrado(request)

	datos = {}
	for obj in Tema.objects.all():
		count_projects = filtro.filter(pregunta_1__tema=obj).count()
		count_tema = filtro.filter(pregunta_5a__tema=obj).count()
		datos[obj] = (count_projects,count_tema)


	return render(request, template, locals())

def salida8(request, template="analisis/salida8.html"):
	filtro = _queryset_filtrado(request)

	tabla = []

	for p in Papel.objects.all():
		socio = filtro.filter(pregunta_5c__pregunta_5c_nested__papel_1=p).count()
		prioritizado = Pregunta_5a.objects.filter(entrevistado=filtro,prioritizado='1').count()
		
		try:
			avg_total = promedio(socio,prioritizado)
		except:
			avg_total = 0

		fila = [p.nombre,prioritizado,socio,avg_total]
		tabla.append(fila)
	print tabla

	return render(request,template, locals())

def salida9(request, template="analisis/salida9.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	datos = {}
	valores1 = []
	valores2 = []
	valores3 = []

	for x in Sector.objects.all():
		cont_organizacion = filtro.filter(organizacion__sector=x).distinct('organizacion').count()
		cont_socios = Pregunta_8.objects.filter(entrevistado=filtro,entrevistado__organizacion__sector=x).count()

		try:
			avg_total = promedio(cont_socios,cont_organizacion)
		except:
			avg_total = 0

		fila = [x.nombre,cont_organizacion,cont_socios,avg_total]
		tabla.append(fila)
		datos[x.nombre] = avg_total

		valores1.append(cont_organizacion)
		valores2.append(cont_socios)
		valores3.append(float(promedio(cont_socios,cont_organizacion)))
		
	total1 = sumarLista(valores1)
	total2 = sumarLista(valores2)
	try:
		total3 = total2/float(total1)
	except:
		total3 = 0

	return render(request,template, locals())

def salida10(request, template="analisis/salida10.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	datos = {}
	datos1 = {}

	for x in Sector.objects.all():
		cont_socio_1 = Pregunta_1.objects.filter(entrevistado=filtro,socio__sector=x).distinct('socio')
		cont_socio_2 = Pregunta_5a.objects.filter(entrevistado=filtro,socio__sector=x).distinct('socio')
		for y in cont_socio_1:
			for z in y.socio.all():
				tabla.append(z)

		for yx in cont_socio_2:
			for zx in y.socio.all():
				tabla.append(zx)
		
		datos[x] = list(set(tabla))

	return render(request,template, locals())


def salida12(request, template="analisis/salida12.html"):
	filtro = _queryset_filtrado(request)

	sectores = Sector.objects.all()

	datos = {}
	datos2 = {}

	a = filtro.count()

	for x in filtro:
		CONTADOR = 0
		for obj in x.pregunta_5a_set.all():
			for z in obj.socio.all():
				CONTADOR += 1
				print z.sector
			datos[x.organizacion] = CONTADOR
	#print datos		
		#datos[x.organizacion]
			# for z in sectores:
			# 	count = y.filter(socio__sector=z)
			# 	print count
			
			#datos[x.organizacion] = count
	# for y in sectores:
	# 	entrevista = filtro.filter(organizacion__sector=y) 

	# 	for x in entrevista:
	# 		count_preg_5 = Pregunta_5a.objects.filter(socio__sector=x.organizacion.sector).count()
	# 		for z in sectores:
	# 			count_ent = Pregunta_5a.objects.filter(socio__sector=z).count()

	# 			try:
	# 				procentaje = count_preg_5/filtro.count()
	# 			except Exception, e:
	# 				raise
	# 			datos[z] = procentaje


	# for x,y in datos.items():
	# 	print "%s %s" % (x,y) 


	return render(request,template, locals())



def salida14(request, template="analisis/salida14.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	proyectos = {}
	valores1 = []
	valores2 = []
	valores3 = []

	for choice in Sector.objects.all():
		innovaciones = filtro.filter(pregunta_6a__entrevistado__organizacion__sector=choice).count()
		cont_organizacion = filtro.filter(organizacion__sector=choice).distinct('organizacion').count()

		fila = [choice.nombre,cont_organizacion,innovaciones,promedio(innovaciones,cont_organizacion)]

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

def salida15(request, template="analisis/salida15.html"):
	#falta grafica
	filtro = _queryset_filtrado(request)

	temas = {}  
	
	for y in Tema.objects.all():
		contador_pregunta1 = filtro.filter(pregunta_6a__tema=y).count()
		temas[y.tema] = contador_pregunta1
		
	return render(request,template, locals())

def salida16(request, template="analisis/salida16.html"):
	filtro = _queryset_filtrado(request)

	datos = {}
	grafica = {}

	for x in Sector.objects.all():
		socio = Pregunta_6c_nested.objects.filter(pregunta_6c__entrevistado=filtro,organizacion__sector=x).distinct('organizacion')
		cont_socio = Pregunta_6c_nested.objects.filter(pregunta_6c__entrevistado=filtro,organizacion__sector=x).distinct('organizacion').count()
		
		datos[x] = socio
		grafica[x] = cont_socio

	return render(request,template, locals())


def salida17(request, template="analisis/salida17.html"):
	filtro = _queryset_filtrado(request)

	sectores = {}
	pregunta_1 = {}
	pregunta_5 = {}
	pregunta_6 = {}
	  

	for y in Sector.objects.all():
		org = filtro.filter(organizacion__sector=y).distinct('organizacion')
		cont_org = filtro.filter(organizacion__sector=y).distinct('organizacion').count()
		
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

def salida18(request, template="analisis/salida18.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	valores1 = []
	valores2 = []
	valores3 = []
	cat_fuente = {}

	for choice in Sector.objects.all():
		fuentes_aprendizaje = filtro.filter(pregunta_5e__entrevistado__organizacion__sector=choice).count()
		cont_organizacion = filtro.filter(organizacion__sector=choice).distinct('organizacion').count()

		fila = [choice.nombre,cont_organizacion,fuentes_aprendizaje,promedio(fuentes_aprendizaje,cont_organizacion)]

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

def salida20(request, template="analisis/salida20.html"):
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
