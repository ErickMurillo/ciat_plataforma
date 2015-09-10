# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Productor.fecha1'
        db.add_column(u'mapeo_productor', 'fecha1',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Productor.fecha1'
        db.delete_column(u'mapeo_productor', 'fecha1')


    models = {
        u'configuracion.areaaccion': {
            'Meta': {'object_name': 'AreaAccion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'configuracion.plataforma': {
            'Meta': {'object_name': 'Plataforma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sitio_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.SitioAccion']"})
        },
        u'configuracion.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'configuracion.sitioaccion': {
            'Meta': {'object_name': 'SitioAccion'},
            'area_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.AreaAccion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'configuration.sector_en': {
            'Meta': {'object_name': 'Sector_en'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        u'mapeo.accionar': {
            'Meta': {'object_name': 'Accionar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mapeo.campoaccion': {
            'Meta': {'object_name': 'CampoAccion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mapeo.decisor': {
            'Meta': {'object_name': 'Decisor'},
            'campo': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.CampoAccion']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Accionar']", 'symmetrical': 'False'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Persona']"}),
            'pertenece': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Organizaciones']", 'symmetrical': 'False'}),
            'proyecto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Proyectos']", 'symmetrical': 'False'})
        },
        u'mapeo.especialidades': {
            'Meta': {'object_name': 'Especialidades'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mapeo.formaatencion': {
            'Meta': {'object_name': 'FormaAtencion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mapeo.fuentemanoobra': {
            'Meta': {'object_name': 'FuenteManoObra'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mapeo.lideres': {
            'Meta': {'object_name': 'Lideres'},
            'atiende': ('django.db.models.fields.IntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'forma_atiende': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.FormaAtencion']", 'symmetrical': 'False'}),
            'fuente': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.FuenteManoObra']", 'symmetrical': 'False'}),
            'ganado': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jefe': ('django.db.models.fields.IntegerField', [], {}),
            'organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'org'", 'symmetrical': 'False', 'to': u"orm['mapeo.Organizaciones']"}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Persona']"}),
            'proyecto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Proyectos']", 'symmetrical': 'False'}),
            'rubro_principal_agro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'principal'", 'to': u"orm['mapeo.RubrosAgropecuarios']"}),
            'rubro_principal_no_agro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'principalno'", 'to': u"orm['mapeo.RubrosNoAgropecuarios']"}),
            'rubros_agro': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'agro'", 'symmetrical': 'False', 'to': u"orm['mapeo.RubrosAgropecuarios']"}),
            'rubros_no_agro': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'noagro'", 'symmetrical': 'False', 'to': u"orm['mapeo.RubrosNoAgropecuarios']"}),
            'tamano': ('django.db.models.fields.FloatField', [], {}),
            'tipologia': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mapeo.organizaciones': {
            'Meta': {'ordering': "[u'nombre']", 'unique_together': "((u'font_color', u'nombre'),)", 'object_name': 'Organizaciones'},
            'area_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.AreaAccion']"}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'departamento': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Departamento']", 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'font_color': ('mapeo.models.ColorField', [], {'unique': 'True', 'max_length': '10', 'blank': 'True'}),
            'fundacion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'generalidades': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'plataforma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Plataforma']"}),
            'rss': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Sector']"}),
            'sector_en': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuration.Sector_en']", 'null': 'True', 'blank': 'True'}),
            'siglas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sitio_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.SitioAccion']"}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'temas': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'})
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
        },
        u'mapeo.productor': {
            'Meta': {'object_name': 'Productor'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fecha1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.FuenteManoObra']", 'symmetrical': 'False'}),
            'ganado': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jefe': ('django.db.models.fields.IntegerField', [], {}),
            'organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'organizacion'", 'symmetrical': 'False', 'to': u"orm['mapeo.Organizaciones']"}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Persona']"}),
            'proyecto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Proyectos']", 'symmetrical': 'False'}),
            'rubro_principal_agro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'dos'", 'to': u"orm['mapeo.RubrosAgropecuarios']"}),
            'rubro_principal_no_agro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cuatro'", 'to': u"orm['mapeo.RubrosNoAgropecuarios']"}),
            'rubros_agro': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'uno'", 'symmetrical': 'False', 'to': u"orm['mapeo.RubrosAgropecuarios']"}),
            'rubros_no_agro': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'tres'", 'symmetrical': 'False', 'to': u"orm['mapeo.RubrosNoAgropecuarios']"}),
            'tamano': ('django.db.models.fields.FloatField', [], {}),
            'tipologia': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mapeo.proyectos': {
            'Meta': {'object_name': 'Proyectos'},
            'alianza': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Plataforma']", 'symmetrical': 'False'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'corto': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'ejecutora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Organizaciones']"}),
            'finalizacion': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'influencia': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lugar.Municipio']", 'symmetrical': 'False'}),
            'informacion': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'socias': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'socias'", 'symmetrical': 'False', 'to': u"orm['mapeo.Organizaciones']"})
        },
        u'mapeo.rubrosagropecuarios': {
            'Meta': {'object_name': 'RubrosAgropecuarios'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mapeo.rubrosnoagropecuarios': {
            'Meta': {'object_name': 'RubrosNoAgropecuarios'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mapeo.tecnicoespinvestigador': {
            'Meta': {'object_name': 'TecnicoEspInvestigador'},
            'especialidad': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Especialidades']", 'symmetrical': 'False'}),
            'experiencia': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'formacion': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Persona']"}),
            'pertenece': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Organizaciones']", 'symmetrical': 'False'}),
            'proyecto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Proyectos']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['mapeo']