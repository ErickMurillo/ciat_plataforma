# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Textura'
        db.create_table(u'indicador12_textura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador12', ['Textura'])

        # Adding model 'Profundidad'
        db.create_table(u'indicador12_profundidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador12', ['Profundidad'])

        # Adding model 'Densidad'
        db.create_table(u'indicador12_densidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador12', ['Densidad'])

        # Adding model 'Pendiente'
        db.create_table(u'indicador12_pendiente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador12', ['Pendiente'])

        # Adding model 'Drenaje'
        db.create_table(u'indicador12_drenaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador12', ['Drenaje'])

        # Adding model 'Suelo'
        db.create_table(u'indicador12_suelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador12', ['Suelo'])

        # Adding M2M table for field textura on 'Suelo'
        m2m_table_name = db.shorten_name(u'indicador12_suelo_textura')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm[u'indicador12.suelo'], null=False)),
            ('textura', models.ForeignKey(orm[u'indicador12.textura'], null=False))
        ))
        db.create_unique(m2m_table_name, ['suelo_id', 'textura_id'])

        # Adding M2M table for field profundidad on 'Suelo'
        m2m_table_name = db.shorten_name(u'indicador12_suelo_profundidad')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm[u'indicador12.suelo'], null=False)),
            ('profundidad', models.ForeignKey(orm[u'indicador12.profundidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['suelo_id', 'profundidad_id'])

        # Adding M2M table for field lombrices on 'Suelo'
        m2m_table_name = db.shorten_name(u'indicador12_suelo_lombrices')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm[u'indicador12.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm[u'indicador12.densidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['suelo_id', 'densidad_id'])

        # Adding M2M table for field densidad on 'Suelo'
        m2m_table_name = db.shorten_name(u'indicador12_suelo_densidad')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm[u'indicador12.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm[u'indicador12.densidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['suelo_id', 'densidad_id'])

        # Adding M2M table for field pendiente on 'Suelo'
        m2m_table_name = db.shorten_name(u'indicador12_suelo_pendiente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm[u'indicador12.suelo'], null=False)),
            ('pendiente', models.ForeignKey(orm[u'indicador12.pendiente'], null=False))
        ))
        db.create_unique(m2m_table_name, ['suelo_id', 'pendiente_id'])

        # Adding M2M table for field drenaje on 'Suelo'
        m2m_table_name = db.shorten_name(u'indicador12_suelo_drenaje')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm[u'indicador12.suelo'], null=False)),
            ('drenaje', models.ForeignKey(orm[u'indicador12.drenaje'], null=False))
        ))
        db.create_unique(m2m_table_name, ['suelo_id', 'drenaje_id'])

        # Adding M2M table for field materia on 'Suelo'
        m2m_table_name = db.shorten_name(u'indicador12_suelo_materia')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm[u'indicador12.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm[u'indicador12.densidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['suelo_id', 'densidad_id'])

        # Adding model 'Preparar'
        db.create_table(u'indicador12_preparar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador12', ['Preparar'])

        # Adding model 'Traccion'
        db.create_table(u'indicador12_traccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador12', ['Traccion'])

        # Adding model 'Fertilizacion'
        db.create_table(u'indicador12_fertilizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador12', ['Fertilizacion'])

        # Adding model 'Conservacion'
        db.create_table(u'indicador12_conservacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador12', ['Conservacion'])

        # Adding model 'ManejoSuelo'
        db.create_table(u'indicador12_manejosuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analisis', self.gf('django.db.models.fields.IntegerField')()),
            ('practica', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador12', ['ManejoSuelo'])

        # Adding M2M table for field preparan on 'ManejoSuelo'
        m2m_table_name = db.shorten_name(u'indicador12_manejosuelo_preparan')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm[u'indicador12.manejosuelo'], null=False)),
            ('preparar', models.ForeignKey(orm[u'indicador12.preparar'], null=False))
        ))
        db.create_unique(m2m_table_name, ['manejosuelo_id', 'preparar_id'])

        # Adding M2M table for field traccion on 'ManejoSuelo'
        m2m_table_name = db.shorten_name(u'indicador12_manejosuelo_traccion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm[u'indicador12.manejosuelo'], null=False)),
            ('traccion', models.ForeignKey(orm[u'indicador12.traccion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['manejosuelo_id', 'traccion_id'])

        # Adding M2M table for field fertilizacion on 'ManejoSuelo'
        m2m_table_name = db.shorten_name(u'indicador12_manejosuelo_fertilizacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm[u'indicador12.manejosuelo'], null=False)),
            ('fertilizacion', models.ForeignKey(orm[u'indicador12.fertilizacion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['manejosuelo_id', 'fertilizacion_id'])

        # Adding M2M table for field obra on 'ManejoSuelo'
        m2m_table_name = db.shorten_name(u'indicador12_manejosuelo_obra')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm[u'indicador12.manejosuelo'], null=False)),
            ('conservacion', models.ForeignKey(orm[u'indicador12.conservacion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['manejosuelo_id', 'conservacion_id'])


    def backwards(self, orm):
        # Deleting model 'Textura'
        db.delete_table(u'indicador12_textura')

        # Deleting model 'Profundidad'
        db.delete_table(u'indicador12_profundidad')

        # Deleting model 'Densidad'
        db.delete_table(u'indicador12_densidad')

        # Deleting model 'Pendiente'
        db.delete_table(u'indicador12_pendiente')

        # Deleting model 'Drenaje'
        db.delete_table(u'indicador12_drenaje')

        # Deleting model 'Suelo'
        db.delete_table(u'indicador12_suelo')

        # Removing M2M table for field textura on 'Suelo'
        db.delete_table(db.shorten_name(u'indicador12_suelo_textura'))

        # Removing M2M table for field profundidad on 'Suelo'
        db.delete_table(db.shorten_name(u'indicador12_suelo_profundidad'))

        # Removing M2M table for field lombrices on 'Suelo'
        db.delete_table(db.shorten_name(u'indicador12_suelo_lombrices'))

        # Removing M2M table for field densidad on 'Suelo'
        db.delete_table(db.shorten_name(u'indicador12_suelo_densidad'))

        # Removing M2M table for field pendiente on 'Suelo'
        db.delete_table(db.shorten_name(u'indicador12_suelo_pendiente'))

        # Removing M2M table for field drenaje on 'Suelo'
        db.delete_table(db.shorten_name(u'indicador12_suelo_drenaje'))

        # Removing M2M table for field materia on 'Suelo'
        db.delete_table(db.shorten_name(u'indicador12_suelo_materia'))

        # Deleting model 'Preparar'
        db.delete_table(u'indicador12_preparar')

        # Deleting model 'Traccion'
        db.delete_table(u'indicador12_traccion')

        # Deleting model 'Fertilizacion'
        db.delete_table(u'indicador12_fertilizacion')

        # Deleting model 'Conservacion'
        db.delete_table(u'indicador12_conservacion')

        # Deleting model 'ManejoSuelo'
        db.delete_table(u'indicador12_manejosuelo')

        # Removing M2M table for field preparan on 'ManejoSuelo'
        db.delete_table(db.shorten_name(u'indicador12_manejosuelo_preparan'))

        # Removing M2M table for field traccion on 'ManejoSuelo'
        db.delete_table(db.shorten_name(u'indicador12_manejosuelo_traccion'))

        # Removing M2M table for field fertilizacion on 'ManejoSuelo'
        db.delete_table(db.shorten_name(u'indicador12_manejosuelo_fertilizacion'))

        # Removing M2M table for field obra on 'ManejoSuelo'
        db.delete_table(db.shorten_name(u'indicador12_manejosuelo_obra'))


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
        u'indicador12.conservacion': {
            'Meta': {'object_name': 'Conservacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador12.densidad': {
            'Meta': {'object_name': 'Densidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador12.drenaje': {
            'Meta': {'object_name': 'Drenaje'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador12.fertilizacion': {
            'Meta': {'object_name': 'Fertilizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador12.manejosuelo': {
            'Meta': {'object_name': 'ManejoSuelo'},
            'analisis': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            'fertilizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador12.Fertilizacion']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obra': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador12.Conservacion']", 'symmetrical': 'False'}),
            'practica': ('django.db.models.fields.IntegerField', [], {}),
            'preparan': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador12.Preparar']", 'symmetrical': 'False'}),
            'traccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador12.Traccion']", 'symmetrical': 'False'})
        },
        u'indicador12.pendiente': {
            'Meta': {'object_name': 'Pendiente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador12.preparar': {
            'Meta': {'object_name': 'Preparar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador12.profundidad': {
            'Meta': {'object_name': 'Profundidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador12.suelo': {
            'Meta': {'object_name': 'Suelo'},
            'densidad': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'densidad'", 'symmetrical': 'False', 'to': u"orm['indicador12.Densidad']"}),
            'drenaje': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador12.Drenaje']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lombrices': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lombrices'", 'symmetrical': 'False', 'to': u"orm['indicador12.Densidad']"}),
            'materia': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'materia'", 'symmetrical': 'False', 'to': u"orm['indicador12.Densidad']"}),
            'pendiente': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador12.Pendiente']", 'symmetrical': 'False'}),
            'profundidad': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador12.Profundidad']", 'symmetrical': 'False'}),
            'textura': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador12.Textura']", 'symmetrical': 'False'})
        },
        u'indicador12.textura': {
            'Meta': {'object_name': 'Textura'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador12.traccion': {
            'Meta': {'object_name': 'Traccion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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

    complete_apps = ['indicador12']