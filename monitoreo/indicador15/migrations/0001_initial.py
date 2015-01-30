# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Piso'
        db.create_table(u'indicador15_piso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'indicador15', ['Piso'])

        # Adding model 'Techo'
        db.create_table(u'indicador15_techo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'indicador15', ['Techo'])

        # Adding model 'TipoCasa'
        db.create_table(u'indicador15_tipocasa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['TipoCasa'])

        # Adding M2M table for field piso on 'TipoCasa'
        m2m_table_name = db.shorten_name(u'indicador15_tipocasa_piso')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipocasa', models.ForeignKey(orm[u'indicador15.tipocasa'], null=False)),
            ('piso', models.ForeignKey(orm[u'indicador15.piso'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tipocasa_id', 'piso_id'])

        # Adding M2M table for field techo on 'TipoCasa'
        m2m_table_name = db.shorten_name(u'indicador15_tipocasa_techo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipocasa', models.ForeignKey(orm[u'indicador15.tipocasa'], null=False)),
            ('techo', models.ForeignKey(orm[u'indicador15.techo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tipocasa_id', 'techo_id'])

        # Adding model 'DetalleCasa'
        db.create_table(u'indicador15_detallecasa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tamano', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ambientes', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('letrina', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lavadero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['DetalleCasa'])

        # Adding model 'Equipos'
        db.create_table(u'indicador15_equipos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'indicador15', ['Equipos'])

        # Adding model 'Infraestructuras'
        db.create_table(u'indicador15_infraestructuras', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'indicador15', ['Infraestructuras'])

        # Adding model 'PropiedadEquipo'
        db.create_table(u'indicador15_propiedadequipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.Equipos'], null=True, blank=True)),
            ('cantidad_equipo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['PropiedadEquipo'])

        # Adding model 'PropiedadInfraestructura'
        db.create_table(u'indicador15_propiedadinfraestructura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('infraestructura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.Infraestructuras'], null=True, blank=True)),
            ('cantidad_infra', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['PropiedadInfraestructura'])

        # Adding model 'NombreHerramienta'
        db.create_table(u'indicador15_nombreherramienta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'indicador15', ['NombreHerramienta'])

        # Adding model 'Herramientas'
        db.create_table(u'indicador15_herramientas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('herramienta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.NombreHerramienta'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['Herramientas'])

        # Adding model 'NombreTransporte'
        db.create_table(u'indicador15_nombretransporte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'indicador15', ['NombreTransporte'])

        # Adding model 'Transporte'
        db.create_table(u'indicador15_transporte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transporte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.NombreTransporte'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['Transporte'])

        # Adding model 'PropiedadEquipoEntrevista'
        db.create_table(u'indicador15_propiedadequipoentrevista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.Equipos'], null=True, blank=True)),
            ('cantidad_equipo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['PropiedadEquipoEntrevista'])

        # Adding model 'PropiedadInfraestructuraEntrevista'
        db.create_table(u'indicador15_propiedadinfraestructuraentrevista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('infraestructura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.Infraestructuras'], null=True, blank=True)),
            ('cantidad_infra', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['PropiedadInfraestructuraEntrevista'])

        # Adding model 'HerramientasEntrevista'
        db.create_table(u'indicador15_herramientasentrevista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('herramienta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.NombreHerramienta'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['HerramientasEntrevista'])

        # Adding model 'TransporteEntrevista'
        db.create_table(u'indicador15_transporteentrevista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transporte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.NombreTransporte'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador15', ['TransporteEntrevista'])


    def backwards(self, orm):
        # Deleting model 'Piso'
        db.delete_table(u'indicador15_piso')

        # Deleting model 'Techo'
        db.delete_table(u'indicador15_techo')

        # Deleting model 'TipoCasa'
        db.delete_table(u'indicador15_tipocasa')

        # Removing M2M table for field piso on 'TipoCasa'
        db.delete_table(db.shorten_name(u'indicador15_tipocasa_piso'))

        # Removing M2M table for field techo on 'TipoCasa'
        db.delete_table(db.shorten_name(u'indicador15_tipocasa_techo'))

        # Deleting model 'DetalleCasa'
        db.delete_table(u'indicador15_detallecasa')

        # Deleting model 'Equipos'
        db.delete_table(u'indicador15_equipos')

        # Deleting model 'Infraestructuras'
        db.delete_table(u'indicador15_infraestructuras')

        # Deleting model 'PropiedadEquipo'
        db.delete_table(u'indicador15_propiedadequipo')

        # Deleting model 'PropiedadInfraestructura'
        db.delete_table(u'indicador15_propiedadinfraestructura')

        # Deleting model 'NombreHerramienta'
        db.delete_table(u'indicador15_nombreherramienta')

        # Deleting model 'Herramientas'
        db.delete_table(u'indicador15_herramientas')

        # Deleting model 'NombreTransporte'
        db.delete_table(u'indicador15_nombretransporte')

        # Deleting model 'Transporte'
        db.delete_table(u'indicador15_transporte')

        # Deleting model 'PropiedadEquipoEntrevista'
        db.delete_table(u'indicador15_propiedadequipoentrevista')

        # Deleting model 'PropiedadInfraestructuraEntrevista'
        db.delete_table(u'indicador15_propiedadinfraestructuraentrevista')

        # Deleting model 'HerramientasEntrevista'
        db.delete_table(u'indicador15_herramientasentrevista')

        # Deleting model 'TransporteEntrevista'
        db.delete_table(u'indicador15_transporteentrevista')


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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'configuracion.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'configuracion.sitioaccion': {
            'Meta': {'object_name': 'SitioAccion'},
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
        u'indicador15.detallecasa': {
            'Meta': {'object_name': 'DetalleCasa'},
            'ambientes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lavadero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'letrina': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tamano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'indicador15.equipos': {
            'Meta': {'object_name': 'Equipos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'indicador15.herramientas': {
            'Meta': {'object_name': 'Herramientas'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            'herramienta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['indicador15.NombreHerramienta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'indicador15.herramientasentrevista': {
            'Meta': {'object_name': 'HerramientasEntrevista'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            'herramienta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['indicador15.NombreHerramienta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'indicador15.infraestructuras': {
            'Meta': {'object_name': 'Infraestructuras'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'indicador15.nombreherramienta': {
            'Meta': {'object_name': 'NombreHerramienta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'indicador15.nombretransporte': {
            'Meta': {'object_name': 'NombreTransporte'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'indicador15.piso': {
            'Meta': {'object_name': 'Piso'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'indicador15.propiedadequipo': {
            'Meta': {'object_name': 'PropiedadEquipo'},
            'cantidad_equipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['indicador15.Equipos']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'indicador15.propiedadequipoentrevista': {
            'Meta': {'object_name': 'PropiedadEquipoEntrevista'},
            'cantidad_equipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['indicador15.Equipos']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'indicador15.propiedadinfraestructura': {
            'Meta': {'object_name': 'PropiedadInfraestructura'},
            'cantidad_infra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infraestructura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['indicador15.Infraestructuras']", 'null': 'True', 'blank': 'True'})
        },
        u'indicador15.propiedadinfraestructuraentrevista': {
            'Meta': {'object_name': 'PropiedadInfraestructuraEntrevista'},
            'cantidad_infra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infraestructura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['indicador15.Infraestructuras']", 'null': 'True', 'blank': 'True'})
        },
        u'indicador15.techo': {
            'Meta': {'object_name': 'Techo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'indicador15.tipocasa': {
            'Meta': {'object_name': 'TipoCasa'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piso': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador15.Piso']", 'symmetrical': 'False'}),
            'techo': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador15.Techo']", 'symmetrical': 'False'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'indicador15.transporte': {
            'Meta': {'object_name': 'Transporte'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transporte': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['indicador15.NombreTransporte']"})
        },
        u'indicador15.transporteentrevista': {
            'Meta': {'object_name': 'TransporteEntrevista'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transporte': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['indicador15.NombreTransporte']"})
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
            'siglas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
        u'monitoreo.recolector': {
            'Meta': {'object_name': 'Recolector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['indicador15']