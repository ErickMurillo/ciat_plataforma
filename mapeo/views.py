from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import MapeoConsulta, MapaConsulta
import json

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

            return HttpResponseRedirect('proyectos/')
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

    return render(request, template, locals())


def proyectos(request, template="mapeo/proyectos.html"):

    proyectos = _queryset_filtrado(request)

    return render(request, template, locals())

def mapa_actores(request, template="mapeo/mapa.html", id_proyecto=None):

    el_proyecto = Proyectos.objects.get(id=id_proyecto)
    form_mapa = MapaConsulta()

    return render(request, template, locals())


def obtener_mapa(request, id_proyecto=None):
    todos_productores = Productor.objects.filter(proyecto__id=id_proyecto)
    todos_lideres = Lideres.objects.filter(proyecto__id=id_proyecto)
    todos_tecnicoespinvestigador = TecnicoEspInvestigador.objects.filter(proyecto__id=id_proyecto)
    todos_decisor = Decisor.objects.filter(proyecto__id=id_proyecto)

    #todos_juntos = pass
    print "aca esta el comentarios"
    print request.POST
    if request.is_ajax():
        lista = []
        print request.POST

        params = []
        # if request.POST['tipo_persona'] == 0:
        #     params = consulta.filter(fkmercado__departamento__id=request.POST['depart'])
        # else:
        #     params = ActividadMercado.objects.filter(fkmercado__departamento__id=request.POST['depart'])
        for objeto in params:
            dicc = dict(nombre=objeto.fkmercado.nombre_mercado,
                        id=objeto.id,
                        idm = float(objeto.fkmercado.id),
                        lon=float(objeto.fkmercado.municipio.longitud) ,
                        lat=float(objeto.fkmercado.municipio.latitud),
                        periodicidad=objeto.periodicidad.nombre,
                        modalidad=objeto.get_modalidad_display(),
                        )
            lista.append(dicc)

        serializado = json.dumps(lista)
        return HttpResponse(serializado, content_type='application/json')
