# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ficha'
        db.create_table(u'ficha_poda_ficha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='setproductor', to=orm['mapeo.Persona'])),
            ('tecnico', self.gf('django.db.models.fields.related.ForeignKey')(related_name='settecnico', to=orm['mapeo.Persona'])),
            ('fecha_visita', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ficha_poda', ['Ficha'])

        # Adding model 'Punto1A'
        db.create_table(u'ficha_poda_punto1a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('uno', self.gf('django.db.models.fields.FloatField')()),
            ('dos', self.gf('django.db.models.fields.FloatField')()),
            ('tres', self.gf('django.db.models.fields.FloatField')()),
            ('cuatro', self.gf('django.db.models.fields.FloatField')()),
            ('cinco', self.gf('django.db.models.fields.FloatField')()),
            ('seis', self.gf('django.db.models.fields.FloatField')()),
            ('siete', self.gf('django.db.models.fields.FloatField')()),
            ('ocho', self.gf('django.db.models.fields.FloatField')()),
            ('nueve', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['Punto1A'])

        # Adding model 'Punto1B'
        db.create_table(u'ficha_poda_punto1b', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('uno', self.gf('django.db.models.fields.IntegerField')()),
            ('dos', self.gf('django.db.models.fields.IntegerField')()),
            ('tres', self.gf('django.db.models.fields.IntegerField')()),
            ('cuatro', self.gf('django.db.models.fields.IntegerField')()),
            ('cinco', self.gf('django.db.models.fields.IntegerField')()),
            ('seis', self.gf('django.db.models.fields.IntegerField')()),
            ('siete', self.gf('django.db.models.fields.IntegerField')()),
            ('ocho', self.gf('django.db.models.fields.IntegerField')()),
            ('nueve', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['Punto1B'])

        # Adding model 'Punto1C'
        db.create_table(u'ficha_poda_punto1c', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('uno', self.gf('django.db.models.fields.IntegerField')()),
            ('dos', self.gf('django.db.models.fields.IntegerField')()),
            ('tres', self.gf('django.db.models.fields.IntegerField')()),
            ('cuatro', self.gf('django.db.models.fields.IntegerField')()),
            ('cinco', self.gf('django.db.models.fields.IntegerField')()),
            ('seis', self.gf('django.db.models.fields.IntegerField')()),
            ('siete', self.gf('django.db.models.fields.IntegerField')()),
            ('ocho', self.gf('django.db.models.fields.IntegerField')()),
            ('nueve', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['Punto1C'])

        # Adding model 'Punto2A'
        db.create_table(u'ficha_poda_punto2a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('uno', self.gf('django.db.models.fields.FloatField')()),
            ('dos', self.gf('django.db.models.fields.FloatField')()),
            ('tres', self.gf('django.db.models.fields.FloatField')()),
            ('cuatro', self.gf('django.db.models.fields.FloatField')()),
            ('cinco', self.gf('django.db.models.fields.FloatField')()),
            ('seis', self.gf('django.db.models.fields.FloatField')()),
            ('siete', self.gf('django.db.models.fields.FloatField')()),
            ('ocho', self.gf('django.db.models.fields.FloatField')()),
            ('nueve', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['Punto2A'])

        # Adding model 'Punto2B'
        db.create_table(u'ficha_poda_punto2b', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('uno', self.gf('django.db.models.fields.IntegerField')()),
            ('dos', self.gf('django.db.models.fields.IntegerField')()),
            ('tres', self.gf('django.db.models.fields.IntegerField')()),
            ('cuatro', self.gf('django.db.models.fields.IntegerField')()),
            ('cinco', self.gf('django.db.models.fields.IntegerField')()),
            ('seis', self.gf('django.db.models.fields.IntegerField')()),
            ('siete', self.gf('django.db.models.fields.IntegerField')()),
            ('ocho', self.gf('django.db.models.fields.IntegerField')()),
            ('nueve', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['Punto2B'])

        # Adding model 'Punto2C'
        db.create_table(u'ficha_poda_punto2c', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('uno', self.gf('django.db.models.fields.IntegerField')()),
            ('dos', self.gf('django.db.models.fields.IntegerField')()),
            ('tres', self.gf('django.db.models.fields.IntegerField')()),
            ('cuatro', self.gf('django.db.models.fields.IntegerField')()),
            ('cinco', self.gf('django.db.models.fields.IntegerField')()),
            ('seis', self.gf('django.db.models.fields.IntegerField')()),
            ('siete', self.gf('django.db.models.fields.IntegerField')()),
            ('ocho', self.gf('django.db.models.fields.IntegerField')()),
            ('nueve', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['Punto2C'])

        # Adding model 'Punto3A'
        db.create_table(u'ficha_poda_punto3a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('uno', self.gf('django.db.models.fields.FloatField')()),
            ('dos', self.gf('django.db.models.fields.FloatField')()),
            ('tres', self.gf('django.db.models.fields.FloatField')()),
            ('cuatro', self.gf('django.db.models.fields.FloatField')()),
            ('cinco', self.gf('django.db.models.fields.FloatField')()),
            ('seis', self.gf('django.db.models.fields.FloatField')()),
            ('siete', self.gf('django.db.models.fields.FloatField')()),
            ('ocho', self.gf('django.db.models.fields.FloatField')()),
            ('nueve', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['Punto3A'])

        # Adding model 'Punto3B'
        db.create_table(u'ficha_poda_punto3b', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('uno', self.gf('django.db.models.fields.IntegerField')()),
            ('dos', self.gf('django.db.models.fields.IntegerField')()),
            ('tres', self.gf('django.db.models.fields.IntegerField')()),
            ('cuatro', self.gf('django.db.models.fields.IntegerField')()),
            ('cinco', self.gf('django.db.models.fields.IntegerField')()),
            ('seis', self.gf('django.db.models.fields.IntegerField')()),
            ('siete', self.gf('django.db.models.fields.IntegerField')()),
            ('ocho', self.gf('django.db.models.fields.IntegerField')()),
            ('nueve', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['Punto3B'])

        # Adding model 'Punto3C'
        db.create_table(u'ficha_poda_punto3c', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('uno', self.gf('django.db.models.fields.IntegerField')()),
            ('dos', self.gf('django.db.models.fields.IntegerField')()),
            ('tres', self.gf('django.db.models.fields.IntegerField')()),
            ('cuatro', self.gf('django.db.models.fields.IntegerField')()),
            ('cinco', self.gf('django.db.models.fields.IntegerField')()),
            ('seis', self.gf('django.db.models.fields.IntegerField')()),
            ('siete', self.gf('django.db.models.fields.IntegerField')()),
            ('ocho', self.gf('django.db.models.fields.IntegerField')()),
            ('nueve', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['Punto3C'])

        # Adding model 'AnalisisPoda'
        db.create_table(u'ficha_poda_analisispoda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campo1', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=15)),
            ('campo2', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11)),
            ('campo3', self.gf('django.db.models.fields.IntegerField')()),
            ('campo4', self.gf('django.db.models.fields.IntegerField')()),
            ('campo5', self.gf('django.db.models.fields.IntegerField')()),
            ('campo6', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=23)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_poda.Ficha'])),
        ))
        db.send_create_signal(u'ficha_poda', ['AnalisisPoda'])


    def backwards(self, orm):
        # Deleting model 'Ficha'
        db.delete_table(u'ficha_poda_ficha')

        # Deleting model 'Punto1A'
        db.delete_table(u'ficha_poda_punto1a')

        # Deleting model 'Punto1B'
        db.delete_table(u'ficha_poda_punto1b')

        # Deleting model 'Punto1C'
        db.delete_table(u'ficha_poda_punto1c')

        # Deleting model 'Punto2A'
        db.delete_table(u'ficha_poda_punto2a')

        # Deleting model 'Punto2B'
        db.delete_table(u'ficha_poda_punto2b')

        # Deleting model 'Punto2C'
        db.delete_table(u'ficha_poda_punto2c')

        # Deleting model 'Punto3A'
        db.delete_table(u'ficha_poda_punto3a')

        # Deleting model 'Punto3B'
        db.delete_table(u'ficha_poda_punto3b')

        # Deleting model 'Punto3C'
        db.delete_table(u'ficha_poda_punto3c')

        # Deleting model 'AnalisisPoda'
        db.delete_table(u'ficha_poda_analisispoda')


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