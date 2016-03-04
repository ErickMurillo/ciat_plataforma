# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ficha'
        db.create_table(u'ficha_sombra_ficha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='persona_productor', to=orm['mapeo.Persona'])),
            ('tecnico', self.gf('django.db.models.fields.related.ForeignKey')(related_name='persona_tecnico', to=orm['mapeo.Persona'])),
            ('fecha_visita', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ficha_sombra', ['Ficha'])

        # Adding model 'Foto1'
        db.create_table(u'ficha_sombra_foto1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Foto1'])

        # Adding model 'Especies'
        db.create_table(u'ficha_sombra_especies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'ficha_sombra', ['Especies'])

        # Adding model 'Punto1'
        db.create_table(u'ficha_sombra_punto1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Especies'])),
            ('pequena', self.gf('django.db.models.fields.FloatField')()),
            ('mediana', self.gf('django.db.models.fields.FloatField')()),
            ('grande', self.gf('django.db.models.fields.FloatField')()),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_de_copa', self.gf('django.db.models.fields.IntegerField')()),
            ('uso', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Punto1'])

        # Adding model 'Cobertura1'
        db.create_table(u'ficha_sombra_cobertura1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cobertura', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Cobertura1'])

        # Adding model 'Foto2'
        db.create_table(u'ficha_sombra_foto2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Foto2'])

        # Adding model 'Punto2'
        db.create_table(u'ficha_sombra_punto2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Especies'])),
            ('pequena', self.gf('django.db.models.fields.FloatField')()),
            ('mediana', self.gf('django.db.models.fields.FloatField')()),
            ('grande', self.gf('django.db.models.fields.FloatField')()),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_de_copa', self.gf('django.db.models.fields.IntegerField')()),
            ('uso', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Punto2'])

        # Adding model 'Cobertura2'
        db.create_table(u'ficha_sombra_cobertura2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cobertura', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Cobertura2'])

        # Adding model 'Foto3'
        db.create_table(u'ficha_sombra_foto3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Foto3'])

        # Adding model 'Punto3'
        db.create_table(u'ficha_sombra_punto3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Especies'])),
            ('pequena', self.gf('django.db.models.fields.FloatField')()),
            ('mediana', self.gf('django.db.models.fields.FloatField')()),
            ('grande', self.gf('django.db.models.fields.FloatField')()),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_de_copa', self.gf('django.db.models.fields.IntegerField')()),
            ('uso', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Punto3'])

        # Adding model 'Cobertura3'
        db.create_table(u'ficha_sombra_cobertura3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cobertura', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Cobertura3'])

        # Adding model 'AnalisisSombra'
        db.create_table(u'ficha_sombra_analisissombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('densidad', self.gf('django.db.models.fields.IntegerField')()),
            ('forma_copa', self.gf('django.db.models.fields.IntegerField')()),
            ('arreglo', self.gf('django.db.models.fields.IntegerField')()),
            ('hojarasca', self.gf('django.db.models.fields.IntegerField')()),
            ('calidad_hojarasca', self.gf('django.db.models.fields.IntegerField')()),
            ('competencia', self.gf('django.db.models.fields.IntegerField')()),
            ('Problema', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['AnalisisSombra'])

        # Adding model 'AccionesSombra'
        db.create_table(u'ficha_sombra_accionessombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['AccionesSombra'])

        # Adding model 'ReducirSombra'
        db.create_table(u'ficha_sombra_reducirsombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poda', self.gf('django.db.models.fields.IntegerField')()),
            ('poda_cuales', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('eliminando', self.gf('django.db.models.fields.IntegerField')()),
            ('eliminando_cuales', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('todo', self.gf('django.db.models.fields.IntegerField')()),
            ('que_parte', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['ReducirSombra'])

        # Adding model 'AumentarSombra'
        db.create_table(u'ficha_sombra_aumentarsombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sembrando', self.gf('django.db.models.fields.IntegerField')()),
            ('sembrando_cuales', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('cambiando', self.gf('django.db.models.fields.IntegerField')()),
            ('cambiando_cuales', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('todo', self.gf('django.db.models.fields.IntegerField')()),
            ('que_parte', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['AumentarSombra'])

        # Adding model 'Manejo'
        db.create_table(u'ficha_sombra_manejo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('herramientas', self.gf('django.db.models.fields.IntegerField')()),
            ('formacion', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_sombra.Ficha'])),
        ))
        db.send_create_signal(u'ficha_sombra', ['Manejo'])


    def backwards(self, orm):
        # Deleting model 'Ficha'
        db.delete_table(u'ficha_sombra_ficha')

        # Deleting model 'Foto1'
        db.delete_table(u'ficha_sombra_foto1')

        # Deleting model 'Especies'
        db.delete_table(u'ficha_sombra_especies')

        # Deleting model 'Punto1'
        db.delete_table(u'ficha_sombra_punto1')

        # Deleting model 'Cobertura1'
        db.delete_table(u'ficha_sombra_cobertura1')

        # Deleting model 'Foto2'
        db.delete_table(u'ficha_sombra_foto2')

        # Deleting model 'Punto2'
        db.delete_table(u'ficha_sombra_punto2')

        # Deleting model 'Cobertura2'
        db.delete_table(u'ficha_sombra_cobertura2')

        # Deleting model 'Foto3'
        db.delete_table(u'ficha_sombra_foto3')

        # Deleting model 'Punto3'
        db.delete_table(u'ficha_sombra_punto3')

        # Deleting model 'Cobertura3'
        db.delete_table(u'ficha_sombra_cobertura3')

        # Deleting model 'AnalisisSombra'
        db.delete_table(u'ficha_sombra_analisissombra')

        # Deleting model 'AccionesSombra'
        db.delete_table(u'ficha_sombra_accionessombra')

        # Deleting model 'ReducirSombra'
        db.delete_table(u'ficha_sombra_reducirsombra')

        # Deleting model 'AumentarSombra'
        db.delete_table(u'ficha_sombra_aumentarsombra')

        # Deleting model 'Manejo'
        db.delete_table(u'ficha_sombra_manejo')


    models = {
        u'ficha_sombra.accionessombra': {
            'Meta': {'object_name': 'AccionesSombra'},
            'accion': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_sombra.analisissombra': {
            'Meta': {'object_name': 'AnalisisSombra'},
            'Problema': ('django.db.models.fields.IntegerField', [], {}),
            'arreglo': ('django.db.models.fields.IntegerField', [], {}),
            'calidad_hojarasca': ('django.db.models.fields.IntegerField', [], {}),
            'competencia': ('django.db.models.fields.IntegerField', [], {}),
            'densidad': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            'forma_copa': ('django.db.models.fields.IntegerField', [], {}),
            'hojarasca': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_sombra.aumentarsombra': {
            'Meta': {'object_name': 'AumentarSombra'},
            'cambiando': ('django.db.models.fields.IntegerField', [], {}),
            'cambiando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'que_parte': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sembrando': ('django.db.models.fields.IntegerField', [], {}),
            'sembrando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'todo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_sombra.cobertura1': {
            'Meta': {'object_name': 'Cobertura1'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_sombra.cobertura2': {
            'Meta': {'object_name': 'Cobertura2'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_sombra.cobertura3': {
            'Meta': {'object_name': 'Cobertura3'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_sombra.especies': {
            'Meta': {'object_name': 'Especies'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'ficha_sombra.ficha': {
            'Meta': {'object_name': 'Ficha'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico'", 'to': u"orm['mapeo.Persona']"})
        },
        u'ficha_sombra.foto1': {
            'Meta': {'object_name': 'Foto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_sombra.foto2': {
            'Meta': {'object_name': 'Foto2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_sombra.foto3': {
            'Meta': {'object_name': 'Foto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_sombra.manejo': {
            'Meta': {'object_name': 'Manejo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {}),
            'herramientas': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_sombra.punto1': {
            'Meta': {'object_name': 'Punto1'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_sombra.punto2': {
            'Meta': {'object_name': 'Punto2'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_sombra.punto3': {
            'Meta': {'object_name': 'Punto3'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_sombra.reducirsombra': {
            'Meta': {'object_name': 'ReducirSombra'},
            'eliminando': ('django.db.models.fields.IntegerField', [], {}),
            'eliminando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_sombra.Ficha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poda': ('django.db.models.fields.IntegerField', [], {}),
            'poda_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'que_parte': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'todo': ('django.db.models.fields.IntegerField', [], {})
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

    complete_apps = ['ficha_sombra']