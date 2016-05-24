# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Punto8y9Plagas.equipos'
        db.alter_column(u'guias_cacao_punto8y9plagas', 'equipos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=15))
        # Adding field 'Especies.tipo'
        db.add_column(u'guias_cacao_especies', 'tipo',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.foto'
        db.add_column(u'guias_cacao_especies', 'foto',
                      self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.p_altura'
        db.add_column(u'guias_cacao_especies', 'p_altura',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.p_diametro'
        db.add_column(u'guias_cacao_especies', 'p_diametro',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.p_ancho'
        db.add_column(u'guias_cacao_especies', 'p_ancho',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.m_altura'
        db.add_column(u'guias_cacao_especies', 'm_altura',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.m_diametro'
        db.add_column(u'guias_cacao_especies', 'm_diametro',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.m_ancho'
        db.add_column(u'guias_cacao_especies', 'm_ancho',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.g_altura'
        db.add_column(u'guias_cacao_especies', 'g_altura',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.g_diametro'
        db.add_column(u'guias_cacao_especies', 'g_diametro',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Especies.g_ancho'
        db.add_column(u'guias_cacao_especies', 'g_ancho',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'PisoPunto10.equipo'
        db.alter_column(u'guias_cacao_pisopunto10', 'equipo', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=15))

        # Changing field 'ProblemasPrincipales.principales'
        db.alter_column(u'guias_cacao_problemasprincipales', 'principales', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=27))

        # Changing field 'ProblemasPrincipales.observadas'
        db.alter_column(u'guias_cacao_problemasprincipales', 'observadas', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=27))

    def backwards(self, orm):

        # Changing field 'Punto8y9Plagas.equipos'
        db.alter_column(u'guias_cacao_punto8y9plagas', 'equipos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=13))
        # Deleting field 'Especies.tipo'
        db.delete_column(u'guias_cacao_especies', 'tipo')

        # Deleting field 'Especies.foto'
        db.delete_column(u'guias_cacao_especies', 'foto')

        # Deleting field 'Especies.p_altura'
        db.delete_column(u'guias_cacao_especies', 'p_altura')

        # Deleting field 'Especies.p_diametro'
        db.delete_column(u'guias_cacao_especies', 'p_diametro')

        # Deleting field 'Especies.p_ancho'
        db.delete_column(u'guias_cacao_especies', 'p_ancho')

        # Deleting field 'Especies.m_altura'
        db.delete_column(u'guias_cacao_especies', 'm_altura')

        # Deleting field 'Especies.m_diametro'
        db.delete_column(u'guias_cacao_especies', 'm_diametro')

        # Deleting field 'Especies.m_ancho'
        db.delete_column(u'guias_cacao_especies', 'm_ancho')

        # Deleting field 'Especies.g_altura'
        db.delete_column(u'guias_cacao_especies', 'g_altura')

        # Deleting field 'Especies.g_diametro'
        db.delete_column(u'guias_cacao_especies', 'g_diametro')

        # Deleting field 'Especies.g_ancho'
        db.delete_column(u'guias_cacao_especies', 'g_ancho')


        # Changing field 'PisoPunto10.equipo'
        db.alter_column(u'guias_cacao_pisopunto10', 'equipo', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=13))

        # Changing field 'ProblemasPrincipales.principales'
        db.alter_column(u'guias_cacao_problemasprincipales', 'principales', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=19))

        # Changing field 'ProblemasPrincipales.observadas'
        db.alter_column(u'guias_cacao_problemasprincipales', 'observadas', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=19))

    models = {
        u'guias_cacao.accionesenfermedad': {
            'Meta': {'object_name': 'AccionesEnfermedad'},
            'cuantas_veces': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'plagas_acciones': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'realiza_manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
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
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'g_altura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'g_ancho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'g_diametro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_altura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'm_ancho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'm_diametro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'p_altura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p_ancho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p_diametro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.fichapiso': {
            'Meta': {'object_name': 'FichaPiso'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_piso'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_piso'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichaplaga': {
            'Meta': {'object_name': 'FichaPlaga'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_plaga'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_plaga'", 'to': u"orm['mapeo.Persona']"})
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
        u'guias_cacao.observacionpunto1': {
            'Meta': {'object_name': 'ObservacionPunto1'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto1nivel': {
            'Meta': {'object_name': 'ObservacionPunto1Nivel'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto2': {
            'Meta': {'object_name': 'ObservacionPunto2'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto2nivel': {
            'Meta': {'object_name': 'ObservacionPunto2Nivel'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto3': {
            'Meta': {'object_name': 'ObservacionPunto3'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto3nivel': {
            'Meta': {'object_name': 'ObservacionPunto3Nivel'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.orientacion': {
            'Meta': {'object_name': 'Orientacion'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            'fuentes': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.pisopunto1': {
            'Meta': {'object_name': 'PisoPunto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'punto1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'punto2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'})
        },
        u'guias_cacao.pisopunto10': {
            'Meta': {'object_name': 'PisoPunto10'},
            'equipo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.pisopunto3': {
            'Meta': {'object_name': 'PisoPunto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'realiza': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'veces': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.pisopunto4': {
            'Meta': {'object_name': 'PisoPunto4'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.pisopunto5': {
            'Meta': {'object_name': 'PisoPunto5'},
            'conteo': ('django.db.models.fields.FloatField', [], {}),
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.pisopunto6': {
            'Meta': {'object_name': 'PisoPunto6'},
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maleza': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'})
        },
        u'guias_cacao.pisopunto7': {
            'Meta': {'object_name': 'PisoPunto7'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'sombra': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7'}),
            'suelo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.pisopunto8': {
            'Meta': {'object_name': 'PisoPunto8'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'parte': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'piso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.plagasenfermedad': {
            'Meta': {'object_name': 'PlagasEnfermedad'},
            'dano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plagas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.problemasprincipales': {
            'Meta': {'object_name': 'ProblemasPrincipales'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observadas': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '27'}),
            'principales': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '27'}),
            'situacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
        u'guias_cacao.punto6plagas': {
            'Meta': {'object_name': 'Punto6Plagas'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'observaciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'sombra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.punto7plagas': {
            'Meta': {'object_name': 'Punto7Plagas'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'parte': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.punto8y9plagas': {
            'Meta': {'object_name': 'Punto8y9Plagas'},
            'equipos': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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