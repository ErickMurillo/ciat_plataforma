from selectable.base import ModelLookup
from selectable.registry import registry
from mapeo.models import Persona

class ProductorLookup(ModelLookup):
    model = Persona
    search_fields = ('nombre__icontains', )
    filters = {'tipo_persona__in': [1,2], }

class TecnicoLookup(ModelLookup):
    model = Persona
    search_fields = ('nombre__icontains', )
    filters = {'tipo_persona': 3, }

registry.register(ProductorLookup)
registry.register(TecnicoLookup)
