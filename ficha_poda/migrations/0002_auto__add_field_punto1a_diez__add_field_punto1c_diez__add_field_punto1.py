# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Punto1A.diez'
        db.add_column(u'ficha_poda_punto1a', 'diez',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Punto1C.diez'
        db.add_column(u'ficha_poda_punto1c', 'diez',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Punto1B.diez'
        db.add_column(u'ficha_poda_punto1b', 'diez',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Punto2A.diez'
        db.add_column(u'ficha_poda_punto2a', 'diez',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Punto2B.diez'
        db.add_column(u'ficha_poda_punto2b', 'diez',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Punto3C.diez'
        db.add_column(u'ficha_poda_punto3c', 'diez',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Punto3B.diez'
        db.add_column(u'ficha_poda_punto3b', 'diez',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Punto3A.diez'
        db.add_column(u'ficha_poda_punto3a', 'diez',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Punto2C.diez'
        db.add_column(u'ficha_poda_punto2c', 'diez',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Punto1A.diez'
        db.delete_column(u'ficha_poda_punto1a', 'diez')

        # Deleting field 'Punto1C.diez'
        db.delete_column(u'ficha_poda_punto1c', 'diez')

        # Deleting field 'Punto1B.diez'
        db.delete_column(u'ficha_poda_punto1b', 'diez')

        # Deleting field 'Punto2A.diez'
        db.delete_column(u'ficha_poda_punto2a', 'diez')

        # Deleting field 'Punto2B.diez'
        db.delete_column(u'ficha_poda_punto2b', 'diez')

        # Deleting field 'Punto3C.diez'
        db.delete_column(u'ficha_poda_punto3c', 'diez')

        # Deleting field 'Punto3B.diez'
        db.delete_column(u'ficha_poda_punto3b', 'diez')

        # Deleting field 'Punto3A.diez'
        db.delete_column(u'ficha_poda_punto3a', 'diez')

        # Deleting field 'Punto2C.diez'
        db.delete_column(u'ficha_poda_punto2c', 'diez')


    models = {
        u'ficha_poda.analisispoda': {
            'Meta': {'object_name': 'AnalisisPoda'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'campo3': ('django.db.models.fields.IntegerField', [], {}),
            'campo4': ('django.db.models.fields.IntegerField', [], {}),
            'campo5': ('django.db.models.fields.IntegerField', [], {}),
            'campo6': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_poda.ficha': {
            'Meta': {'object_name': 'Ficha'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'setproductor'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'settecnico'", 'to': u"orm['mapeo.Persona']"})
        },
        u'ficha_poda.punto1a': {
            'Meta': {'object_name': 'Punto1A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_poda.punto1b': {
            'Meta': {'object_name': 'Punto1B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_poda.punto1c': {
            'Meta': {'object_name': 'Punto1C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_poda.punto2a': {
            'Meta': {'object_name': 'Punto2A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_poda.punto2b': {
            'Meta': {'object_name': 'Punto2B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_poda.punto2c': {
            'Meta': {'object_name': 'Punto2C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_poda.punto3a': {
            'Meta': {'object_name': 'Punto3A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_poda.punto3b': {
            'Meta': {'object_name': 'Punto3B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_poda.punto3c': {
            'Meta': {'object_name': 'Punto3C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_poda.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'lugar.comunidad': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Comunidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'lugar.departamento': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre', 'nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.pais': {
            'Meta': {'object_name': 'Pais'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mapeo.persona': {
            'Meta': {'object_name': 'Persona'},
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Comunidad']"}),
            'departamento': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_persona': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ficha_poda']