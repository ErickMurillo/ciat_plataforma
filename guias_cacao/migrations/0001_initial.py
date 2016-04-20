# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FichaSombra'
        db.create_table(u'guias_cacao_fichasombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='persona_productor', to=orm['mapeo.Persona'])),
            ('tecnico', self.gf('django.db.models.fields.related.ForeignKey')(related_name='persona_tecnico', to=orm['mapeo.Persona'])),
            ('fecha_visita', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'guias_cacao', ['FichaSombra'])

        # Adding model 'Foto1'
        db.create_table(u'guias_cacao_foto1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Foto1'])

        # Adding model 'Especies'
        db.create_table(u'guias_cacao_especies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'guias_cacao', ['Especies'])

        # Adding model 'Punto1'
        db.create_table(u'guias_cacao_punto1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.Especies'])),
            ('pequena', self.gf('django.db.models.fields.FloatField')()),
            ('mediana', self.gf('django.db.models.fields.FloatField')()),
            ('grande', self.gf('django.db.models.fields.FloatField')()),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_de_copa', self.gf('django.db.models.fields.IntegerField')()),
            ('uso', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto1'])

        # Adding model 'Cobertura1'
        db.create_table(u'guias_cacao_cobertura1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cobertura', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Cobertura1'])

        # Adding model 'Foto2'
        db.create_table(u'guias_cacao_foto2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Foto2'])

        # Adding model 'Punto2'
        db.create_table(u'guias_cacao_punto2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.Especies'])),
            ('pequena', self.gf('django.db.models.fields.FloatField')()),
            ('mediana', self.gf('django.db.models.fields.FloatField')()),
            ('grande', self.gf('django.db.models.fields.FloatField')()),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_de_copa', self.gf('django.db.models.fields.IntegerField')()),
            ('uso', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto2'])

        # Adding model 'Cobertura2'
        db.create_table(u'guias_cacao_cobertura2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cobertura', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Cobertura2'])

        # Adding model 'Foto3'
        db.create_table(u'guias_cacao_foto3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Foto3'])

        # Adding model 'Punto3'
        db.create_table(u'guias_cacao_punto3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.Especies'])),
            ('pequena', self.gf('django.db.models.fields.FloatField')()),
            ('mediana', self.gf('django.db.models.fields.FloatField')()),
            ('grande', self.gf('django.db.models.fields.FloatField')()),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_de_copa', self.gf('django.db.models.fields.IntegerField')()),
            ('uso', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto3'])

        # Adding model 'Cobertura3'
        db.create_table(u'guias_cacao_cobertura3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cobertura', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Cobertura3'])

        # Adding model 'AnalisisSombra'
        db.create_table(u'guias_cacao_analisissombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('densidad', self.gf('django.db.models.fields.IntegerField')()),
            ('forma_copa', self.gf('django.db.models.fields.IntegerField')()),
            ('arreglo', self.gf('django.db.models.fields.IntegerField')()),
            ('hojarasca', self.gf('django.db.models.fields.IntegerField')()),
            ('calidad_hojarasca', self.gf('django.db.models.fields.IntegerField')()),
            ('competencia', self.gf('django.db.models.fields.IntegerField')()),
            ('Problema', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['AnalisisSombra'])

        # Adding model 'AccionesSombra'
        db.create_table(u'guias_cacao_accionessombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['AccionesSombra'])

        # Adding model 'ReducirSombra'
        db.create_table(u'guias_cacao_reducirsombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poda', self.gf('django.db.models.fields.IntegerField')()),
            ('poda_cuales', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('eliminando', self.gf('django.db.models.fields.IntegerField')()),
            ('eliminando_cuales', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('todo', self.gf('django.db.models.fields.IntegerField')()),
            ('que_parte', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['ReducirSombra'])

        # Adding model 'AumentarSombra'
        db.create_table(u'guias_cacao_aumentarsombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sembrando', self.gf('django.db.models.fields.IntegerField')()),
            ('sembrando_cuales', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('cambiando', self.gf('django.db.models.fields.IntegerField')()),
            ('cambiando_cuales', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('todo', self.gf('django.db.models.fields.IntegerField')()),
            ('que_parte', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['AumentarSombra'])

        # Adding model 'ManejoSombra'
        db.create_table(u'guias_cacao_manejosombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('herramientas', self.gf('django.db.models.fields.IntegerField')()),
            ('formacion', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSombra'])),
        ))
        db.send_create_signal(u'guias_cacao', ['ManejoSombra'])

        # Adding model 'FichaPoda'
        db.create_table(u'guias_cacao_fichapoda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='setproductor', to=orm['mapeo.Persona'])),
            ('tecnico', self.gf('django.db.models.fields.related.ForeignKey')(related_name='settecnico', to=orm['mapeo.Persona'])),
            ('fecha_visita', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'guias_cacao', ['FichaPoda'])

        # Adding model 'Punto1A'
        db.create_table(u'guias_cacao_punto1a', (
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
            ('diez', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto1A'])

        # Adding model 'Punto1B'
        db.create_table(u'guias_cacao_punto1b', (
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
            ('diez', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto1B'])

        # Adding model 'Punto1C'
        db.create_table(u'guias_cacao_punto1c', (
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
            ('diez', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto1C'])

        # Adding model 'Punto2A'
        db.create_table(u'guias_cacao_punto2a', (
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
            ('diez', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto2A'])

        # Adding model 'Punto2B'
        db.create_table(u'guias_cacao_punto2b', (
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
            ('diez', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto2B'])

        # Adding model 'Punto2C'
        db.create_table(u'guias_cacao_punto2c', (
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
            ('diez', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto2C'])

        # Adding model 'Punto3A'
        db.create_table(u'guias_cacao_punto3a', (
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
            ('diez', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto3A'])

        # Adding model 'Punto3B'
        db.create_table(u'guias_cacao_punto3b', (
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
            ('diez', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto3B'])

        # Adding model 'Punto3C'
        db.create_table(u'guias_cacao_punto3c', (
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
            ('diez', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto3C'])

        # Adding model 'AnalisisPoda'
        db.create_table(u'guias_cacao_analisispoda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campo1', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=15)),
            ('campo2', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11)),
            ('campo3', self.gf('django.db.models.fields.IntegerField')()),
            ('campo4', self.gf('django.db.models.fields.IntegerField')()),
            ('campo5', self.gf('django.db.models.fields.IntegerField')()),
            ('campo6', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=23)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['AnalisisPoda'])

        # Adding model 'ManejoPoda'
        db.create_table(u'guias_cacao_manejopoda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('herramientas', self.gf('django.db.models.fields.IntegerField')()),
            ('formacion', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaPoda'])),
        ))
        db.send_create_signal(u'guias_cacao', ['ManejoPoda'])


    def backwards(self, orm):
        # Deleting model 'FichaSombra'
        db.delete_table(u'guias_cacao_fichasombra')

        # Deleting model 'Foto1'
        db.delete_table(u'guias_cacao_foto1')

        # Deleting model 'Especies'
        db.delete_table(u'guias_cacao_especies')

        # Deleting model 'Punto1'
        db.delete_table(u'guias_cacao_punto1')

        # Deleting model 'Cobertura1'
        db.delete_table(u'guias_cacao_cobertura1')

        # Deleting model 'Foto2'
        db.delete_table(u'guias_cacao_foto2')

        # Deleting model 'Punto2'
        db.delete_table(u'guias_cacao_punto2')

        # Deleting model 'Cobertura2'
        db.delete_table(u'guias_cacao_cobertura2')

        # Deleting model 'Foto3'
        db.delete_table(u'guias_cacao_foto3')

        # Deleting model 'Punto3'
        db.delete_table(u'guias_cacao_punto3')

        # Deleting model 'Cobertura3'
        db.delete_table(u'guias_cacao_cobertura3')

        # Deleting model 'AnalisisSombra'
        db.delete_table(u'guias_cacao_analisissombra')

        # Deleting model 'AccionesSombra'
        db.delete_table(u'guias_cacao_accionessombra')

        # Deleting model 'ReducirSombra'
        db.delete_table(u'guias_cacao_reducirsombra')

        # Deleting model 'AumentarSombra'
        db.delete_table(u'guias_cacao_aumentarsombra')

        # Deleting model 'ManejoSombra'
        db.delete_table(u'guias_cacao_manejosombra')

        # Deleting model 'FichaPoda'
        db.delete_table(u'guias_cacao_fichapoda')

        # Deleting model 'Punto1A'
        db.delete_table(u'guias_cacao_punto1a')

        # Deleting model 'Punto1B'
        db.delete_table(u'guias_cacao_punto1b')

        # Deleting model 'Punto1C'
        db.delete_table(u'guias_cacao_punto1c')

        # Deleting model 'Punto2A'
        db.delete_table(u'guias_cacao_punto2a')

        # Deleting model 'Punto2B'
        db.delete_table(u'guias_cacao_punto2b')

        # Deleting model 'Punto2C'
        db.delete_table(u'guias_cacao_punto2c')

        # Deleting model 'Punto3A'
        db.delete_table(u'guias_cacao_punto3a')

        # Deleting model 'Punto3B'
        db.delete_table(u'guias_cacao_punto3b')

        # Deleting model 'Punto3C'
        db.delete_table(u'guias_cacao_punto3c')

        # Deleting model 'AnalisisPoda'
        db.delete_table(u'guias_cacao_analisispoda')

        # Deleting model 'ManejoPoda'
        db.delete_table(u'guias_cacao_manejopoda')


    models = {
        u'guias_cacao.accionessombra': {
            'Meta': {'object_name': 'AccionesSombra'},
            'accion': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.analisispoda': {
            'Meta': {'object_name': 'AnalisisPoda'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'campo3': ('django.db.models.fields.IntegerField', [], {}),
            'campo4': ('django.db.models.fields.IntegerField', [], {}),
            'campo5': ('django.db.models.fields.IntegerField', [], {}),
            'campo6': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.analisissombra': {
            'Meta': {'object_name': 'AnalisisSombra'},
            'Problema': ('django.db.models.fields.IntegerField', [], {}),
            'arreglo': ('django.db.models.fields.IntegerField', [], {}),
            'calidad_hojarasca': ('django.db.models.fields.IntegerField', [], {}),
            'competencia': ('django.db.models.fields.IntegerField', [], {}),
            'densidad': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'forma_copa': ('django.db.models.fields.IntegerField', [], {}),
            'hojarasca': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.aumentarsombra': {
            'Meta': {'object_name': 'AumentarSombra'},
            'cambiando': ('django.db.models.fields.IntegerField', [], {}),
            'cambiando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'que_parte': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sembrando': ('django.db.models.fields.IntegerField', [], {}),
            'sembrando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'todo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cobertura1': {
            'Meta': {'object_name': 'Cobertura1'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cobertura2': {
            'Meta': {'object_name': 'Cobertura2'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cobertura3': {
            'Meta': {'object_name': 'Cobertura3'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.especies': {
            'Meta': {'object_name': 'Especies'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'guias_cacao.fichapoda': {
            'Meta': {'object_name': 'FichaPoda'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'setproductor'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'settecnico'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichasombra': {
            'Meta': {'object_name': 'FichaSombra'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.foto1': {
            'Meta': {'object_name': 'Foto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.foto2': {
            'Meta': {'object_name': 'Foto2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.foto3': {
            'Meta': {'object_name': 'Foto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.manejopoda': {
            'Meta': {'object_name': 'ManejoPoda'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {}),
            'herramientas': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.manejosombra': {
            'Meta': {'object_name': 'ManejoSombra'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {}),
            'herramientas': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.punto1': {
            'Meta': {'object_name': 'Punto1'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto1a': {
            'Meta': {'object_name': 'Punto1A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.punto1b': {
            'Meta': {'object_name': 'Punto1B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto1c': {
            'Meta': {'object_name': 'Punto1C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2': {
            'Meta': {'object_name': 'Punto2'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2a': {
            'Meta': {'object_name': 'Punto2A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.punto2b': {
            'Meta': {'object_name': 'Punto2B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2c': {
            'Meta': {'object_name': 'Punto2C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3': {
            'Meta': {'object_name': 'Punto3'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3a': {
            'Meta': {'object_name': 'Punto3A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.punto3b': {
            'Meta': {'object_name': 'Punto3B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3c': {
            'Meta': {'object_name': 'Punto3C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.reducirsombra': {
            'Meta': {'object_name': 'ReducirSombra'},
            'eliminando': ('django.db.models.fields.IntegerField', [], {}),
            'eliminando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
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

    complete_apps = ['guias_cacao']