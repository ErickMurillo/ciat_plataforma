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
        #if 'fecha' in request.session:
        #    del request.session['fecha']
        #    del request.session['pais']
        #    del request.session['sitio_accion']
        #    del request.session['tipo_estudio']
    
    return render(request, template, locals())

def salida1(request, template="analisis/salida1.html"):
    filtro = _queryset_filtrado(request)
    #print "cuantas encuestas hay: %s " % (filtro.count())

    sectores = {}
    sectores1 = {}
    for x in Sector.objects.all():
        cont_organizacion = filtro.filter(organizacion__sector=x).count()
        sectores[x.nombre] = cont_organizacion

        cont_organizacion1 = filtro.filter(organizacion__sector=x)
        sectores1[x.nombre] = cont_organizacion1.distinct()
        
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
        cont_organizacion = filtro.filter(organizacion__sector=choice).count()

        resultados = query.count()

        fila = [choice.nombre,cont_organizacion,resultados,promedio(resultados,cont_organizacion)]

        tabla.append(fila)
        proyectos[choice.nombre] = promedio(resultados,cont_organizacion)

        valores1.append(cont_organizacion)
        valores2.append(resultados)
        valores3.append(float(promedio(resultados,cont_organizacion)))
        
    total1 = sumarLista(valores1)
    total2 = sumarLista(valores2)
    total3 = sumarLista(valores3)/len(valores3)
        
    return render(request,template, locals())

def salida3(request, template="analisis/salida3.html"):
    filtro = _queryset_filtrado(request)

    sectores = Sector.objects.all()
    
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
    valores1 = []
    valores2 = []
    valores3 = []
    
    for imp in Sector.objects.all():
        preg_4 = filtro.filter(pregunta_4__entrevistado__organizacion__sector=imp).count()
        cont_organizacion = filtro.filter(organizacion__sector=imp).count()
        
        fila = [imp.nombre,cont_organizacion,preg_4,promedio(preg_4,cont_organizacion)]

        tabla.append(fila)
        impactos[imp.nombre] = promedio(preg_4,cont_organizacion)

        valores1.append(cont_organizacion)
        valores2.append(preg_4)
        valores3.append(float(promedio(preg_4,cont_organizacion)))
        
    total1 = sumarLista(valores1)
    total2 = sumarLista(valores2)
    total3 = sumarLista(valores3)/len(valores3)

        
    return render(request,template, locals())

def salida8(request, template="analisis/salida8.html"):
	#revisar
	filtro = _queryset_filtrado(request)

	tabla = []

	for p in Papel.objects.all():
		socio = filtro.filter(pregunta_5c__pregunta_5c_nested__papel_1=p).count()
		# for obj in Pregunta_5c.objects.all():
		# 	for x in obj.pregunta_5c_nested_set.all():
		# 		prioritizado = filtro.filter(pregunta_5c__pregunta_5c_nested__papel_1=p).count()
		# 		print prioritizado
		

		fila = [p.nombre,'--',socio]
		tabla.append(fila)
		print tabla

	return render(request,template, locals())

def salida9(request, template="analisis/salida9.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	datos = {}

	for x in Sector.objects.all():
		cont_organizacion = filtro.filter(organizacion__sector=x).count()
		cont_socios = filtro.filter(pregunta_5c__pregunta_5c_nested__pregunta_5c__entrevistado__organizacion__sector=x).count()
		try:
			avg_total = promedio(cont_organizacion, cont_socios)
		except:
			avg_total = 0

		fila = [x.nombre,cont_organizacion,cont_socios,avg_total]
		tabla.append(fila)
		datos[x.nombre] = avg_total

	return render(request,template, locals())

def salida10(request, template="analisis/salida10.html"):
	filtro = _queryset_filtrado(request)

	tabla = []
	datos = {}

	for x in Sector.objects.all():
		cont_socio_1 = Pregunta_1.objects.filter(entrevistado=filtro,socio__sector=x).distinct('socio')
		cont_socio_2 = Pregunta_5a.objects.filter(entrevistado=filtro,socio__sector=x).distinct('socio')

		tabla.append(cont_socio_1)
		tabla.append(cont_socio_2)
		datos[x] = (list(set(tabla)))

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
        cont_organizacion = filtro.filter(organizacion__sector=choice).count()

        fila = [choice.nombre,cont_organizacion,innovaciones,promedio(innovaciones,cont_organizacion)]

        tabla.append(fila)
        proyectos[choice.nombre] = promedio(innovaciones,cont_organizacion)

        valores1.append(cont_organizacion)
        valores2.append(innovaciones)
        valores3.append(float(promedio(innovaciones,cont_organizacion)))
        
    total1 = sumarLista(valores1)
    total2 = sumarLista(valores2)
    total3 = sumarLista(valores3)/len(valores3)
        
    return render(request,template, locals())

def salida15(request, template="analisis/salida15.html"):
	#falta grafica
    filtro = _queryset_filtrado(request)

    temas = {}  
    
    for y in Tema.objects.all():
        contador_pregunta1 = filtro.filter(pregunta_6a__tema=y).count()
        temas[y.tema] = contador_pregunta1
        
    return render(request,template, locals())

###########################################################################################

def salida5(request, template="analisis/salida5.html"):
    filtro = _queryset_filtrado(request)

    tematicas = {}
    datos = []
    for obj in Tema.objects.all():
        count_impacts = filtro.filter(pregunta_4__tema=obj).count()
        count_projects = filtro.filter(pregunta_1__tema=obj).count()

        fila = [obj.tema,count_projects,count_impacts]
        datos.append(fila)
        #tematicas[obj] = count_impacts
        #for sector in Sector.objects.all():
        #    cont_organizacion = filtro.filter(pregunta_4__entrevistado__organizacion__sector=sector).count()
        #     tematicas[obj] = (cont_organizacion,count_impacts)


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
    for obj in Sector.objects.all():
        count_organization = filtro.filter(pregunta_5a__socio__sector=obj).count()
        count_innovation = filtro.filter(pregunta_5a__innovacion=True).exclude(pregunta_5a__innovacion='').count()
        try:
            avg_total = promedio(count_organization, count_innovation)
        except:
            avg_total = 0
        lista.append(count_innovation)
        mediana_obj = calcular_mediana(lista)
        datos[obj] = (count_organization,count_innovation, avg_total, mediana_obj)


    return render(request, template, locals())


def salida7(request, template="analisis/salida7.html"):
    filtro = _queryset_filtrado(request)

    datos = {}
    for obj in Tema.objects.all():
        count_tema = filtro.filter(pregunta_5a__tema=obj, pregunta_5a__innovacion=True).count()
        datos[obj] = count_tema


    return render(request, template, locals())


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

class BusquedaPaisView(TemplateView):
     
    def get(self, request, *args, **kwargs):
        id_pais = request.GET['id']
        departamento = Departamento.objects.filter(pais__id=id_pais)
        data = serializers.serialize('json',departamento,fields=('nombre',))
        return HttpResponse(data,mimetype='application/json')
