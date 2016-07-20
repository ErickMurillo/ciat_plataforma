# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def _queryset_filtrado(request):
	params = {}

	if request.session['year']:
		params['year__in'] = request.session['year']

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

	return Monitoreo.objects.filter(**params).order_by('anio')

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

			# return HttpResponseRedirect('/productores/dashboard/')

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
