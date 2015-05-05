from comunicacion.foros.models import Imagen


def globales(request):

    imagenes_global = Imagen.objects.all()[:9]

    return {'imagenes_global':imagenes_global}