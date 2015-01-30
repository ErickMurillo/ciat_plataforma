# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Aliados'
        db.create_table(u'aliados_aliados', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('siglas', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('logo', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Pais'])),
            ('fundacion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('temas', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('generalidades', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('contacto', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('sitio_web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('rss', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'aliados', ['Aliados'])

        # Adding unique constraint on 'Aliados', fields ['nombre']
        db.create_unique(u'aliados_aliados', ['nombre'])


    def backwards(self, orm):
        # Removing unique constraint on 'Aliados', fields ['nombre']
        db.delete_unique(u'aliados_aliados', ['nombre'])

        # Deleting model 'Aliados'
        db.delete_table(u'aliados_aliados')


    models = {
        u'aliados.aliados': {
            'Meta': {'unique_together': "(('nombre',),)", 'object_name': 'Aliados'},
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fundacion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'generalidades': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'rss': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'siglas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'temas': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'lugar.pais': {
            'Meta': {'object_name': 'Pais'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['aliados']