# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from .forms import *
from comunicacion.lugar.models import *
from mapeo.models import *
from django.http import HttpResponse
from django.db.models import Sum, Count, Avg

# Create your views here.
def _queryset_filtrado(request):
	params = {}

	if request.session['year']:
		params['anio'] = request.session['year']

	if request.session['municipio']:
			params['productor__comunidad__municipio__in'] = request.session['municipio']
	else:
		if request.session['comunidad']:
			params['productor__comunidad__in'] = request.session['comunidad']

	if request.session['ciclo']:
		params['ciclo_productivo'] = request.session['ciclo']

	if request.session['rubro']:
		params['datosmonitoreo__cultivo'] = request.session['rubro']


	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)

	for key in unvalid_keys:
		del params[key]

	return Monitoreo.objects.filter(**params)

def consulta(request,template="granos_basicos/consulta.html"):
	if request.method == 'POST':
		mensaje = None
		form = Consulta(request.POST)
		if form.is_valid():
			request.session['year'] = form.cleaned_data['year']
			request.session['municipio'] = form.cleaned_data['municipio']
			request.session['comunidad'] = form.cleaned_data['comunidad']
			request.session['ciclo'] = form.cleaned_data['ciclo']
			request.session['rubro'] = form.cleaned_data['rubro']

			mensaje = "Todas las variables estan correctamente :)"
			request.session['activo'] = True
			centinela = 1


		else:
			centinela = 0

	else:
		form = Consulta()
		mensaje = "Existen alguno errores"
		centinela = 0
		try:
			del request.session['year']
			del request.session['municipio']
			del request.session['comunidad']
			del request.session['ciclo']
			del request.session['rubro']
		except:
			pass

	return render(request, template, locals())

def genero_produccion(request,template="granos_basicos/productores/genero_produccion.html"):
    filtro = _queryset_filtrado(request)

    CHOICE_SEXO = ((1,'Hombre'),(2,'Mujer'))
    CHOICE_SEXO_JEFE = ((1,'Hombre'),(2,'Mujer'),(3,'Compartida'))

    sexo_productor = {}
    prod_mujeres = {}
    prod_hombres = {}
    for obj in CHOICE_SEXO:
        conteo = filtro.filter(productor__sexo = obj[0]).distinct('productor').count()
        sexo_productor[obj[1]] = conteo

        for x in CHOICE_SEXO_JEFE:
            jefe_familia = filtro.filter(productor__sexo = obj[0],productor__productor__jefe = x[0]).distinct('productor').count()
            if obj[0] == '1':
                prod_hombres[x[1]] = jefe_familia
            else:
                prod_mujeres[x[1]] = jefe_familia

    quien_produce = {}
    for obj in RELACION_CHOICES:
        conteo = filtro.filter(productor__productorgranosbasicos__relacion = obj[0]).distinct('productor').count()
        quien_produce[obj[1]] = conteo

    return render(request, template, locals())

def composicion_familiar(request,template="granos_basicos/productores/composicion_familiar.html"):
	filtro = _queryset_filtrado(request)

	count_productores = filtro.distinct('productor').count()

	hijas = filtro.filter(productor__composicionfamiliar__familia = '4').distinct('productor__composicionfamiliar').count()
	avg_hijas = hijas / count_productores

	hijos = filtro.filter(productor__composicionfamiliar__familia = '3').distinct('productor__composicionfamiliar').count()
	avg_hijos = hijos / count_productores

	ESCOLARIDAD_CHOICES = (
		(1,'Ninguno'),(2,'Primaria Incompleta'),(3,'Primaria'),
		(4,'Secundaria Incompleta'),(5,'Secundaria'),(6,'Técnico'),
		(7,'Universitario'),(8,'Profesional'),
	)

	escolaridad = {}
	escolaridad_hijos = {}
	for obj in ESCOLARIDAD_CHOICES:
		padre = filtro.filter(productor__composicionfamiliar__familia = '1',
		                    productor__composicionfamiliar__escolaridad = obj[0]).distinct('productor__composicionfamiliar').count()
		percentage_padre = (padre / count_productores) * 100

		madre = filtro.filter(productor__composicionfamiliar__familia = '2',
		                    productor__composicionfamiliar__escolaridad = obj[0]).distinct('productor__composicionfamiliar').count()
		percentage_madre = (madre / count_productores) * 100

		escolaridad[obj[1]] = (percentage_padre,percentage_madre)

		#--------------------------------
		#hijos--------------------
		hijos_5_12 = filtro.filter(productor__composicionfamiliar__familia = '3',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (5,12)).distinct('productor__composicionfamiliar').count()

		hijos_13_18 = filtro.filter(productor__composicionfamiliar__familia = '3',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (13,18)).distinct('productor__composicionfamiliar').count()

		hijos_19 = filtro.filter(productor__composicionfamiliar__familia = '3',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (19,100)).distinct('productor__composicionfamiliar').count()

		#hijas--------------------
		hijas_5_12 = filtro.filter(productor__composicionfamiliar__familia = '4',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (5,12)).distinct('productor__composicionfamiliar').count()

		hijas_13_18 = filtro.filter(productor__composicionfamiliar__familia = '4',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (13,18)).distinct('productor__composicionfamiliar').count()

		hijas_19 = filtro.filter(productor__composicionfamiliar__familia = '4',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (19,100)).distinct('productor__composicionfamiliar').count()

		escolaridad_hijos[obj[1]] = (saca_porcentajes(hijas_5_12,hijas,False),
									saca_porcentajes(hijas_13_18,hijas,False),
									saca_porcentajes(hijas_19,hijas,False),

									saca_porcentajes(hijos_5_12,hijos,False),
									saca_porcentajes(hijos_13_18,hijos,False),
									saca_porcentajes(hijos_19,hijos,False))

	SI_NO_CHOICES = ((1,'Si'),(2,'No'))

	participacion = {}
	for obj in SI_NO_CHOICES:
		participan_hijos = filtro.filter(productor__composicionfamiliar__familia = '3',
									productor__composicionfamiliar__participacion = obj[0]).distinct(
									'productor__composicionfamiliar').count()

		participan_hijas = filtro.filter(productor__composicionfamiliar__familia = '4',
									productor__composicionfamiliar__participacion = obj[0]).distinct(
									'productor__composicionfamiliar').count()

		participacion[obj[1]] = (saca_porcentajes(participan_hijos,hijos,False),
								saca_porcentajes(participan_hijas,hijas,False))

	return render(request, template, locals())

def georeferencia(request,template="granos_basicos/monitoreos/georeferencia.html"):
	filtro = _queryset_filtrado(request)

	mapa = filtro.values('nombre_parcela','latitud','longitud')

	return render(request, template, locals())

def caracteristicas_parcela(request,template="granos_basicos/monitoreos/caracteristicas_parcela.html"):
	filtro = _queryset_filtrado(request)

	parcela_5 = filtro.filter(edad_parcela__range = (0,5)).aggregate(avg = Avg('profundidad_capa'))['avg']
	parcela_6_20 = filtro.filter(edad_parcela__range = (6,20)).aggregate(avg = Avg('profundidad_capa'))['avg']
	parcela_20 = filtro.filter(edad_parcela__range = (21,100)).aggregate(avg = Avg('profundidad_capa'))['avg']

	#grafico de lineas
	inclinado = filtro.filter(distribucionpendiente__seleccion = '1',distribucionpendiente__inclinado__gt = 59.9).values_list('profundidad_capa','distribucionpendiente__inclinado')
	plano = filtro.filter(distribucionpendiente__seleccion = '1',distribucionpendiente__plano__gt = 59.9).values_list('profundidad_capa','distribucionpendiente__plano')

	#acceso agua
	SI_NO_CHOICES = ((1,'Si'),(2,'No'))

	acceso_agua = {}
	for obj in SI_NO_CHOICES:
		conteo = filtro.filter(acceso_agua = obj[0]).count()
		acceso_agua[obj[1]] = conteo

	#fuente agua
	fuente_agua = {}
	for obj in ACCESO_AGUA_CHOICES:
		conteo = filtro.filter(fuente_agua__icontains = obj[0]).count()
		fuente_agua[obj[1]] = conteo

	print fuente_agua
	return render(request, template, locals())

def get_comunies(request):
    ids = request.GET.get('ids', '')
    results = []
    dicc = {}
    if ids:
        lista = ids.split(',')

    monitoreos = Monitoreo.objects.filter(productor__municipio__pk__in = lista).distinct().values_list('productor__comunidad__id', flat=True)
    municipios = Municipio.objects.filter(pk__in = lista)

    dicc = {}
    for municipio in municipios:
        comunies = Comunidad.objects.filter(municipio__id = municipio.id,id = monitoreos)
        lista1 = []
        comu = {}
        for c in comunies:
            comu['id'] = c.id
            comu['nombre'] = c.nombre
            lista1.append(comu)
            dicc[municipio.nombre] = lista1

    return HttpResponse(simplejson.dumps(dicc), content_type = 'application/json')

def saca_porcentajes(dato, total, formato=True):
	if dato != None:
		try:
			porcentaje = (dato/float(total)) * 100 if total != None or total != 0 else 0
		except:
			return 0
		if formato:
			return porcentaje
		else:
			return '%.2f' % porcentaje
	else:
		return 0
