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
        print request.session['fecha']

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
        
    print Entrevista.objects.filter(**params)
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

def salida1(request, template="analisis/salida1.html"):
    filtro = _queryset_filtrado(request)

    sectores = {}
    sectores1 = {}

    for x in Sector.objects.all():
        cont_organizacion = filtro.filter(organizacion__sector=x).count()
        sectores[x.nombre] = cont_organizacion

        cont_organizacion1 = filtro.filter(organizacion__sector=x)	
        sectores1[x.nombre] = cont_organizacion1
        
    return render(request,template, locals())

def salida2(request, template="analisis/salida2.html"):
    filtro = _queryset_filtrado(request)

    tabla = []
    proyectos = {}
    valores1 = []
    valores2 = []

    for choice in Sector.objects.all():
        query = filtro.filter(pregunta_1__socio__sector=choice)
        cont_organizacion = filtro.filter(organizacion__sector=choice).count()

        resultados = query.count()

        fila = [choice.nombre,
                cont_organizacion,
                resultados,
                promedio(resultados,cont_organizacion)
                ]

        tabla.append(fila)
        proyectos[choice.nombre] = promedio(resultados,cont_organizacion)

        valores1.append(cont_organizacion)
        valores2.append(resultados)
        
    total1 = sumarLista(valores1)
    total2 = sumarLista(valores2)
        
    return render(request,template, locals())

def salida3(request, template="analisis/salida3.html"):
    filtro = _queryset_filtrado(request)
    
    temas = {}  
    for y in Tema.objects.all():
        contador_pregunta1 = filtro.filter(pregunta_1__tema=y).count()
        temas[y.tema] = contador_pregunta1
        
    return render(request,template, locals())

def salida4(request, template="analisis/salida4.html"):
    filtro = _queryset_filtrado(request)

    #salida 4: Numero de Impactos por Grupo Organizacional
    impactos = {}
    tabla = []
    
    for imp in Sector.objects.all():
        preg_4 = filtro.filter(pregunta_4__entrevistado__organizacion__sector=imp).count()
        cont_organizacion = filtro.filter(organizacion__sector=imp).count()
        #impactos[imp.nombre] = preg_4
        fila = [imp.nombre,
	                cont_organizacion,
	                preg_4,
	                promedio(preg_4,cont_organizacion)
	                ]

        tabla.append(fila)
        
    return render(request,template, locals())

def post(request,template='analisis/index.html'):
	fecha = request.POST['fecha']
	pais = request.POST['pais']
	sitio_accion = request.POST['sitio_accion']
	tipo_estudio = request.POST['tipo_estudio']
	
	
	#salida 1 : Participacion entrevista por sector
	sectores = {}
	for x in Sector.objects.all():
		cont_organizacion = Organizaciones.objects.filter(sector=x,sitio_accion=sitio_accion,pais=pais,
												 entrevista__tipo_estudio=tipo_estudio,
												 entrevista__fecha1=fecha).count()
		sectores[x.nombre] = cont_organizacion

	sectores1 = {}
	for x in Sector.objects.all():
		cont_organizacion = Organizaciones.objects.filter(sector=x,sitio_accion=sitio_accion,pais=pais,
															entrevista__tipo_estudio=tipo_estudio,
															entrevista__fecha1=fecha)
		sectores1[x.nombre] = cont_organizacion	

	#salida 2: Proyectos/Iniciativas de las Organizaciones
	tabla = []
	proyectos = {}
	valores1 = []
	valores2 = []

	for choice in Sector.objects.all():
		query = Pregunta_1.objects.filter(entrevistado__organizacion__sector=choice,
										   entrevistado__organizacion__sitio_accion=sitio_accion,
										   entrevistado__organizacion__pais=pais,
										   entrevistado__fecha1=fecha)
		cont_organizacion = Organizaciones.objects.filter(sector=choice,sitio_accion=sitio_accion,pais=pais,
												 entrevista__tipo_estudio=tipo_estudio,
												 entrevista__fecha1=fecha).count()

		resultados = query.count()

		fila = [choice.nombre,
				cont_organizacion,
				resultados,
				promedio(resultados,cont_organizacion)
				]

		tabla.append(fila)
		proyectos[choice.nombre] = promedio(resultados,cont_organizacion)

		valores1.append(cont_organizacion)
		valores2.append(resultados)
		
	total1 = sumarLista(valores1)
	total2 = sumarLista(valores2)

	


 	#salida 3: Distribución de Proyectos/Iniciativas por Temáticas
	temas = {}	
	for y in Tema.objects.all():
		contador_pregunta1 = Pregunta_1.objects.filter(tema=y,
													   entrevistado__organizacion__sitio_accion=sitio_accion,
													   entrevistado__organizacion__pais=pais,
													   entrevistado__fecha1=fecha).count()
		temas[y.tema] = contador_pregunta1

	
	#salida 4: Numero de Impactos por Grupo Organizacional
	impactos = {}
	for imp in Sector.objects.all():
		preg_4 = Pregunta_4.objects.filter(entrevistado__organizacion__sector=imp,
										   entrevistado__organizacion__sitio_accion=sitio_accion,
										   entrevistado__organizacion__pais=pais,
										   entrevistado__fecha1=fecha).count()
		impactos[imp.nombre] = preg_4


	return render(request, template, locals())

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
	return '%.1f' % promedio


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
