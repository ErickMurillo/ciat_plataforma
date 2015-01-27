from selectable.base import ModelLookup
from selectable.registry import registry
from mapeo.models import Persona

class ProductorLookup(ModelLookup):
    model = Persona
    search_fields = ('nombre__icontains', )

registry.register(ProductorLookup)