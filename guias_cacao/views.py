# -*- coding: UTF-8 -*-
from django.shortcuts import render
from .forms import ConsultaSombraForm
from .models import FichaSombra, FichaPoda, FichaPlaga, FichaPiso
# Create your views here.

def _queryset_filtrado_sombra(request):
    params = {}

    if 'fecha' in request.session:
       params['fecha_visita__year'] = request.session['fecha']

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
            del request.session['fecha']
            del request.session['organizacion']
            del request.session['pais']
            del request.session['departamento']
            del request.session['municipio']
            del request.session['comunidad']
            del request.session['sexo']
            del request.session['tipologia']

    return render(request, template, {'form': form, 'centinela': centinela})


def sombra_riqueza(request, template="guiascacao/sombra_riqueza.html"):
    filtro = _queryset_filtrado_sombra(request)
    print filtro
    return render(request, template, locals())
