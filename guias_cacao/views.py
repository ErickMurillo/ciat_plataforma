# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConsultaSombraForm
from .models import *
from mapeo.models import Persona
import json as simplejson
from itertools import chain
from django.db.models import Avg, Sum
import numpy as np
from collections import OrderedDict
# Create your views here.

def _queryset_filtrado_sombra(request):
    params = {}

    if 'fecha' in request.session:
        params['fecha_visita__year'] = request.session['fecha']

    if 'productor' in request.session:
        params['productor__nombre'] = request.session['productor']

    if 'organizacion' in request.session:
        params['productor__productor__organizacion'] = request.session['organizacion']

    if 'pais' in request.session:
        params['productor__pais'] = request.session['pais']

    if 'departamento' in request.session:
        params['productor__departamento'] = request.session['departamento']

    if 'municipio' in request.session:
        params['productor__municipio'] = request.session['municipio']

    if 'comunidad' in request.session:
        params['productor__comunidad'] = request.session['comunidad']

    if 'sexo' in request.session:
        params['productor__sexo'] = request.session['sexo']

    if 'tipologia' in request.session:
        params['productor__productor__tipologia'] = request.session['tipologia']

    unvalid_keys = []
    for key in params:
    	if not params[key]:
    		unvalid_keys.append(key)

    for key in unvalid_keys:
    	del params[key]

    print params

    return FichaSombra.objects.filter(**params)



def index_ficha_sombra(request, template='guiascacao/index.html'):
    if request.method == 'POST':
        form = ConsultaSombraForm(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['productor'] = form.cleaned_data['productor']
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['pais'] = form.cleaned_data['pais']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['municipio'] = form.cleaned_data['municipio']
            request.session['comunidad'] = form.cleaned_data['comunidad']
            request.session['sexo'] = form.cleaned_data['sexo']
            request.session['tipologia'] = form.cleaned_data['tipologia']
            centinela = 1
        else:
            centinela = 0
    else:
        form = ConsultaSombraForm()
        centinela = 0

        if 'fecha' in request.session:
            try:
                del request.session['fecha']
                del request.session['productor']
                del request.session['organizacion']
                del request.session['pais']
                del request.session['departamento']
                del request.session['municipio']
                del request.session['comunidad']
                del request.session['sexo']
                del request.session['tipologia']
            except:
                pass

    return render(request, template, {'form': form, 'centinela': centinela})


#---------------- salidas sombra -----------------------------

def riqueza_sombra(request, template="guiascacao/sombra_riqueza.html"):
    filtro = _queryset_filtrado_sombra(request)
    print filtro
    return render(request, template, locals())

def analisis_sombra(request, template="guiascacao/analisis_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    CHOICE_DENSIDAD = ( (1,'Alta'),
                        (2,'Adecuada'),
                        (3,'Baja'),
                      )

    CHOICE_COPA = ((1,'Ancha'),
                   (2,'Adecuada'),
                   (3,'Angosta'),
                )

    CHOICE_ARREGLO = ((1, 'Uniforme'), (2, 'Desuniforme'))
    CHOICE_HOJARASCA = ((1, 'Suficiente'), (2, 'No Suficiente'))
    CHOICE_HOJARASCA_CALIDAD = ((1, 'Rico en nutrientes'), (2, 'Pobre en nutriente'))
    CHOICE_COMPETENCIA = ((1, 'Fuerte'), (2, 'Mediana'), (3, 'Leve'))
    CHOICE_PROBLEMA = (
                        (1,'Cobertura'),
                        (2,'Mal arreglo'),
                        (3,'Competencia'),
                        (4,'Densidad Tipo de árboles'),
                        (5,'Ninguno')
                    )

    dict_densidad = {}
    for densidad in CHOICE_DENSIDAD:
        conteo = filtro.filter(analisissombra__densidad=densidad[0]).count()
        dict_densidad[densidad[1]] = conteo

    dict_copa = {}
    for copa in CHOICE_COPA:
        conteo = filtro.filter(analisissombra__forma_copa=copa[0]).count()
        dict_copa[copa[1]] = conteo

    dict_arreglo = {}
    for arreglo in CHOICE_ARREGLO:
        conteo = filtro.filter(analisissombra__arreglo=arreglo[0]).count()
        dict_arreglo[arreglo[1]] = conteo

    dict_hojarasca = {}
    for hoja in CHOICE_HOJARASCA:
        conteo = filtro.filter(analisissombra__hojarasca=hoja[0]).count()
        dict_hojarasca[hoja[1]] = conteo

    dict_calidad_hojarasca = {}
    for hoja in CHOICE_HOJARASCA_CALIDAD:
        conteo = filtro.filter(analisissombra__calidad_hojarasca=hoja[0]).count()
        dict_calidad_hojarasca[hoja[1]] = conteo

    dict_competencia = {}
    for obj in CHOICE_COMPETENCIA:
        conteo = filtro.filter(analisissombra__competencia=obj[0]).count()
        dict_competencia[obj[1]] = conteo

    dict_problema = {}
    for obj in CHOICE_PROBLEMA:
        conteo = filtro.filter(analisissombra__Problema=obj[0]).count()
        dict_problema[obj[1]] = conteo


    return render(request, template, locals())

def riqueza_sombra(request, template="guiascacao/sombra_riqueza.html"):
    filtro = _queryset_filtrado_sombra(request)
    print filtro
    return render(request, template, locals())


def cobertura_sombra(request, template="guiascacao/cobertura_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    punto1 = Cobertura1.objects.filter(ficha__in=filtro).values_list('cobertura', flat=True)
    punto2 = Cobertura2.objects.filter(ficha__in=filtro).values_list('cobertura', flat=True)
    punto3 = Cobertura3.objects.filter(ficha__in=filtro).values_list('cobertura', flat=True)

    l = list(chain(punto1, punto2, punto3))

    #promedio_todo_puntos = reduce(lambda x, y: x + y, l) / len(l)

    # media arítmetica
    promedio2 = np.mean(l)
    # mediana
    mediana2 = np.median(l)
    # Desviación típica
    desviacion2 = np.std(l)

    rangos = {'0 - 20': (0, 20.99),
              '21 - 40': (21, 40.99),
              '41 - 60': (41, 60.99),
              '61 - 80': (61, 80.99),
              '> 81 ': (81, 10000000),
              }
    rangos_cobertura1 = OrderedDict()
    for k, v in rangos.items():
        cnt = Cobertura1.objects.filter(ficha__in=filtro).filter(cobertura__range=v).count()
        rangos_cobertura1[k] = (cnt)

    rangos_cobertura2 = OrderedDict()
    for k, v in rangos.items():
        cnt = Cobertura2.objects.filter(ficha__in=filtro).filter(cobertura__range=v).count()
        rangos_cobertura2[k] = (cnt)

    rangos_cobertura3 = OrderedDict()
    for k, v in rangos.items():
        cnt = Cobertura3.objects.filter(ficha__in=filtro).filter(cobertura__range=v).count()
        rangos_cobertura3[k] = (cnt)


    rangos_todos = { k: rangos_cobertura1.get(k, 0) + rangos_cobertura2.get(k, 0) + rangos_cobertura3.get(k, 0) for k in set(rangos_cobertura1) | set(rangos_cobertura2) | set(rangos_cobertura3)}
    od = OrderedDict(sorted(rangos_todos.items()))

    return render(request, template, locals())


def densidad_sombra(request, template="guiascacao/densidad_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    total_puntos = []
    for obj in filtro:
        total1 = Punto1.objects.exclude(especie__id=11).filter(ficha=obj).aggregate(pi=Sum('pequena'),
                                                                   mi=Sum('mediana'),
                                                                   gi=Sum('grande'), )
        try:
            suma_total1 = sum(total1.itervalues())
        except:
            pass

        total2 = Punto2.objects.exclude(especie__id=11).filter(ficha=obj).aggregate(pi=Sum('pequena'),
                                                                   mi=Sum('mediana'),
                                                                   gi=Sum('grande'), )
        try:
            suma_total2 = sum(total2.itervalues())
        except:
            pass

        total3 = Punto3.objects.exclude(especie__id=11).filter(ficha=obj).aggregate(pi=Sum('pequena'),
                                                                   mi=Sum('mediana'),
                                                                   gi=Sum('grande'), )
        try:
            suma_total3 = sum(total3.itervalues())
        except:
            pass

        gran_suma = suma_total1 + suma_total2 + suma_total3
        densidad_total = (gran_suma  * float(10000)) / float(3000)

        total_puntos.append(densidad_total)
    # media arítmetica
    promedio2 = np.mean(total_puntos)
    # mediana
    mediana2 = np.median(total_puntos)
    # Desviación típica
    desviacion2 = np.std(total_puntos)

    veinte = 0
    cuarenta = 0
    sesenta = 0
    ochenta = 0
    mas_cien = 0
    for obj in total_puntos:
        if obj >= 0 and obj <= 20.99:
            veinte += 1
        elif obj >= 21 and obj <= 40.99:
            cuarenta += 1
        elif obj >= 41 and obj <= 60.99:
            sesenta += 1
        elif obj >= 61 and obj <= 80.99:
            ochenta += 1
        elif obj > 81:
            mas_cien += 1

    return render(request, template, locals())

def acciones_sombra(request, template="guiascacao/acciones_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    CHOICE_ACCIONES_SOMBRA = (
        (1, 'Reducir la sombra'),
        (2, 'Aumentar la sombra'),
        (3, 'Ninguna'),)

    dict_acciones = {}
    for obj in CHOICE_ACCIONES_SOMBRA:
        cnt = filtro.filter(accionessombra__accion=obj[0]).count()
        dict_acciones[obj[1]] = (cnt/float(len(filtro))) * 100

    CHOICE_PODA = (
        (1, 'Si'),
        (2, 'No'),
    )
    dict_reducir_poda = {}
    dict_reducir_eliminando = {}
    VAR_REDUCIR = filtro.filter(accionessombra__accion=1).count()
    for obj in CHOICE_PODA:
        cnt_poda = filtro.filter(reducirsombra__poda=obj[0]).count()
        cnt_elim = filtro.filter(reducirsombra__eliminando=obj[0]).count()

        dict_reducir_poda[obj[1]] = (cnt_poda/float(VAR_REDUCIR)) * 100
        dict_reducir_eliminando[obj[1]] = (cnt_elim/float(VAR_REDUCIR)) * 100

    CHOICE_TODO = (
        (1, 'En todo la parcela '),
        (2, 'Solo en una parte de la parcela'),
    )
    dict_todo = {}
    for obj in CHOICE_TODO:
        cnt = filtro.filter(reducirsombra__todo=obj[0]).count()

        dict_todo[obj[1]] = (cnt/float(VAR_REDUCIR)) * 100

    dict_aumentar_poda = {}
    dict_aumentar_eliminando = {}
    VAR_AUMENTAR = filtro.filter(accionessombra__accion=2).count()
    for obj in CHOICE_PODA:
        cnt_sembra = filtro.filter(aumentarsombra__sembrando=obj[0]).count()
        cnt_cambia = filtro.filter(aumentarsombra__cambiando=obj[0]).count()

        dict_aumentar_poda[obj[1]] = (cnt_sembra/float(VAR_AUMENTAR)) * 100
        dict_aumentar_eliminando[obj[1]] = (cnt_cambia/float(VAR_AUMENTAR)) * 100

    dict_aumentar_todo = {}
    for obj in CHOICE_TODO:
        cnt = filtro.filter(aumentarsombra__todo=obj[0]).count()

        dict_aumentar_todo[obj[1]] = (cnt/float(VAR_REDUCIR)) * 100

    dict_manejo_herramienta = {}
    dict_manejo_formacion = {}
    for obj in CHOICE_PODA:
        cnt_herra = filtro.filter(manejosombra__herramientas=obj[0]).count()
        cnt_forma = filtro.filter(manejosombra__formacion=obj[0]).count()

        dict_manejo_herramienta[obj[1]] = (cnt_herra/float(len(filtro))) * 100
        dict_manejo_formacion[obj[1]] = (cnt_forma/float(len(filtro))) * 100

    return render(request, template, locals())

def caracterizacion_sombra(request, template="guiascacao/caracterizacion_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)


    #punto1
    punto1_pere_pi = Punto1.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=1).aggregate(pi=Sum('pequena'))
    punto1_pere_mi = Punto1.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=1).aggregate(mi=Sum('mediana'))
    punto1_pere_gi = Punto1.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=1).aggregate(gi=Sum('grande'))

    punto1_cad_pi = Punto1.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=2).aggregate(pi=Sum('pequena'))
    punto1_cad_mi = Punto1.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=2).aggregate(mi=Sum('mediana'))
    punto1_cad_gi = Punto1.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=2).aggregate(gi=Sum('grande'))

    #punto2
    punto2_pere_pi = Punto2.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=1).aggregate(pi=Sum('pequena'))
    punto2_pere_mi = Punto2.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=1).aggregate(mi=Sum('mediana'))
    punto2_pere_gi = Punto2.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=1).aggregate(gi=Sum('grande'))

    punto2_cad_pi = Punto2.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=2).aggregate(pi=Sum('pequena'))
    punto2_cad_mi = Punto2.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=2).aggregate(mi=Sum('mediana'))
    punto2_cad_gi = Punto2.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=2).aggregate(gi=Sum('grande'))

    #punto3
    punto3_pere_pi = Punto3.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=1).aggregate(pi=Sum('pequena'))
    punto3_pere_mi = Punto3.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=1).aggregate(mi=Sum('mediana'))
    punto3_pere_gi = Punto3.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=1).aggregate(gi=Sum('grande'))

    punto3_cad_pi = Punto3.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=2).aggregate(pi=Sum('pequena'))
    punto3_cad_mi = Punto3.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=2).aggregate(mi=Sum('mediana'))
    punto3_cad_gi = Punto3.objects.exclude(especie__id=11).filter(ficha__in=filtro, tipo=2).aggregate(gi=Sum('grande'))

    total_puntos_pere_pi = list(chain(punto1_pere_pi.itervalues(), punto2_pere_pi.itervalues(), punto3_pere_pi.itervalues()))
    total_puntos_pere_mi = list(chain(punto1_pere_mi.itervalues(), punto2_pere_mi.itervalues(), punto3_pere_mi.itervalues()))
    total_puntos_pere_gi = list(chain(punto1_pere_gi.itervalues(), punto2_pere_gi.itervalues(), punto3_pere_gi.itervalues()))


    grafo_pere_pi = sum(total_puntos_pere_pi)
    grafo_pere_mi = sum(total_puntos_pere_mi)
    grafo_pere_gi = sum(total_puntos_pere_gi)

    total_puntos_cad_pi = list(chain(punto1_cad_pi.itervalues(), punto2_cad_pi.itervalues(), punto3_cad_pi.itervalues()))
    total_puntos_cad_mi = list(chain(punto1_cad_mi.itervalues(), punto2_cad_mi.itervalues(), punto3_cad_mi.itervalues()))
    total_puntos_cad_gi = list(chain(punto1_cad_gi.itervalues(), punto2_cad_gi.itervalues(), punto3_cad_gi.itervalues()))

    grafo_cad_pi = sum(total_puntos_cad_pi)
    grafo_cad_mi = sum(total_puntos_cad_mi)
    grafo_cad_gi = sum(total_puntos_cad_gi)

    return render(request, template, locals())
#----------------- fin salidas de sombra -------------------------

#----------  funciones utilitarias -----------------

def get_productor(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        personas = Persona.objects.filter(nombre__icontains = q, tipo_persona=1 )[:10]
        results = []
        for person in personas:
            personas_json = {}
            personas_json['id'] = person.id
            personas_json['label'] = person.nombre
            personas_json['value'] = person.nombre
            results.append(personas_json)
    else:
        results = 'fail'
    return HttpResponse(simplejson.dumps(results), content_type='application/json')
