from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import MapeoConsulta

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

def mapa_actores(request, template="mapeo/mapa.html", proyecto=None):

    return render(request, template, locals())
