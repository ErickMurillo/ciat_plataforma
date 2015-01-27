# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.contenttypes import generic
from comunicacion.contrapartes.models import *
from comunicacion.foros.models import *
from django.template.defaultfilters import slugify
from south.modelsinspector import add_introspection_rules
from ckeditor.fields import RichTextField

add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

# Create your models here.
class Temas(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

class Notas(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    fecha = models.DateField('Fecha de publicación', auto_now_add=True)
    contenido = RichTextField()
    temas = models.ManyToManyField(Temas)
    fotos = generic.GenericRelation(Imagen)
    adjuntos = generic.GenericRelation(Documentos)
    video = generic.GenericRelation(Videos)
    audio = generic.GenericRelation(Audios)

    user = models.ForeignKey(User)

    class Meta:
    	verbose_name_plural = "Noticias"
        ordering = ['-fecha','-id']

    def __unicode__(self):
    	return self.titulo

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.titulo)
        return super(Notas, self).save(*args, **kwargs)

    def imagenes(self):
        imagenes = Imagen.objects.filter(object_id=self.id)
        return imagenes

    def adjunto(self):
        adjunto = Documentos.objects.filter(object_id=self.id)
        return adjunto

    def get_absolute_url(self):
    	return '/comunicacion/%d/' % (self.id,)
    # Para obtener el pais de la noticia
    def pais(self):
        usuario = UserProfile.objects.get(pk=self.user.id)
        contraparte = Contraparte.objects.get(pk=usuario.contraparte.id)
        pais = Pais.objects.get(pk=contraparte.pais.id)
        return pais

    # Para obtener la contraparte de la noticia
    def contraparte(self):
        usuario = UserProfile.objects.get(pk=self.user.id)
        contraparte = Contraparte.objects.get(pk=usuario.contraparte.id)
        return contraparte

class ComentarioNotas(models.Model):
    nota = models.ForeignKey(Notas)
    fecha = models.DateField(default=datetime.datetime.now())
    user = models.ForeignKey(User)
    comentario = RichTextField()

    def __unicode__(self):
        return self.user.username
