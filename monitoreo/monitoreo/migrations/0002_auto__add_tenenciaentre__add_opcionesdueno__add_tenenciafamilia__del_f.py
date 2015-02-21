# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TenenciaEntre'
        db.create_table(u'monitoreo_tenenciaentre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'monitoreo', ['TenenciaEntre'])

        # Adding model 'OpcionesDueno'
        db.create_table(u'monitoreo_opcionesdueno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'monitoreo', ['OpcionesDueno'])

        # Adding model 'TenenciaFamilia'
        db.create_table(u'monitoreo_tenenciafamilia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'monitoreo', ['TenenciaFamilia'])

        # Deleting field 'TenenciaEntrevistada.dueno'
        db.delete_column(u'monitoreo_tenenciaentrevistada', 'dueno')

        # Deleting field 'TenenciaEntrevistada.parcela'
        db.delete_column(u'monitoreo_tenenciaentrevistada', 'parcela')

        # Deleting field 'TenenciaEntrevistada.solar'
        db.delete_column(u'monitoreo_tenenciaentrevistada', 'solar')

        # Adding M2M table for field parcela on 'TenenciaEntrevistada'
        m2m_table_name = db.shorten_name(u'monitoreo_tenenciaentrevistada_parcela')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tenenciaentrevistada', models.ForeignKey(orm[u'monitoreo.tenenciaentrevistada'], null=False)),
            ('tenenciafamilia', models.ForeignKey(orm[u'monitoreo.tenenciafamilia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tenenciaentrevistada_id', 'tenenciafamilia_id'])

        # Adding M2M table for field solar on 'TenenciaEntrevistada'
        m2m_table_name = db.shorten_name(u'monitoreo_tenenciaentrevistada_solar')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tenenciaentrevistada', models.ForeignKey(orm[u'monitoreo.tenenciaentrevistada'], null=False)),
            ('tenenciaentre', models.ForeignKey(orm[u'monitoreo.tenenciaentre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tenenciaentrevistada_id', 'tenenciaentre_id'])

        # Adding M2M table for field dueno on 'TenenciaEntrevistada'
        m2m_table_name = db.shorten_name(u'monitoreo_tenenciaentrevistada_dueno')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tenenciaentrevistada', models.ForeignKey(orm[u'monitoreo.tenenciaentrevistada'], null=False)),
            ('opcionesdueno', models.ForeignKey(orm[u'monitoreo.opcionesdueno'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tenenciaentrevistada_id', 'opcionesdueno_id'])

        # Deleting field 'Tenencia.dueno'
        db.delete_column(u'monitoreo_tenencia', 'dueno')

        # Deleting field 'Tenencia.parcela'
        db.delete_column(u'monitoreo_tenencia', 'parcela')

        # Deleting field 'Tenencia.solar'
        db.delete_column(u'monitoreo_tenencia', 'solar')

        # Adding M2M table for field parcela on 'Tenencia'
        m2m_table_name = db.shorten_name(u'monitoreo_tenencia_parcela')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tenencia', models.ForeignKey(orm[u'monitoreo.tenencia'], null=False)),
            ('tenenciafamilia', models.ForeignKey(orm[u'monitoreo.tenenciafamilia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tenencia_id', 'tenenciafamilia_id'])

        # Adding M2M table for field solar on 'Tenencia'
        m2m_table_name = db.shorten_name(u'monitoreo_tenencia_solar')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tenencia', models.ForeignKey(orm[u'monitoreo.tenencia'], null=False)),
            ('tenenciaentre', models.ForeignKey(orm[u'monitoreo.tenenciaentre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tenencia_id', 'tenenciaentre_id'])

        # Adding M2M table for field dueno on 'Tenencia'
        m2m_table_name = db.shorten_name(u'monitoreo_tenencia_dueno')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tenencia', models.ForeignKey(orm[u'monitoreo.tenencia'], null=False)),
            ('opcionesdueno', models.ForeignKey(orm[u'monitoreo.opcionesdueno'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tenencia_id', 'opcionesdueno_id'])


    def backwards(self, orm):
        # Deleting model 'TenenciaEntre'
        db.delete_table(u'monitoreo_tenenciaentre')

        # Deleting model 'OpcionesDueno'
        db.delete_table(u'monitoreo_opcionesdueno')

        # Deleting model 'TenenciaFamilia'
        db.delete_table(u'monitoreo_tenenciafamilia')

        # Adding field 'TenenciaEntrevistada.dueno'
        db.add_column(u'monitoreo_tenenciaentrevistada', 'dueno',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'TenenciaEntrevistada.parcela'
        db.add_column(u'monitoreo_tenenciaentrevistada', 'parcela',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'TenenciaEntrevistada.solar'
        db.add_column(u'monitoreo_tenenciaentrevistada', 'solar',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Removing M2M table for field parcela on 'TenenciaEntrevistada'
        db.delete_table(db.shorten_name(u'monitoreo_tenenciaentrevistada_parcela'))

        # Removing M2M table for field solar on 'TenenciaEntrevistada'
        db.delete_table(db.shorten_name(u'monitoreo_tenenciaentrevistada_solar'))

        # Removing M2M table for field dueno on 'TenenciaEntrevistada'
        db.delete_table(db.shorten_name(u'monitoreo_tenenciaentrevistada_dueno'))

        # Adding field 'Tenencia.dueno'
        db.add_column(u'monitoreo_tenencia', 'dueno',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Tenencia.parcela'
        db.add_column(u'monitoreo_tenencia', 'parcela',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Tenencia.solar'
        db.add_column(u'monitoreo_tenencia', 'solar',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Removing M2M table for field parcela on 'Tenencia'
        db.delete_table(db.shorten_name(u'monitoreo_tenencia_parcela'))

        # Removing M2M table for field solar on 'Tenencia'
        db.delete_table(db.shorten_name(u'monitoreo_tenencia_solar'))

        # Removing M2M table for field dueno on 'Tenencia'
        db.delete_table(db.shorten_name(u'monitoreo_tenencia_dueno'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'lugar.comunidad': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Comunidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'lugar.departamento': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
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
        u'mapeo.organizaciones': {
            'Meta': {'ordering': "[u'nombre']", 'unique_together': "((u'font_color', u'nombre'),)", 'object_name': 'Organizaciones'},
            'area_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.AreaAccion']"}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'departamento': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'font_color': ('mapeo.models.ColorField', [], {'unique': 'True', 'max_length': '10', 'blank': 'True'}),
            'fundacion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'generalidades': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'plataforma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Plataforma']"}),
            'rss': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Sector']"}),
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
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nivel_educacion': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'org'", 'symmetrical': 'False', 'to': u"orm['mapeo.Organizaciones']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'monitoreo.casasolar': {
            'Meta': {'object_name': 'CasaSolar'},
            'casa': ('django.db.models.fields.IntegerField', [], {}),
            'dueno': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tenencia': ('django.db.models.fields.IntegerField', [], {})
        },
        u'monitoreo.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jefe': ('django.db.models.fields.IntegerField', [], {}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Persona']"}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Recolector']"}),
            'tipo_encuesta': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'monitoreo.opcionesdueno': {
            'Meta': {'object_name': 'OpcionesDueno'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'monitoreo.recolector': {
            'Meta': {'object_name': 'Recolector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'monitoreo.tenencia': {
            'Meta': {'object_name': 'Tenencia'},
            'dueno': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['monitoreo.OpcionesDueno']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parcela': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['monitoreo.TenenciaFamilia']", 'symmetrical': 'False'}),
            'solar': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['monitoreo.TenenciaEntre']", 'symmetrical': 'False'})
        },
        u'monitoreo.tenenciaentre': {
            'Meta': {'object_name': 'TenenciaEntre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'monitoreo.tenenciaentrevistada': {
            'Meta': {'object_name': 'TenenciaEntrevistada'},
            'dueno': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['monitoreo.OpcionesDueno']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parcela': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['monitoreo.TenenciaFamilia']", 'symmetrical': 'False'}),
            'solar': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['monitoreo.TenenciaEntre']", 'symmetrical': 'False'})
        },
        u'monitoreo.tenenciafamilia': {
            'Meta': {'object_name': 'TenenciaFamilia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['monitoreo']