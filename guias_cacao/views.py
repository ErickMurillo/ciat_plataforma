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
from collections import OrderedDict, Counter
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

def analisis_sombra(request, template="guiascacao/sombra/analisis_sombra.html"):
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


def cobertura_sombra(request, template="guiascacao/sombra/cobertura_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)
    numero_parcelas = filtro.count()

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
    #minimo y maximo
    minimo2 = min(l)
    maximo2 = max(l)
    #TODO

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

def riqueza_sombra(request, template="guiascacao/sombra_riqueza.html"):
    filtro = _queryset_filtrado_sombra(request)
    numero_parcelas = filtro.count()

    puntos = []
    for obj in filtro:
        cnt1 = Punto1.objects.filter(ficha=obj).values_list('especie__id', flat=True)
        cnt2 = Punto2.objects.filter(ficha=obj).values_list('especie__id', flat=True)
        cnt3 = Punto3.objects.filter(ficha=obj).values_list('especie__id', flat=True)
        lista = list(cnt1) + list(cnt2) + list(cnt3)

        reducida_lista = list(set(lista))
        formula_riqueza = len(reducida_lista) #(len(reducida_lista) * 1000) / float(1890)
        puntos.append(formula_riqueza)

    # media arítmetica
    promedio2 = np.mean(puntos)
    # mediana
    mediana2 = np.median(puntos)
    # Desviación típica
    desviacion2 = np.std(puntos)
    #minimo
    minimo = min(puntos)
    #maximo
    maximo = max(puntos)

    #rangos
    grafo_riqueza = crear_rangos(request, puntos, minimo, maximo, step=2)

    return render(request, template, locals())


def densidad_sombra(request, template="guiascacao/sombra/densidad_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)
    numero_parcelas = filtro.count()

    total_puntos = []
    for obj in filtro:
        total1 = Punto1.objects.exclude(especie__id__in=[11,60]).filter(ficha=obj).aggregate(pi=Sum('pequena'),
                                                                   mi=Sum('mediana'),
                                                                   gi=Sum('grande'), )
        try:
            suma_total1 = sum(total1.itervalues())
        except:
            pass

        total2 = Punto2.objects.exclude(especie__id__in=[11,60]).filter(ficha=obj).aggregate(pi=Sum('pequena'),
                                                                   mi=Sum('mediana'),
                                                                   gi=Sum('grande'), )
        try:
            suma_total2 = sum(total2.itervalues())
        except:
            pass

        total3 = Punto3.objects.exclude(especie__id__in=[11,60]).filter(ficha=obj).aggregate(pi=Sum('pequena'),
                                                                   mi=Sum('mediana'),
                                                                   gi=Sum('grande'), )
        try:
            suma_total3 = sum(total3.itervalues())
        except:
            suma_total3 = 0

        try:
            gran_suma = suma_total1 + suma_total2 + suma_total3
        except:
            gran_suma = 0

        try:
            densidad_total = (gran_suma  * float(10000)) / float(1890)
        except:
            densidad_total = 0
        #print "gran suma: %s - encuesta: %s " % (densidad_total, obj)

        total_puntos.append(densidad_total)
    # media arítmetica
    promedio2 = np.mean(total_puntos)
    # mediana
    mediana2 = np.median(total_puntos)
    # Desviación típica
    desviacion2 = np.std(total_puntos)
    #minimo
    minimo = min(total_puntos)
    #maximo
    maximo = max(total_puntos)
    #rangos
    grafo_densidad = crear_rangos(request, total_puntos, minimo, maximo, step=25)

    return render(request, template, locals())

def acciones_sombra(request, template="guiascacao/sombra/acciones_sombra.html"):
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

        try:
            dict_aumentar_poda[obj[1]] = (cnt_sembra/float(VAR_AUMENTAR)) * 100
        except:
            dict_aumentar_poda[obj[1]] = 0
        try:
            dict_aumentar_eliminando[obj[1]] = (cnt_cambia/float(VAR_AUMENTAR)) * 100
        except:
            dict_aumentar_eliminando[obj[1]] = 0

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

def change(f):
    if f is None:
        return 0
    else:
        return f

def caracterizacion_sombra(request, template="guiascacao/sombra/caracterizacion_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    #calculos sobre tipo de especies
    dict_todo_tipo = {}
    for obj in CHOICE_TIPO_PUNTO:
        p1_tipo = Punto1.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p2_tipo = Punto2.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p3_tipo = Punto3.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        dict_todo_tipo[obj[1]] = [p1_tipo,p2_tipo,p3_tipo]

    todo_tipo = []
    for k, myLIst in dict_todo_tipo.items():
        pe = [item['pi'] for item in myLIst if item['pi'] is not None]
        me = [item['mi'] for item in myLIst if item['mi'] is not None]
        ga = [item['gi'] for item in myLIst if item['gi'] is not None]
        todo_tipo.append([sum(pe),sum(me),sum(ga)])

    #calculos sobre tipo de copas
    dict_todo_copa = {}
    for obj in CHOICE_TIPO_COPA_PUNTO:
        p1_copa = Punto1.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo_de_copa=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p2_copa = Punto2.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo_de_copa=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p3_copa = Punto3.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo_de_copa=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        dict_todo_copa[obj[1]] = [p1_copa,p2_copa,p3_copa]

    todo_copa = []
    for k, myLIst in dict_todo_copa.items():
        pe = [item['pi'] for item in myLIst if item['pi'] is not None]
        me = [item['mi'] for item in myLIst if item['mi'] is not None]
        ga = [item['gi'] for item in myLIst if item['gi'] is not None]
        todo_copa.append([sum(pe),sum(me),sum(ga)])


    #calculos sobre tipo de uso
    dict_todo_uso = {}
    for obj in CHOICE_TIPO_USO_PUNTO:
        p1_uso = Punto1.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, uso=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p2_uso = Punto2.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, uso=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p3_uso = Punto3.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, uso=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        dict_todo_uso[obj[1]] = [p1_uso,p2_uso,p3_uso]

    todo_uso = []
    for k, myLIst in dict_todo_uso.items():
        pe = [item['pi'] for item in myLIst if item['pi'] is not None]
        me = [item['mi'] for item in myLIst if item['mi'] is not None]
        ga = [item['gi'] for item in myLIst if item['gi'] is not None]
        todo_uso.append([sum(pe),sum(me),sum(ga)])

    return render(request, template, locals())

def dominancia_sombra(request, template="guiascacao/sombra/dominancia_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    CUANTO_ESPECIES = Especies.objects.exclude(id__in=[11,60]).count()
    dict_especie_todo = OrderedDict()

    for obj in Especies.objects.exclude(id__in=[11,60]):
        cnt_p1 = filtro.filter(punto1__especie=obj).aggregate(pi=Sum('punto1__pequena'),
                                                               mi=Sum('punto1__mediana'),
                                                               gi=Sum('punto1__grande'))

        cnt_p2 = filtro.filter(punto2__especie=obj).aggregate(pi=Sum('punto2__pequena'),
                                                              mi=Sum('punto2__mediana'),
                                                              gi=Sum('punto2__grande'))

        cnt_p3 = filtro.filter(punto3__especie=obj).aggregate(pi=Sum('punto3__pequena'),
                                                            mi=Sum('punto3__mediana'),
                                                            gi=Sum('punto3__grande'))

        dict_especie_todo[obj] = [cnt_p1,cnt_p2,cnt_p3]

    todo = {}
    SUMA_TOTAL_ESPECIE = 0
    for k, myLIst in dict_especie_todo.items():
        pe = [item['pi'] for item in myLIst if item['pi'] is not None]
        me = [item['mi'] for item in myLIst if item['mi'] is not None]
        ga = [item['gi'] for item in myLIst if item['gi'] is not None]
        suma_total = sum([sum(pe),sum(me),sum(ga)])
        if suma_total > 0:
            todo[k] = suma_total
            SUMA_TOTAL_ESPECIE += suma_total

    algo = sorted(todo.iteritems(), key=lambda (k,v): (v,k), reverse=True)

    return render(request, template, locals())

def dimensiones_sombra(request, template="guiascacao/sombra/dimenciones_especies_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    altura_p1 = []
    diametro_p1 = []
    anchura_p1 = []

    for obj in Especies.objects.exclude(id__in=[11,60]):
        conteo = filtro.filter(punto1__especie=obj).count()
        cnt_p1 = filtro.filter(punto1__especie=obj).aggregate(pi=Sum('punto1__pequena'),
                                                               mi=Sum('punto1__mediana'),
                                                               gi=Sum('punto1__grande'))
        if conteo > 0:
            for k,v in cnt_p1.items():
                if v > 0:
                    if k == 'pi':
                        alti = [obj.p_altura] * int(v)
                        diam = [obj.p_diametro] * int(v)
                        anch = [obj.p_ancho] * int(v)
                        altura_p1.append(alti)
                        diametro_p1.append(diam)
                        anchura_p1.append(anch)
                    if k == 'mi':
                        alti = [obj.m_altura] * int(v)
                        diam = [obj.m_diametro] * int(v)
                        anch = [obj.m_ancho] * int(v)
                        altura_p1.append(alti)
                        diametro_p1.append(diam)
                        anchura_p1.append(anch)
                    if k == "gi":
                        alti = [obj.g_altura] * int(v)
                        diam = [obj.g_diametro] * int(v)
                        anch = [obj.g_ancho] * int(v)
                        altura_p1.append(alti)
                        diametro_p1.append(diam)
                        anchura_p1.append(anch)

    altura_p2 = []
    diametro_p2 = []
    anchura_p2 = []

    for obj in Especies.objects.exclude(id__in=[11,60]):
        conteo = filtro.filter(punto2__especie=obj).count()
        cnt_p2 = filtro.filter(punto2__especie=obj).aggregate(pi=Sum('punto2__pequena'),
                                                               mi=Sum('punto2__mediana'),
                                                               gi=Sum('punto2__grande'))
        if conteo > 0:
            for k,v in cnt_p2.items():
                if v > 0:
                    if k == 'pi':
                        alti = [obj.p_altura] * int(v)
                        diam = [obj.p_diametro] * int(v)
                        anch = [obj.p_ancho] * int(v)
                        altura_p2.append(alti)
                        diametro_p2.append(diam)
                        anchura_p2.append(anch)
                    if k == 'mi':
                        alti = [obj.m_altura] * int(v)
                        diam = [obj.m_diametro] * int(v)
                        anch = [obj.m_ancho] * int(v)
                        altura_p2.append(alti)
                        diametro_p2.append(diam)
                        anchura_p2.append(anch)
                    if k == "gi":
                        alti = [obj.g_altura] * int(v)
                        diam = [obj.g_diametro] * int(v)
                        anch = [obj.g_ancho] * int(v)
                        altura_p2.append(alti)
                        diametro_p2.append(diam)
                        anchura_p2.append(anch)

    altura_p3 = []
    diametro_p3 = []
    anchura_p3 = []

    for obj in Especies.objects.exclude(id__in=[11,60]):
        conteo = filtro.filter(punto3__especie=obj).count()
        cnt_p3 = filtro.filter(punto3__especie=obj).aggregate(pi=Sum('punto3__pequena'),
                                                               mi=Sum('punto3__mediana'),
                                                               gi=Sum('punto3__grande'))
        if conteo > 0:
            for k,v in cnt_p3.items():
                if v > 0:
                    if k == 'pi':
                        alti = [obj.p_altura] * int(v)
                        diam = [obj.p_diametro] * int(v)
                        anch = [obj.p_ancho] * int(v)
                        altura_p3.append(alti)
                        diametro_p3.append(diam)
                        anchura_p3.append(anch)
                    if k == 'mi':
                        alti = [obj.m_altura] * int(v)
                        diam = [obj.m_diametro] * int(v)
                        anch = [obj.m_ancho] * int(v)
                        altura_p3.append(alti)
                        diametro_p3.append(diam)
                        anchura_p3.append(anch)
                    if k == "gi":
                        alti = [obj.g_altura] * int(v)
                        diam = [obj.g_diametro] * int(v)
                        anch = [obj.g_ancho] * int(v)
                        altura_p3.append(alti)
                        diametro_p3.append(diam)
                        anchura_p3.append(anch)

    altura_total = altura_p1 + altura_p2 + altura_p3
    diametro_total = diametro_p1 + diametro_p2 + diametro_p3
    anchura_total = anchura_p1 + anchura_p2 + anchura_p3

    #con esto trabajo estan las listas completas
    todas_alturas = list(chain.from_iterable(altura_total))
    todas_diametro = list(chain.from_iterable(diametro_total))
    todas_anchura = list(chain.from_iterable(anchura_total))

    #promedio, rango, desviacion estandar, media de altura
    promedio_altura = np.mean(todas_alturas)
    desviacion_altura = np.std(todas_alturas)
    media_altura = np.median(todas_alturas)
    minimo_altura = min(todas_alturas)
    maximo_altura = max(todas_alturas)

    grafo_altura = crear_rangos(request, todas_alturas, minimo_altura, maximo_altura, step=3)

    #promedio, rango, desviacion estandar, media de diametro
    promedio_diametro = np.mean(todas_diametro)
    desviacion_diametro = np.std(todas_diametro)
    media_diametro = np.median(todas_diametro)
    minimo_diametro = min(todas_diametro)
    maximo_diametro = max(todas_diametro)

    grafo_diametro = crear_rangos(request, todas_diametro, minimo_diametro, maximo_diametro, step=16)

    #promedio, rango, desviacion estandar, media de anchura
    promedio_anchura = np.mean(todas_anchura)
    desviacion_anchura = np.std(todas_anchura)
    media_anchura = np.median(todas_anchura)
    minimo_anchura = min(todas_anchura)
    maximo_anchura = max(todas_anchura)

    grafo_anchura = crear_rangos(request, todas_anchura, minimo_anchura, maximo_anchura, step=2)

    return render(request, template, locals())
#----------------- fin salidas de sombra -------------------------

#----------  funciones utilitarias -----------------
def crear_rangos(request, lista, start=0, stop=0, step=0):
    dict_algo = OrderedDict()
    rangos = []
    contador = 0
    rangos = [(n, n+int(step)-1) for n in range(int(start), int(stop), int(step))]

    for desde, hasta in rangos:
        dict_algo[(desde,hasta)] = len([x for x in lista if desde <= x <= hasta])

    return dict_algo


def get_productor(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        personas = Persona.objects.filter(nombre__icontains = q, tipo_persona=1 )[:10]
        #print personas
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

#salidas de poda
