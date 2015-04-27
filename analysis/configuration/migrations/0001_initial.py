# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AreaAccion'
        db.create_table(u'configuration_areaaccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'configuration', ['AreaAccion'])

        # Adding model 'SitioAccion'
        db.create_table(u'configuration_sitioaccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('area_accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuration.AreaAccion'])),
        ))
        db.send_create_signal(u'configuration', ['SitioAccion'])

        # Adding model 'Plataforma'
        db.create_table(u'configuration_plataforma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('sitio_accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuration.SitioAccion'])),
        ))
        db.send_create_signal(u'configuration', ['Plataforma'])

        # Adding model 'Status_Legal'
        db.create_table(u'configuration_status_legal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'configuration', ['Status_Legal'])

        # Adding model 'Sector'
        db.create_table(u'configuration_sector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'configuration', ['Sector'])

        # Adding model 'Ubicacion'
        db.create_table(u'configuration_ubicacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'configuration', ['Ubicacion'])

        # Adding model 'Tema'
        db.create_table(u'configuration_tema', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tema', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'configuration', ['Tema'])

        # Adding model 'Grupo'
        db.create_table(u'configuration_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Grupo'])

        # Adding model 'Grupo_Beneficiario'
        db.create_table(u'configuration_grupo_beneficiario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Grupo_Beneficiario'])

        # Adding model 'Papel'
        db.create_table(u'configuration_papel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Papel'])

        # Adding model 'Categoria'
        db.create_table(u'configuration_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Categoria'])

        # Adding model 'Categoria_Innovacion'
        db.create_table(u'configuration_categoria_innovacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Categoria_Innovacion'])

        # Adding model 'Categoria_Conocimiento'
        db.create_table(u'configuration_categoria_conocimiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Categoria_Conocimiento'])

        # Adding model 'Categoria_Fuente'
        db.create_table(u'configuration_categoria_fuente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Categoria_Fuente'])

        # Adding model 'Seleccion_7a'
        db.create_table(u'configuration_seleccion_7a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Seleccion_7a'])

        # Adding model 'Seleccion_7b'
        db.create_table(u'configuration_seleccion_7b', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Seleccion_7b'])

        # Adding model 'Tipo_Estudio'
        db.create_table(u'configuration_tipo_estudio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Tipo_Estudio'])

        # Adding model 'Tema_Relacion'
        db.create_table(u'configuration_tema_relacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['Tema_Relacion'])


    def backwards(self, orm):
        # Deleting model 'AreaAccion'
        db.delete_table(u'configuration_areaaccion')

        # Deleting model 'SitioAccion'
        db.delete_table(u'configuration_sitioaccion')

        # Deleting model 'Plataforma'
        db.delete_table(u'configuration_plataforma')

        # Deleting model 'Status_Legal'
        db.delete_table(u'configuration_status_legal')

        # Deleting model 'Sector'
        db.delete_table(u'configuration_sector')

        # Deleting model 'Ubicacion'
        db.delete_table(u'configuration_ubicacion')

        # Deleting model 'Tema'
        db.delete_table(u'configuration_tema')

        # Deleting model 'Grupo'
        db.delete_table(u'configuration_grupo')

        # Deleting model 'Grupo_Beneficiario'
        db.delete_table(u'configuration_grupo_beneficiario')

        # Deleting model 'Papel'
        db.delete_table(u'configuration_papel')

        # Deleting model 'Categoria'
        db.delete_table(u'configuration_categoria')

        # Deleting model 'Categoria_Innovacion'
        db.delete_table(u'configuration_categoria_innovacion')

        # Deleting model 'Categoria_Conocimiento'
        db.delete_table(u'configuration_categoria_conocimiento')

        # Deleting model 'Categoria_Fuente'
        db.delete_table(u'configuration_categoria_fuente')

        # Deleting model 'Seleccion_7a'
        db.delete_table(u'configuration_seleccion_7a')

        # Deleting model 'Seleccion_7b'
        db.delete_table(u'configuration_seleccion_7b')

        # Deleting model 'Tipo_Estudio'
        db.delete_table(u'configuration_tipo_estudio')

        # Deleting model 'Tema_Relacion'
        db.delete_table(u'configuration_tema_relacion')


    models = {
        u'configuration.areaaccion': {
            'Meta': {'object_name': 'AreaAccion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'configuration.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.categoria_conocimiento': {
            'Meta': {'object_name': 'Categoria_Conocimiento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.categoria_fuente': {
            'Meta': {'object_name': 'Categoria_Fuente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.categoria_innovacion': {
            'Meta': {'object_name': 'Categoria_Innovacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.grupo': {
            'Meta': {'object_name': 'Grupo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.grupo_beneficiario': {
            'Meta': {'object_name': 'Grupo_Beneficiario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.papel': {
            'Meta': {'object_name': 'Papel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.plataforma': {
            'Meta': {'object_name': 'Plataforma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sitio_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuration.SitioAccion']"})
        },
        u'configuration.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'configuration.seleccion_7a': {
            'Meta': {'object_name': 'Seleccion_7a'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.seleccion_7b': {
            'Meta': {'object_name': 'Seleccion_7b'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.sitioaccion': {
            'Meta': {'object_name': 'SitioAccion'},
            'area_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuration.AreaAccion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'configuration.status_legal': {
            'Meta': {'object_name': 'Status_Legal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'configuration.tema': {
            'Meta': {'object_name': 'Tema'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'configuration.tema_relacion': {
            'Meta': {'object_name': 'Tema_Relacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.tipo_estudio': {
            'Meta': {'object_name': 'Tipo_Estudio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuration.ubicacion': {
            'Meta': {'object_name': 'Ubicacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['configuration']