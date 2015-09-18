from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import MapeoConsulta, MapaConsulta
import json
from itertools import chain
from datetime import datetime

# Create your views here.

def _queryset_filtrado(request):
    params = {}

    if 'area_accion' in request.session:
        params['alianza__sitio_accion__area_accion'] = request.session['area_accion']

    if 'sitio_accion' in request.session:
        params['alianza__sitio_accion'] = request.session['sitio_accion']

    if 'alianza' in request.session:
        params['alianza'] = request.session['alianza']

    #if 'proyectos' in request.session:
    #    params['productor__proyecto'] = request.session['proyectos']

    return Proyectos.objects.filter(**params)


def indexview(request, template='mapeo/index.html'):

    if request.method == 'POST':
        mensaje = None
        form = MapeoConsulta(request.POST)
        if form.is_valid():
            request.session['area_accion'] = form.cleaned_data['area_accion']
            request.session['sitio_accion'] = form.cleaned_data['sitio_accion']
            request.session['alianza'] = form.cleaned_data['alianza']
            #request.session['proyectos'] = form.cleaned_data['proyectos']
            request.session['activo'] = True
            centinela = 1

            #return HttpResponseRedirect('proyectos/')
        else:
            centinela = 0

    else:
        form = MapeoConsulta()
        mensaje = "Existen alguno errores"
        centinela = 0
        try:
            del request.session['area_accion']
            del request.session['sitio_accion']
            del request.session['plataforma']
            #del request.session['proyectos']
        except:
            pass

    proyectos = Proyectos.objects.all()

    return render(request, template, locals())


def proyectos(request, template="mapeo/proyectos.html"):

    proyectos = _queryset_filtrado(request)

    return render(request, template, locals())

def mapa_actores(request, template="mapeo/mapa.html", id_proyecto=None):

    el_proyecto = Proyectos.objects.get(id=id_proyecto)

    persona_productor = Persona.objects.filter(productor__proyecto__id=id_proyecto,tipo_persona=1)
    persona_lideres = Persona.objects.filter(lideres__proyecto__id=id_proyecto,tipo_persona=2)
    persona_tecnico = Persona.objects.filter(tecnicoespinvestigador__proyecto__id=id_proyecto, tipo_persona=3)
    persona_esp = Persona.objects.filter(decisor__proyecto__id=id_proyecto, tipo_persona=4)
    persona_inv = Persona.objects.filter(decisor__proyecto__id=id_proyecto, tipo_persona=5)
    persona_decisor = Persona.objects.filter(decisor__proyecto__id=id_proyecto, tipo_persona=6)

    if request.method == 'POST':
        mensaje = None
        form_mapa = MapaConsulta(request.POST)
        if form_mapa.is_valid():
            request.session['tipo_persona'] = form_mapa.cleaned_data['tipo_persona']
            request.session['activo'] = True
            centinela = 1
        else:
            centinela = 0

    else:
        form_mapa = MapaConsulta()
        mensaje = "Existen alguno errores"
        centinela = 0
        try:
            del request.session['tipo_persona']
        except:
            pass

    return render(request, template, locals())


def obtener_mapa(request, id_proyecto=None):
    persona_productor = Persona.objects.filter(productor__proyecto__id=id_proyecto)
    persona_lideres = Persona.objects.filter(lideres__proyecto__id=id_proyecto)
    persona_tecnicoespinvestigador = Persona.objects.filter(tecnicoespinvestigador__proyecto__id=id_proyecto)
    persona_decisor = Persona.objects.filter(decisor__proyecto__id=id_proyecto)

    todos = list(chain(persona_productor, persona_lideres, persona_tecnicoespinvestigador,persona_decisor))

    if request.is_ajax():
        lista = []
        params = []
        try:
            if request.POST['tipo_persona'] == '0':
                params = todos
            if request.POST['tipo_persona'] == '1':
                params = Persona.objects.filter(productor__proyecto__id=id_proyecto, tipo_persona=request.POST['tipo_persona'])
            if request.POST['tipo_persona'] == '2':
                params = Persona.objects.filter(lideres__proyecto__id=id_proyecto, tipo_persona=request.POST['tipo_persona'])
            if request.POST['tipo_persona'] == '3':
                params = Persona.objects.filter(tecnicoespinvestigador__proyecto__id=id_proyecto, tipo_persona=request.POST['tipo_persona'])
            if request.POST['tipo_persona'] == '4':
                params = Persona.objects.filter(tecnicoespinvestigador__proyecto__id=id_proyecto, tipo_persona=request.POST['tipo_persona'])
            if request.POST['tipo_persona'] == '5':
                params = Persona.objects.filter(tecnicoespinvestigador__proyecto__id=id_proyecto, tipo_persona=request.POST['tipo_persona'])
            if request.POST['tipo_persona'] == '6':
                params = Persona.objects.filter(decisor__proyecto__id=id_proyecto, tipo_persona=request.POST['tipo_persona'])

            for objeto in params:
                dicc = dict(nombre=objeto.nombre,
                            tipo=objeto.tipo_persona,
                            id=objeto.id,
                            lon=float(objeto.municipio.longitud) ,
                            lat=float(objeto.municipio.latitud),
                            )
                lista.append(dicc)
        except:
            pass

        serializado = json.dumps(lista)
        return HttpResponse(serializado, content_type='application/json')


def timelinejson(request, id_proyecto=None):
    if request.is_ajax():
        lista = []
        for objeto in TimeLineProyecto.objects.filter(proyecto__id=id_proyecto):
            dicc = dict(title=str(objeto.fecha.strftime("%B %d, %Y")),
                        description=objeto.texto,
                        startDate=str(objeto.fecha.strftime("%B %d, %Y")),
                        endDate= 'null',
                        )
            lista.append(dicc)

        serializado = json.dumps(lista)
        print serializado
        return HttpResponse(serializado, content_type='application/json')
