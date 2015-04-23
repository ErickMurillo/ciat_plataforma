from django.db import models
from sorl.thumbnail import ImageField
from comunicacion.utils import get_file_path

# Create your models here.

class Producto_Proceso(models.Model):
	titulo  = models.CharField(max_length=200)
	descripcion = models.TextField()
	imagen = ImageField(upload_to=get_file_path, null=True, blank=True)
	url  = models.URLField()


	fileDir = 'producto_proceso/'

	class Meta:
		verbose_name='Productos y Procesos'
		verbose_name_plural='Productos y Procesos'

	def __unicode__(self):
		return self.titulo

