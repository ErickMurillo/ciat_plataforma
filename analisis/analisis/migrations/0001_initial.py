# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entrevista'
        db.create_table(u'analisis_entrevista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('posicion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Organizaciones'])),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'])),
            ('telefono', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('alcance', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tipo_estudio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Tipo_Estudio'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'analisis', ['Entrevista'])

        # Adding model 'Pregunta_1'
        db.create_table(u'analisis_pregunta_1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_1'])

        # Adding M2M table for field ubicacion on 'Pregunta_1'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_1_ubicacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_1', models.ForeignKey(orm[u'analisis.pregunta_1'], null=False)),
            ('ubicacion', models.ForeignKey(orm[u'configuracion.ubicacion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_1_id', 'ubicacion_id'])

        # Adding M2M table for field socio on 'Pregunta_1'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_1_socio')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_1', models.ForeignKey(orm[u'analisis.pregunta_1'], null=False)),
            ('socio', models.ForeignKey(orm[u'configuracion.socio'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_1_id', 'socio_id'])

        # Adding M2M table for field tema on 'Pregunta_1'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_1_tema')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_1', models.ForeignKey(orm[u'analisis.pregunta_1'], null=False)),
            ('tema', models.ForeignKey(orm[u'configuracion.tema'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_1_id', 'tema_id'])

        # Adding model 'Pregunta_2'
        db.create_table(u'analisis_pregunta_2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seleccion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_2'])

        # Adding model 'Pregunta_3'
        db.create_table(u'analisis_pregunta_3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_3'])

        # Adding M2M table for field grupo on 'Pregunta_3'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_3_grupo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_3', models.ForeignKey(orm[u'analisis.pregunta_3'], null=False)),
            ('grupo', models.ForeignKey(orm[u'configuracion.grupo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_3_id', 'grupo_id'])

        # Adding model 'Pregunta_4'
        db.create_table(u'analisis_pregunta_4', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('impacto', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_4'])

        # Adding M2M table for field grupo_beneficiario on 'Pregunta_4'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_4_grupo_beneficiario')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_4', models.ForeignKey(orm[u'analisis.pregunta_4'], null=False)),
            ('grupo', models.ForeignKey(orm[u'configuracion.grupo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_4_id', 'grupo_id'])

        # Adding M2M table for field tema on 'Pregunta_4'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_4_tema')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_4', models.ForeignKey(orm[u'analisis.pregunta_4'], null=False)),
            ('tema', models.ForeignKey(orm[u'configuracion.tema'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_4_id', 'tema_id'])

        # Adding model 'Pregunta_5a'
        db.create_table(u'analisis_pregunta_5a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovacion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('prioritizado', self.gf('django.db.models.fields.IntegerField')()),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_5a'])

        # Adding M2M table for field ubicacion on 'Pregunta_5a'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_5a_ubicacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_5a', models.ForeignKey(orm[u'analisis.pregunta_5a'], null=False)),
            ('ubicacion', models.ForeignKey(orm[u'configuracion.ubicacion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_5a_id', 'ubicacion_id'])

        # Adding M2M table for field socio on 'Pregunta_5a'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_5a_socio')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_5a', models.ForeignKey(orm[u'analisis.pregunta_5a'], null=False)),
            ('socio', models.ForeignKey(orm[u'configuracion.socio'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_5a_id', 'socio_id'])

        # Adding M2M table for field tema on 'Pregunta_5a'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_5a_tema')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_5a', models.ForeignKey(orm[u'analisis.pregunta_5a'], null=False)),
            ('tema', models.ForeignKey(orm[u'configuracion.tema'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_5a_id', 'tema_id'])

        # Adding model 'Pregunta_5c'
        db.create_table(u'analisis_pregunta_5c', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Pregunta_5a'])),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Organizaciones'])),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_5c'])

        # Adding M2M table for field papel_1 on 'Pregunta_5c'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_5c_papel_1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_5c', models.ForeignKey(orm[u'analisis.pregunta_5c'], null=False)),
            ('papel', models.ForeignKey(orm[u'configuracion.papel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_5c_id', 'papel_id'])

        # Adding model 'Pregunta_5d'
        db.create_table(u'analisis_pregunta_5d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Pregunta_5a'])),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_5d'])

        # Adding M2M table for field categoria on 'Pregunta_5d'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_5d_categoria')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_5d', models.ForeignKey(orm[u'analisis.pregunta_5d'], null=False)),
            ('categoria', models.ForeignKey(orm[u'configuracion.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_5d_id', 'categoria_id'])

        # Adding model 'Pregunta_5e'
        db.create_table(u'analisis_pregunta_5e', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Pregunta_5a'])),
            ('fuente', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_5e'])

        # Adding M2M table for field categoria_fuente on 'Pregunta_5e'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_5e_categoria_fuente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_5e', models.ForeignKey(orm[u'analisis.pregunta_5e'], null=False)),
            ('categoria_fuente', models.ForeignKey(orm[u'configuracion.categoria_fuente'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_5e_id', 'categoria_fuente_id'])

        # Adding model 'Pregunta_6a'
        db.create_table(u'analisis_pregunta_6a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('prioritizado', self.gf('django.db.models.fields.IntegerField')()),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_6a'])

        # Adding M2M table for field ubicacion on 'Pregunta_6a'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_6a_ubicacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_6a', models.ForeignKey(orm[u'analisis.pregunta_6a'], null=False)),
            ('ubicacion', models.ForeignKey(orm[u'configuracion.ubicacion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_6a_id', 'ubicacion_id'])

        # Adding M2M table for field tema on 'Pregunta_6a'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_6a_tema')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_6a', models.ForeignKey(orm[u'analisis.pregunta_6a'], null=False)),
            ('tema', models.ForeignKey(orm[u'configuracion.tema'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_6a_id', 'tema_id'])

        # Adding model 'Pregunta_6c'
        db.create_table(u'analisis_pregunta_6c', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Pregunta_6a'])),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Organizaciones'])),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_6c'])

        # Adding M2M table for field papel on 'Pregunta_6c'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_6c_papel')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_6c', models.ForeignKey(orm[u'analisis.pregunta_6c'], null=False)),
            ('papel', models.ForeignKey(orm[u'configuracion.papel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_6c_id', 'papel_id'])

        # Adding model 'Pregunta_6d'
        db.create_table(u'analisis_pregunta_6d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Pregunta_6a'])),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_6d'])

        # Adding M2M table for field categoria on 'Pregunta_6d'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_6d_categoria')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_6d', models.ForeignKey(orm[u'analisis.pregunta_6d'], null=False)),
            ('categoria', models.ForeignKey(orm[u'configuracion.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_6d_id', 'categoria_id'])

        # Adding model 'Pregunta_6e'
        db.create_table(u'analisis_pregunta_6e', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Pregunta_6a'])),
            ('conocimient', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('categoria_innovacio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Categoria_Innovacion'])),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_6e'])

        # Adding M2M table for field categoria_conocimient on 'Pregunta_6e'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_6e_categoria_conocimient')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_6e', models.ForeignKey(orm[u'analisis.pregunta_6e'], null=False)),
            ('categoria_conocimiento', models.ForeignKey(orm[u'configuracion.categoria_conocimiento'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_6e_id', 'categoria_conocimiento_id'])

        # Adding model 'Pregunta_7a'
        db.create_table(u'analisis_pregunta_7a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_7a'])

        # Adding M2M table for field ubicacion on 'Pregunta_7a'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_7a_ubicacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_7a', models.ForeignKey(orm[u'analisis.pregunta_7a'], null=False)),
            ('ubicacion', models.ForeignKey(orm[u'configuracion.ubicacion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_7a_id', 'ubicacion_id'])

        # Adding M2M table for field seleccion on 'Pregunta_7a'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_7a_seleccion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_7a', models.ForeignKey(orm[u'analisis.pregunta_7a'], null=False)),
            ('seleccion_7a', models.ForeignKey(orm[u'configuracion.seleccion_7a'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_7a_id', 'seleccion_7a_id'])

        # Adding model 'Pregunta_7b'
        db.create_table(u'analisis_pregunta_7b', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_7b'])

        # Adding M2M table for field seleccion on 'Pregunta_7b'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_7b_seleccion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_7b', models.ForeignKey(orm[u'analisis.pregunta_7b'], null=False)),
            ('seleccion_7b', models.ForeignKey(orm[u'configuracion.seleccion_7b'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_7b_id', 'seleccion_7b_id'])

        # Adding model 'Pregunta_8'
        db.create_table(u'analisis_pregunta_8', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Organizaciones'])),
            ('territorio', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('periodo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('profundidad', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_8'])

        # Adding M2M table for field tema on 'Pregunta_8'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_8_tema')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_8', models.ForeignKey(orm[u'analisis.pregunta_8'], null=False)),
            ('tema_relacion', models.ForeignKey(orm[u'configuracion.tema_relacion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_8_id', 'tema_relacion_id'])

        # Adding model 'Pregunta_9'
        db.create_table(u'analisis_pregunta_9', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tema', self.gf('django.db.models.fields.IntegerField')()),
            ('prioridad', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('papel', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('conocimiento', self.gf('django.db.models.fields.IntegerField')()),
            ('experiencia', self.gf('django.db.models.fields.IntegerField')()),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_9'])

        # Adding model 'Pregunta_11'
        db.create_table(u'analisis_pregunta_11', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sobre', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_estudio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configuracion.Tipo_Estudio'])),
            ('calendario', self.gf('django.db.models.fields.IntegerField')()),
            ('disponibilidad', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('entrevistado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Entrevista'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_11'])


    def backwards(self, orm):
        # Deleting model 'Entrevista'
        db.delete_table(u'analisis_entrevista')

        # Deleting model 'Pregunta_1'
        db.delete_table(u'analisis_pregunta_1')

        # Removing M2M table for field ubicacion on 'Pregunta_1'
        db.delete_table(db.shorten_name(u'analisis_pregunta_1_ubicacion'))

        # Removing M2M table for field socio on 'Pregunta_1'
        db.delete_table(db.shorten_name(u'analisis_pregunta_1_socio'))

        # Removing M2M table for field tema on 'Pregunta_1'
        db.delete_table(db.shorten_name(u'analisis_pregunta_1_tema'))

        # Deleting model 'Pregunta_2'
        db.delete_table(u'analisis_pregunta_2')

        # Deleting model 'Pregunta_3'
        db.delete_table(u'analisis_pregunta_3')

        # Removing M2M table for field grupo on 'Pregunta_3'
        db.delete_table(db.shorten_name(u'analisis_pregunta_3_grupo'))

        # Deleting model 'Pregunta_4'
        db.delete_table(u'analisis_pregunta_4')

        # Removing M2M table for field grupo_beneficiario on 'Pregunta_4'
        db.delete_table(db.shorten_name(u'analisis_pregunta_4_grupo_beneficiario'))

        # Removing M2M table for field tema on 'Pregunta_4'
        db.delete_table(db.shorten_name(u'analisis_pregunta_4_tema'))

        # Deleting model 'Pregunta_5a'
        db.delete_table(u'analisis_pregunta_5a')

        # Removing M2M table for field ubicacion on 'Pregunta_5a'
        db.delete_table(db.shorten_name(u'analisis_pregunta_5a_ubicacion'))

        # Removing M2M table for field socio on 'Pregunta_5a'
        db.delete_table(db.shorten_name(u'analisis_pregunta_5a_socio'))

        # Removing M2M table for field tema on 'Pregunta_5a'
        db.delete_table(db.shorten_name(u'analisis_pregunta_5a_tema'))

        # Deleting model 'Pregunta_5c'
        db.delete_table(u'analisis_pregunta_5c')

        # Removing M2M table for field papel_1 on 'Pregunta_5c'
        db.delete_table(db.shorten_name(u'analisis_pregunta_5c_papel_1'))

        # Deleting model 'Pregunta_5d'
        db.delete_table(u'analisis_pregunta_5d')

        # Removing M2M table for field categoria on 'Pregunta_5d'
        db.delete_table(db.shorten_name(u'analisis_pregunta_5d_categoria'))

        # Deleting model 'Pregunta_5e'
        db.delete_table(u'analisis_pregunta_5e')

        # Removing M2M table for field categoria_fuente on 'Pregunta_5e'
        db.delete_table(db.shorten_name(u'analisis_pregunta_5e_categoria_fuente'))

        # Deleting model 'Pregunta_6a'
        db.delete_table(u'analisis_pregunta_6a')

        # Removing M2M table for field ubicacion on 'Pregunta_6a'
        db.delete_table(db.shorten_name(u'analisis_pregunta_6a_ubicacion'))

        # Removing M2M table for field tema on 'Pregunta_6a'
        db.delete_table(db.shorten_name(u'analisis_pregunta_6a_tema'))

        # Deleting model 'Pregunta_6c'
        db.delete_table(u'analisis_pregunta_6c')

        # Removing M2M table for field papel on 'Pregunta_6c'
        db.delete_table(db.shorten_name(u'analisis_pregunta_6c_papel'))

        # Deleting model 'Pregunta_6d'
        db.delete_table(u'analisis_pregunta_6d')

        # Removing M2M table for field categoria on 'Pregunta_6d'
        db.delete_table(db.shorten_name(u'analisis_pregunta_6d_categoria'))

        # Deleting model 'Pregunta_6e'
        db.delete_table(u'analisis_pregunta_6e')

        # Removing M2M table for field categoria_conocimient on 'Pregunta_6e'
        db.delete_table(db.shorten_name(u'analisis_pregunta_6e_categoria_conocimient'))

        # Deleting model 'Pregunta_7a'
        db.delete_table(u'analisis_pregunta_7a')

        # Removing M2M table for field ubicacion on 'Pregunta_7a'
        db.delete_table(db.shorten_name(u'analisis_pregunta_7a_ubicacion'))

        # Removing M2M table for field seleccion on 'Pregunta_7a'
        db.delete_table(db.shorten_name(u'analisis_pregunta_7a_seleccion'))

        # Deleting model 'Pregunta_7b'
        db.delete_table(u'analisis_pregunta_7b')

        # Removing M2M table for field seleccion on 'Pregunta_7b'
        db.delete_table(db.shorten_name(u'analisis_pregunta_7b_seleccion'))

        # Deleting model 'Pregunta_8'
        db.delete_table(u'analisis_pregunta_8')

        # Removing M2M table for field tema on 'Pregunta_8'
        db.delete_table(db.shorten_name(u'analisis_pregunta_8_tema'))

        # Deleting model 'Pregunta_9'
        db.delete_table(u'analisis_pregunta_9')

        # Deleting model 'Pregunta_11'
        db.delete_table(u'analisis_pregunta_11')


    models = {
        u'analisis.entrevista': {
            'Meta': {'object_name': 'Entrevista'},
            'alcance': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Organizaciones']"}),
            'posicion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_estudio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Tipo_Estudio']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'analisis.pregunta_1': {
            'Meta': {'object_name': 'Pregunta_1'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Socio']", 'symmetrical': 'False'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema']", 'symmetrical': 'False'}),
            'ubicacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Ubicacion']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_11': {
            'Meta': {'object_name': 'Pregunta_11'},
            'calendario': ('django.db.models.fields.IntegerField', [], {}),
            'disponibilidad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sobre': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_estudio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Tipo_Estudio']"})
        },
        u'analisis.pregunta_2': {
            'Meta': {'object_name': 'Pregunta_2'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'hombre': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujer': ('django.db.models.fields.IntegerField', [], {}),
            'seleccion': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'analisis.pregunta_3': {
            'Meta': {'object_name': 'Pregunta_3'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'grupo': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Grupo']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'analisis.pregunta_4': {
            'Meta': {'object_name': 'Pregunta_4'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'grupo_beneficiario': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Grupo']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impacto': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_5a': {
            'Meta': {'object_name': 'Pregunta_5a'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'prioritizado': ('django.db.models.fields.IntegerField', [], {}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Socio']", 'symmetrical': 'False'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema']", 'symmetrical': 'False'}),
            'ubicacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Ubicacion']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_5c': {
            'Meta': {'object_name': 'Pregunta_5c'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_5a']"}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Organizaciones']"}),
            'papel_1': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Papel']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_5d': {
            'Meta': {'object_name': 'Pregunta_5d'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Categoria']", 'symmetrical': 'False'}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_5a']"})
        },
        u'analisis.pregunta_5e': {
            'Meta': {'object_name': 'Pregunta_5e'},
            'categoria_fuente': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Categoria_Fuente']", 'symmetrical': 'False'}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'fuente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_5a']"})
        },
        u'analisis.pregunta_6a': {
            'Meta': {'object_name': 'Pregunta_6a'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prioritizado': ('django.db.models.fields.IntegerField', [], {}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema']", 'symmetrical': 'False'}),
            'ubicacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Ubicacion']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_6c': {
            'Meta': {'object_name': 'Pregunta_6c'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_6a']"}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Organizaciones']"}),
            'papel': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Papel']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_6d': {
            'Meta': {'object_name': 'Pregunta_6d'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Categoria']", 'symmetrical': 'False'}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_6a']"})
        },
        u'analisis.pregunta_6e': {
            'Meta': {'object_name': 'Pregunta_6e'},
            'categoria_conocimient': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Categoria_Conocimiento']", 'symmetrical': 'False'}),
            'categoria_innovacio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Categoria_Innovacion']"}),
            'conocimient': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_6a']"})
        },
        u'analisis.pregunta_7a': {
            'Meta': {'object_name': 'Pregunta_7a'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seleccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Seleccion_7a']", 'symmetrical': 'False'}),
            'ubicacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Ubicacion']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_7b': {
            'Meta': {'object_name': 'Pregunta_7b'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seleccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Seleccion_7b']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_8': {
            'Meta': {'object_name': 'Pregunta_8'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Organizaciones']"}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'profundidad': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema_Relacion']", 'symmetrical': 'False'}),
            'territorio': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'analisis.pregunta_9': {
            'Meta': {'object_name': 'Pregunta_9'},
            'conocimiento': ('django.db.models.fields.IntegerField', [], {}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'experiencia': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'papel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prioridad': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tema': ('django.db.models.fields.IntegerField', [], {})
        },
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
        u'configuracion.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.categoria_conocimiento': {
            'Meta': {'object_name': 'Categoria_Conocimiento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.categoria_fuente': {
            'Meta': {'object_name': 'Categoria_Fuente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.categoria_innovacion': {
            'Meta': {'object_name': 'Categoria_Innovacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.grupo': {
            'Meta': {'object_name': 'Grupo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.papel': {
            'Meta': {'object_name': 'Papel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        u'configuracion.seleccion_7a': {
            'Meta': {'object_name': 'Seleccion_7a'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.seleccion_7b': {
            'Meta': {'object_name': 'Seleccion_7b'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.sitioaccion': {
            'Meta': {'object_name': 'SitioAccion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'configuracion.socio': {
            'Meta': {'object_name': 'Socio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'socio': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.tema': {
            'Meta': {'object_name': 'Tema'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'configuracion.tema_relacion': {
            'Meta': {'object_name': 'Tema_Relacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.tipo_estudio': {
            'Meta': {'object_name': 'Tipo_Estudio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.ubicacion': {
            'Meta': {'object_name': 'Ubicacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        }
    }

    complete_apps = ['analisis']