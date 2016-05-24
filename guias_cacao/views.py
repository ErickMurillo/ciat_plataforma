# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConsultaSombraForm
from .models import FichaSombra, FichaPoda, FichaPlaga, FichaPiso, Cobertura1, Cobertura2, Cobertura3
from mapeo.models import Persona
import json as simplejson
from itertools import chain
from django.db.models import Avg, Sum
import numpy as np
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
    print len(punto3)
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
    rangos_cobertura1 = {}
    for k, v in rangos.items():
        cnt = Cobertura1.objects.filter(ficha__in=filtro).filter(cobertura__range=v).count()
        rangos_cobertura1[k] = (cnt)

    rangos_cobertura2 = {}
    for k, v in rangos.items():
        cnt = Cobertura2.objects.filter(ficha__in=filtro).filter(cobertura__range=v).count()
        rangos_cobertura2[k] = (cnt)

    rangos_cobertura3 = {}
    for k, v in rangos.items():
        cnt = Cobertura3.objects.filter(ficha__in=filtro).filter(cobertura__range=v).count()
        rangos_cobertura3[k] = (cnt)


    print { k: rangos_cobertura1.get(k, 0) + rangos_cobertura2.get(k, 0) + rangos_cobertura3.get(k, 0) for k in set(rangos_cobertura1) | set(rangos_cobertura2) | set(rangos_cobertura3)}



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
