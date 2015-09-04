# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CampoAccion'
        db.create_table(u'mapeo_campoaccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'mapeo', ['CampoAccion'])

        # Adding model 'RubrosAgropecuarios'
        db.create_table(u'mapeo_rubrosagropecuarios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'mapeo', ['RubrosAgropecuarios'])

        # Adding model 'RubrosNoAgropecuarios'
        db.create_table(u'mapeo_rubrosnoagropecuarios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'mapeo', ['RubrosNoAgropecuarios'])

        # Adding model 'Proyectos'
        db.create_table(u'mapeo_proyectos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('corto', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('inicio', self.gf('django.db.models.fields.DateField')()),
            ('finalizacion', self.gf('django.db.models.fields.DateField')()),
            ('ejecutora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Organizaciones'])),
            ('informacion', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'mapeo', ['Proyectos'])

        # Adding M2M table for field alianza on 'Proyectos'
        m2m_table_name = db.shorten_name(u'mapeo_proyectos_alianza')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyectos', models.ForeignKey(orm[u'mapeo.proyectos'], null=False)),
            ('plataforma', models.ForeignKey(orm[u'configuracion.plataforma'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyectos_id', 'plataforma_id'])

        # Adding M2M table for field influencia on 'Proyectos'
        m2m_table_name = db.shorten_name(u'mapeo_proyectos_influencia')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyectos', models.ForeignKey(orm[u'mapeo.proyectos'], null=False)),
            ('municipio', models.ForeignKey(orm[u'lugar.municipio'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyectos_id', 'municipio_id'])

        # Adding M2M table for field socias on 'Proyectos'
        m2m_table_name = db.shorten_name(u'mapeo_proyectos_socias')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyectos', models.ForeignKey(orm[u'mapeo.proyectos'], null=False)),
            ('organizaciones', models.ForeignKey(orm[u'mapeo.organizaciones'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyectos_id', 'organizaciones_id'])

        # Adding model 'FormaAtencion'
        db.create_table(u'mapeo_formaatencion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'mapeo', ['FormaAtencion'])

        # Adding model 'Productor'
        db.create_table(u'mapeo_productor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Persona'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('finca', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('tamano', self.gf('django.db.models.fields.FloatField')()),
            ('ganado', self.gf('django.db.models.fields.IntegerField')()),
            ('rubro_principal_agro', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'dos', to=orm['mapeo.RubrosAgropecuarios'])),
            ('rubro_principal_no_agro', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'cuatro', to=orm['mapeo.RubrosNoAgropecuarios'])),
            ('jefe', self.gf('django.db.models.fields.IntegerField')()),
            ('tipologia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mapeo', ['Productor'])

        # Adding M2M table for field organizacion on 'Productor'
        m2m_table_name = db.shorten_name(u'mapeo_productor_organizacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productor', models.ForeignKey(orm[u'mapeo.productor'], null=False)),
            ('organizaciones', models.ForeignKey(orm[u'mapeo.organizaciones'], null=False))
        ))
        db.create_unique(m2m_table_name, ['productor_id', 'organizaciones_id'])

        # Adding M2M table for field rubros_agro on 'Productor'
        m2m_table_name = db.shorten_name(u'mapeo_productor_rubros_agro')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productor', models.ForeignKey(orm[u'mapeo.productor'], null=False)),
            ('rubrosagropecuarios', models.ForeignKey(orm[u'mapeo.rubrosagropecuarios'], null=False))
        ))
        db.create_unique(m2m_table_name, ['productor_id', 'rubrosagropecuarios_id'])

        # Adding M2M table for field rubros_no_agro on 'Productor'
        m2m_table_name = db.shorten_name(u'mapeo_productor_rubros_no_agro')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productor', models.ForeignKey(orm[u'mapeo.productor'], null=False)),
            ('rubrosnoagropecuarios', models.ForeignKey(orm[u'mapeo.rubrosnoagropecuarios'], null=False))
        ))
        db.create_unique(m2m_table_name, ['productor_id', 'rubrosnoagropecuarios_id'])

        # Adding M2M table for field fuente on 'Productor'
        m2m_table_name = db.shorten_name(u'mapeo_productor_fuente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productor', models.ForeignKey(orm[u'mapeo.productor'], null=False)),
            ('fuentemanoobra', models.ForeignKey(orm[u'mapeo.fuentemanoobra'], null=False))
        ))
        db.create_unique(m2m_table_name, ['productor_id', 'fuentemanoobra_id'])

        # Adding M2M table for field proyecto on 'Productor'
        m2m_table_name = db.shorten_name(u'mapeo_productor_proyecto')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productor', models.ForeignKey(orm[u'mapeo.productor'], null=False)),
            ('proyectos', models.ForeignKey(orm[u'mapeo.proyectos'], null=False))
        ))
        db.create_unique(m2m_table_name, ['productor_id', 'proyectos_id'])

        # Adding model 'Especialidades'
        db.create_table(u'mapeo_especialidades', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'mapeo', ['Especialidades'])

        # Adding model 'TecnicoEspInvestigador'
        db.create_table(u'mapeo_tecnicoespinvestigador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Persona'])),
            ('formacion', self.gf('django.db.models.fields.IntegerField')()),
            ('experiencia', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'mapeo', ['TecnicoEspInvestigador'])

        # Adding M2M table for field especialidad on 'TecnicoEspInvestigador'
        m2m_table_name = db.shorten_name(u'mapeo_tecnicoespinvestigador_especialidad')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tecnicoespinvestigador', models.ForeignKey(orm[u'mapeo.tecnicoespinvestigador'], null=False)),
            ('especialidades', models.ForeignKey(orm[u'mapeo.especialidades'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tecnicoespinvestigador_id', 'especialidades_id'])

        # Adding M2M table for field pertenece on 'TecnicoEspInvestigador'
        m2m_table_name = db.shorten_name(u'mapeo_tecnicoespinvestigador_pertenece')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tecnicoespinvestigador', models.ForeignKey(orm[u'mapeo.tecnicoespinvestigador'], null=False)),
            ('organizaciones', models.ForeignKey(orm[u'mapeo.organizaciones'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tecnicoespinvestigador_id', 'organizaciones_id'])

        # Adding M2M table for field proyecto on 'TecnicoEspInvestigador'
        m2m_table_name = db.shorten_name(u'mapeo_tecnicoespinvestigador_proyecto')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tecnicoespinvestigador', models.ForeignKey(orm[u'mapeo.tecnicoespinvestigador'], null=False)),
            ('proyectos', models.ForeignKey(orm[u'mapeo.proyectos'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tecnicoespinvestigador_id', 'proyectos_id'])

        # Adding model 'Decisor'
        db.create_table(u'mapeo_decisor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Persona'])),
        ))
        db.send_create_signal(u'mapeo', ['Decisor'])

        # Adding M2M table for field nivel on 'Decisor'
        m2m_table_name = db.shorten_name(u'mapeo_decisor_nivel')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('decisor', models.ForeignKey(orm[u'mapeo.decisor'], null=False)),
            ('accionar', models.ForeignKey(orm[u'mapeo.accionar'], null=False))
        ))
        db.create_unique(m2m_table_name, ['decisor_id', 'accionar_id'])

        # Adding M2M table for field campo on 'Decisor'
        m2m_table_name = db.shorten_name(u'mapeo_decisor_campo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('decisor', models.ForeignKey(orm[u'mapeo.decisor'], null=False)),
            ('campoaccion', models.ForeignKey(orm[u'mapeo.campoaccion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['decisor_id', 'campoaccion_id'])

        # Adding M2M table for field pertenece on 'Decisor'
        m2m_table_name = db.shorten_name(u'mapeo_decisor_pertenece')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('decisor', models.ForeignKey(orm[u'mapeo.decisor'], null=False)),
            ('organizaciones', models.ForeignKey(orm[u'mapeo.organizaciones'], null=False))
        ))
        db.create_unique(m2m_table_name, ['decisor_id', 'organizaciones_id'])

        # Adding M2M table for field proyecto on 'Decisor'
        m2m_table_name = db.shorten_name(u'mapeo_decisor_proyecto')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('decisor', models.ForeignKey(orm[u'mapeo.decisor'], null=False)),
            ('proyectos', models.ForeignKey(orm[u'mapeo.proyectos'], null=False))
        ))
        db.create_unique(m2m_table_name, ['decisor_id', 'proyectos_id'])

        # Adding model 'Lideres'
        db.create_table(u'mapeo_lideres', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Persona'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('finca', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('tamano', self.gf('django.db.models.fields.FloatField')()),
            ('ganado', self.gf('django.db.models.fields.IntegerField')()),
            ('rubro_principal_agro', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'principal', to=orm['mapeo.RubrosAgropecuarios'])),
            ('rubro_principal_no_agro', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'principalno', to=orm['mapeo.RubrosNoAgropecuarios'])),
            ('jefe', self.gf('django.db.models.fields.IntegerField')()),
            ('tipologia', self.gf('django.db.models.fields.IntegerField')()),
            ('atiende', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mapeo', ['Lideres'])

        # Adding M2M table for field organizacion on 'Lideres'
        m2m_table_name = db.shorten_name(u'mapeo_lideres_organizacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lideres', models.ForeignKey(orm[u'mapeo.lideres'], null=False)),
            ('organizaciones', models.ForeignKey(orm[u'mapeo.organizaciones'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lideres_id', 'organizaciones_id'])

        # Adding M2M table for field rubros_agro on 'Lideres'
        m2m_table_name = db.shorten_name(u'mapeo_lideres_rubros_agro')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lideres', models.ForeignKey(orm[u'mapeo.lideres'], null=False)),
            ('rubrosagropecuarios', models.ForeignKey(orm[u'mapeo.rubrosagropecuarios'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lideres_id', 'rubrosagropecuarios_id'])

        # Adding M2M table for field rubros_no_agro on 'Lideres'
        m2m_table_name = db.shorten_name(u'mapeo_lideres_rubros_no_agro')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lideres', models.ForeignKey(orm[u'mapeo.lideres'], null=False)),
            ('rubrosnoagropecuarios', models.ForeignKey(orm[u'mapeo.rubrosnoagropecuarios'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lideres_id', 'rubrosnoagropecuarios_id'])

        # Adding M2M table for field fuente on 'Lideres'
        m2m_table_name = db.shorten_name(u'mapeo_lideres_fuente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lideres', models.ForeignKey(orm[u'mapeo.lideres'], null=False)),
            ('fuentemanoobra', models.ForeignKey(orm[u'mapeo.fuentemanoobra'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lideres_id', 'fuentemanoobra_id'])

        # Adding M2M table for field forma_atiende on 'Lideres'
        m2m_table_name = db.shorten_name(u'mapeo_lideres_forma_atiende')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lideres', models.ForeignKey(orm[u'mapeo.lideres'], null=False)),
            ('formaatencion', models.ForeignKey(orm[u'mapeo.formaatencion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lideres_id', 'formaatencion_id'])

        # Adding M2M table for field proyecto on 'Lideres'
        m2m_table_name = db.shorten_name(u'mapeo_lideres_proyecto')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lideres', models.ForeignKey(orm[u'mapeo.lideres'], null=False)),
            ('proyectos', models.ForeignKey(orm[u'mapeo.proyectos'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lideres_id', 'proyectos_id'])

        # Adding model 'Accionar'
        db.create_table(u'mapeo_accionar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'mapeo', ['Accionar'])

        # Adding model 'FuenteManoObra'
        db.create_table(u'mapeo_fuentemanoobra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'mapeo', ['FuenteManoObra'])

        # Deleting field 'Persona.nivel_educacion'
        db.delete_column(u'mapeo_persona', 'nivel_educacion')

        # Deleting field 'Persona.finca'
        db.delete_column(u'mapeo_persona', 'finca')

        # Adding field 'Persona.tipo_persona'
        db.add_column(u'mapeo_persona', 'tipo_persona',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field organizacion on 'Persona'
        db.delete_table(db.shorten_name(u'mapeo_persona_organizacion'))


    def backwards(self, orm):
        # Deleting model 'CampoAccion'
        db.delete_table(u'mapeo_campoaccion')

        # Deleting model 'RubrosAgropecuarios'
        db.delete_table(u'mapeo_rubrosagropecuarios')

        # Deleting model 'RubrosNoAgropecuarios'
        db.delete_table(u'mapeo_rubrosnoagropecuarios')

        # Deleting model 'Proyectos'
        db.delete_table(u'mapeo_proyectos')

        # Removing M2M table for field alianza on 'Proyectos'
        db.delete_table(db.shorten_name(u'mapeo_proyectos_alianza'))

        # Removing M2M table for field influencia on 'Proyectos'
        db.delete_table(db.shorten_name(u'mapeo_proyectos_influencia'))

        # Removing M2M table for field socias on 'Proyectos'
        db.delete_table(db.shorten_name(u'mapeo_proyectos_socias'))

        # Deleting model 'FormaAtencion'
        db.delete_table(u'mapeo_formaatencion')

        # Deleting model 'Productor'
        db.delete_table(u'mapeo_productor')

        # Removing M2M table for field organizacion on 'Productor'
        db.delete_table(db.shorten_name(u'mapeo_productor_organizacion'))

        # Removing M2M table for field rubros_agro on 'Productor'
        db.delete_table(db.shorten_name(u'mapeo_productor_rubros_agro'))

        # Removing M2M table for field rubros_no_agro on 'Productor'
        db.delete_table(db.shorten_name(u'mapeo_productor_rubros_no_agro'))

        # Removing M2M table for field fuente on 'Productor'
        db.delete_table(db.shorten_name(u'mapeo_productor_fuente'))

        # Removing M2M table for field proyecto on 'Productor'
        db.delete_table(db.shorten_name(u'mapeo_productor_proyecto'))

        # Deleting model 'Especialidades'
        db.delete_table(u'mapeo_especialidades')

        # Deleting model 'TecnicoEspInvestigador'
        db.delete_table(u'mapeo_tecnicoespinvestigador')

        # Removing M2M table for field especialidad on 'TecnicoEspInvestigador'
        db.delete_table(db.shorten_name(u'mapeo_tecnicoespinvestigador_especialidad'))

        # Removing M2M table for field pertenece on 'TecnicoEspInvestigador'
        db.delete_table(db.shorten_name(u'mapeo_tecnicoespinvestigador_pertenece'))

        # Removing M2M table for field proyecto on 'TecnicoEspInvestigador'
        db.delete_table(db.shorten_name(u'mapeo_tecnicoespinvestigador_proyecto'))

        # Deleting model 'Decisor'
        db.delete_table(u'mapeo_decisor')

        # Removing M2M table for field nivel on 'Decisor'
        db.delete_table(db.shorten_name(u'mapeo_decisor_nivel'))

        # Removing M2M table for field campo on 'Decisor'
        db.delete_table(db.shorten_name(u'mapeo_decisor_campo'))

        # Removing M2M table for field pertenece on 'Decisor'
        db.delete_table(db.shorten_name(u'mapeo_decisor_pertenece'))

        # Removing M2M table for field proyecto on 'Decisor'
        db.delete_table(db.shorten_name(u'mapeo_decisor_proyecto'))

        # Deleting model 'Lideres'
        db.delete_table(u'mapeo_lideres')

        # Removing M2M table for field organizacion on 'Lideres'
        db.delete_table(db.shorten_name(u'mapeo_lideres_organizacion'))

        # Removing M2M table for field rubros_agro on 'Lideres'
        db.delete_table(db.shorten_name(u'mapeo_lideres_rubros_agro'))

        # Removing M2M table for field rubros_no_agro on 'Lideres'
        db.delete_table(db.shorten_name(u'mapeo_lideres_rubros_no_agro'))

        # Removing M2M table for field fuente on 'Lideres'
        db.delete_table(db.shorten_name(u'mapeo_lideres_fuente'))

        # Removing M2M table for field forma_atiende on 'Lideres'
        db.delete_table(db.shorten_name(u'mapeo_lideres_forma_atiende'))

        # Removing M2M table for field proyecto on 'Lideres'
        db.delete_table(db.shorten_name(u'mapeo_lideres_proyecto'))

        # Deleting model 'Accionar'
        db.delete_table(u'mapeo_accionar')

        # Deleting model 'FuenteManoObra'
        db.delete_table(u'mapeo_fuentemanoobra')

        # Adding field 'Persona.nivel_educacion'
        db.add_column(u'mapeo_persona', 'nivel_educacion',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Persona.finca'
        db.add_column(u'mapeo_persona', 'finca',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Persona.tipo_persona'
        db.delete_column(u'mapeo_persona', 'tipo_persona')

        # Adding M2M table for field organizacion on 'Persona'
        m2m_table_name = db.shorten_name(u'mapeo_persona_organizacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('persona', models.ForeignKey(orm[u'mapeo.persona'], null=False)),
            ('organizaciones', models.ForeignKey(orm[u'mapeo.organizaciones'], null=False))
        ))
        db.create_unique(m2m_table_name, ['persona_id', 'organizaciones_id'])


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