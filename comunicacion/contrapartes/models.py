# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from comunicacion.utils import *
from south.modelsinspector import add_introspection_rules
from ckeditor.fields import RichTextField
import datetime
from comunicacion.lugar.models import *
from sorl.thumbnail import ImageField
from mapeo.models import Organizaciones

add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

add_introspection_rules ([], ["^contrapartes\.models\.ColorField"])

# Create your models here.

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # Other fields here
    contraparte = models.ForeignKey(Organizaciones)
    avatar = ImageField(upload_to=get_file_path,
                                   null=True, blank=True)
    fileDir = 'usuario/avatar/'

    def __unicode__(self):
        return u"%s - %s" % (self.user.username, self.contraparte.nombre)

    def get_absolute_url(self):
        return '/usuario/%d/' % (self.user.id)

class Mensajero(models.Model):
    user = models.ManyToManyField(User)
    fecha = models.DateField(default=datetime.date.today())
    mensaje = RichTextField()
    usuario = models.CharField(max_length=200,blank=True, null=True)

    def __unicode__(self):
        return u'%s - %s ' % (self.fecha, self.mensaje)
