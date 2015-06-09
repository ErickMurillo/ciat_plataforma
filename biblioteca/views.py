from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Biblioteca

# Create your views here.

class IndexView(TemplateView):
    template_name = "biblioteca/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['libros'] = Biblioteca.objects.all()

        return context