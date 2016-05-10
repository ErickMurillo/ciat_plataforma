# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Monitoreo'
        db.create_table(u'ficha_granos_basicos_monitoreo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Persona'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('visita', self.gf('django.db.models.fields.IntegerField')()),
            ('areas', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=17)),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Monitoreo'])

        # Adding model 'DatosMonitoreo'
        db.create_table(u'ficha_granos_basicos_datosmonitoreo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ciclo_productivo', self.gf('django.db.models.fields.IntegerField')()),
            ('cultivo', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_siembra', self.gf('django.db.models.fields.DateField')()),
            ('fecha_cosecha', self.gf('django.db.models.fields.DateField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['DatosMonitoreo'])

        # Adding model 'DatosParcela'
        db.create_table(u'ficha_granos_basicos_datosparcela', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('edad_parcela', self.gf('django.db.models.fields.FloatField')()),
            ('latitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('direccion_viento', self.gf('django.db.models.fields.IntegerField')()),
            ('percepcion_fertilidad', self.gf('django.db.models.fields.IntegerField')()),
            ('tamano_parcela', self.gf('django.db.models.fields.FloatField')()),
            ('profundidad_capa', self.gf('django.db.models.fields.FloatField')()),
            ('acceso_agua', self.gf('django.db.models.fields.IntegerField')()),
            ('fuente_agua', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=7, null=True, blank=True)),
            ('distancia', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['DatosParcela'])

        # Adding model 'DistribucionPendiente'
        db.create_table(u'ficha_granos_basicos_distribucionpendiente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seleccion', self.gf('django.db.models.fields.IntegerField')()),
            ('inclinado', self.gf('django.db.models.fields.FloatField')()),
            ('plano', self.gf('django.db.models.fields.FloatField')()),
            ('ondulado', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['DistribucionPendiente'])

        # Adding model 'RecursosSiembra'
        db.create_table(u'ficha_granos_basicos_recursossiembra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rubro', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['RecursosSiembra'])

        # Adding model 'HistorialRendimiento'
        db.create_table(u'ficha_granos_basicos_historialrendimiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rubro', self.gf('django.db.models.fields.IntegerField')()),
            ('ciclo_productivo', self.gf('django.db.models.fields.IntegerField')()),
            ('anio', self.gf('django.db.models.fields.IntegerField')()),
            ('rendimiento', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['HistorialRendimiento'])

        # Adding model 'Semillas'
        db.create_table(u'ficha_granos_basicos_semillas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('semilla_frijol', self.gf('django.db.models.fields.IntegerField')()),
            ('semilla_maiz', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_frijol', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nombre_maiz', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Semillas'])

        # Adding model 'ProcedenciaSemilla'
        db.create_table(u'ficha_granos_basicos_procedenciasemilla', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rubro', self.gf('django.db.models.fields.IntegerField')()),
            ('procedencia', self.gf('django.db.models.fields.IntegerField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['ProcedenciaSemilla'])

        # Adding model 'PruebaGerminacion'
        db.create_table(u'ficha_granos_basicos_pruebagerminacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rubro', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('porcentaje', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['PruebaGerminacion'])

        # Adding model 'ParametrosSuelo'
        db.create_table(u'ficha_granos_basicos_parametrossuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parametro', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('unidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nivel_critico', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('nivel_suficiencia', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['ParametrosSuelo'])

        # Adding model 'Suelo'
        db.create_table(u'ficha_granos_basicos_suelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parametro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.ParametrosSuelo'])),
            ('resultado', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Suelo'])

        # Adding model 'Especies'
        db.create_table(u'ficha_granos_basicos_especies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_popular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nombre_cientifico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('reconocimiento', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('dano', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('control_cultural', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('control_biologico', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('control_quimico', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('rubro', self.gf('django.db.models.fields.IntegerField')()),
            ('umbral', self.gf('django.db.models.fields.IntegerField')()),
            ('rango_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rango_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Especies'])

        # Adding model 'FotosEspecies'
        db.create_table(u'ficha_granos_basicos_fotosespecies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Especies'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['FotosEspecies'])

        # Adding model 'Macrofauna'
        db.create_table(u'ficha_granos_basicos_macrofauna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Especies'])),
            ('est1', self.gf('django.db.models.fields.IntegerField')()),
            ('est2', self.gf('django.db.models.fields.IntegerField')()),
            ('est3', self.gf('django.db.models.fields.IntegerField')()),
            ('est4', self.gf('django.db.models.fields.IntegerField')()),
            ('est5', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Macrofauna'])

        # Adding model 'MonitoreoMalezas'
        db.create_table(u'ficha_granos_basicos_monitoreomalezas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('cobertura_total', self.gf('django.db.models.fields.FloatField')()),
            ('gramineas', self.gf('django.db.models.fields.FloatField')()),
            ('hoja_ancha', self.gf('django.db.models.fields.FloatField')()),
            ('ciperaceas', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['MonitoreoMalezas'])

        # Adding model 'TiposMalezas'
        db.create_table(u'ficha_granos_basicos_tiposmalezas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_popular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nombre_cientifico', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('categoria', self.gf('django.db.models.fields.IntegerField')()),
            ('ciclo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['TiposMalezas'])

        # Adding model 'TablaMalezas'
        db.create_table(u'ficha_granos_basicos_tablamalezas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('maleza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.TiposMalezas'])),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['TablaMalezas'])

        # Adding model 'PoblacionFrijol'
        db.create_table(u'ficha_granos_basicos_poblacionfrijol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('distancia_frijol', self.gf('django.db.models.fields.FloatField')()),
            ('est1', self.gf('django.db.models.fields.IntegerField')()),
            ('est2', self.gf('django.db.models.fields.IntegerField')()),
            ('est3', self.gf('django.db.models.fields.IntegerField')()),
            ('est4', self.gf('django.db.models.fields.IntegerField')()),
            ('est5', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
            ('numero_surcos', self.gf('django.db.models.fields.FloatField')()),
            ('metros_lineales', self.gf('django.db.models.fields.FloatField')()),
            ('poblacion', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['PoblacionFrijol'])

        # Adding model 'PoblacionMaiz'
        db.create_table(u'ficha_granos_basicos_poblacionmaiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('distancia_maiz', self.gf('django.db.models.fields.FloatField')()),
            ('est1', self.gf('django.db.models.fields.IntegerField')()),
            ('est2', self.gf('django.db.models.fields.IntegerField')()),
            ('est3', self.gf('django.db.models.fields.IntegerField')()),
            ('est4', self.gf('django.db.models.fields.IntegerField')()),
            ('est5', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
            ('numero_surcos', self.gf('django.db.models.fields.FloatField')()),
            ('metros_lineales', self.gf('django.db.models.fields.FloatField')()),
            ('poblacion', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['PoblacionMaiz'])

        # Adding model 'VigorFrijol'
        db.create_table(u'ficha_granos_basicos_vigorfrijol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('est1', self.gf('django.db.models.fields.IntegerField')()),
            ('est2', self.gf('django.db.models.fields.IntegerField')()),
            ('est3', self.gf('django.db.models.fields.IntegerField')()),
            ('est4', self.gf('django.db.models.fields.IntegerField')()),
            ('est5', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
            ('estimado_plantas', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['VigorFrijol'])

        # Adding model 'VigorMaiz'
        db.create_table(u'ficha_granos_basicos_vigormaiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas', self.gf('django.db.models.fields.IntegerField')()),
            ('est1', self.gf('django.db.models.fields.IntegerField')()),
            ('est2', self.gf('django.db.models.fields.IntegerField')()),
            ('est3', self.gf('django.db.models.fields.IntegerField')()),
            ('est4', self.gf('django.db.models.fields.IntegerField')()),
            ('est5', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
            ('estimado_plantas', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['VigorMaiz'])

        # Adding model 'PlagasFrijol'
        db.create_table(u'ficha_granos_basicos_plagasfrijol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plaga', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Especies'])),
            ('presencia_1', self.gf('django.db.models.fields.FloatField')()),
            ('presencia_2', self.gf('django.db.models.fields.FloatField')()),
            ('presencia_3', self.gf('django.db.models.fields.FloatField')()),
            ('presencia_4', self.gf('django.db.models.fields.FloatField')()),
            ('presencia_5', self.gf('django.db.models.fields.FloatField')()),
            ('promedio_presencia', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_1', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_2', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_3', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_4', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_5', self.gf('django.db.models.fields.FloatField')()),
            ('promedio_dano', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['PlagasFrijol'])

        # Adding model 'PlagasMaiz'
        db.create_table(u'ficha_granos_basicos_plagasmaiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plaga', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Especies'])),
            ('presencia_1', self.gf('django.db.models.fields.FloatField')()),
            ('presencia_2', self.gf('django.db.models.fields.FloatField')()),
            ('presencia_3', self.gf('django.db.models.fields.FloatField')()),
            ('presencia_4', self.gf('django.db.models.fields.FloatField')()),
            ('presencia_5', self.gf('django.db.models.fields.FloatField')()),
            ('promedio_presencia', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_1', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_2', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_3', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_4', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_dano_5', self.gf('django.db.models.fields.FloatField')()),
            ('promedio_dano', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['PlagasMaiz'])

        # Adding model 'EnfermedadesFrijol'
        db.create_table(u'ficha_granos_basicos_enfermedadesfrijol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enfermedad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Especies'])),
            ('planta_1', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_2', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_3', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_4', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_5', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['EnfermedadesFrijol'])

        # Adding model 'EnfermedadesMaiz'
        db.create_table(u'ficha_granos_basicos_enfermedadesmaiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enfermedad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Especies'])),
            ('planta_1', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_2', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_3', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_4', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_5', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['EnfermedadesMaiz'])

        # Adding model 'EstimadoCosechaFrijol'
        db.create_table(u'ficha_granos_basicos_estimadocosechafrijol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estacion', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_1', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_2', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_3', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_4', self.gf('django.db.models.fields.IntegerField')()),
            ('planta_5', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['EstimadoCosechaFrijol'])

        # Adding model 'GranosPlanta'
        db.create_table(u'ficha_granos_basicos_granosplanta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['GranosPlanta'])

        # Adding model 'EstimadoCosechaMaiz'
        db.create_table(u'ficha_granos_basicos_estimadocosechamaiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mazorca', self.gf('django.db.models.fields.IntegerField')()),
            ('estacion_1', self.gf('django.db.models.fields.IntegerField')()),
            ('estacion_2', self.gf('django.db.models.fields.IntegerField')()),
            ('estacion_3', self.gf('django.db.models.fields.IntegerField')()),
            ('estacion_4', self.gf('django.db.models.fields.IntegerField')()),
            ('estacion_5', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['EstimadoCosechaMaiz'])

        # Adding model 'EstimadoCosechaMaiz2'
        db.create_table(u'ficha_granos_basicos_estimadocosechamaiz2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mazorca', self.gf('django.db.models.fields.IntegerField')()),
            ('peso', self.gf('django.db.models.fields.FloatField')()),
            ('peso_promedio', self.gf('django.db.models.fields.IntegerField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['EstimadoCosechaMaiz2'])

        # Adding model 'SobreCosecha'
        db.create_table(u'ficha_granos_basicos_sobrecosecha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rubro', self.gf('django.db.models.fields.IntegerField')()),
            ('cosecha', self.gf('django.db.models.fields.FloatField')()),
            ('venta', self.gf('django.db.models.fields.FloatField')()),
            ('almacenamiento', self.gf('django.db.models.fields.FloatField')()),
            ('precio_mercado', self.gf('django.db.models.fields.FloatField')()),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['SobreCosecha'])

        # Adding model 'TratamientoSemilla'
        db.create_table(u'ficha_granos_basicos_tratamientosemilla', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dosis', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('preparacion', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['TratamientoSemilla'])

        # Adding model 'CuradoSemilla'
        db.create_table(u'ficha_granos_basicos_curadosemilla', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('monitoreo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['CuradoSemilla'])

        # Adding M2M table for field tratamiento on 'CuradoSemilla'
        m2m_table_name = db.shorten_name(u'ficha_granos_basicos_curadosemilla_tratamiento')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curadosemilla', models.ForeignKey(orm[u'ficha_granos_basicos.curadosemilla'], null=False)),
            ('tratamientosemilla', models.ForeignKey(orm[u'ficha_granos_basicos.tratamientosemilla'], null=False))
        ))
        db.create_unique(m2m_table_name, ['curadosemilla_id', 'tratamientosemilla_id'])

        # Adding model 'Gastos'
        db.create_table(u'ficha_granos_basicos_gastos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
            ('fecha_siembra', self.gf('django.db.models.fields.DateField')()),
            ('rubro', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Gastos'])

        # Adding model 'TablaGastos'
        db.create_table(u'ficha_granos_basicos_tablagastos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('actividad', self.gf('django.db.models.fields.IntegerField')()),
            ('hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('dias_persona', self.gf('django.db.models.fields.IntegerField')()),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('gastos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Gastos'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['TablaGastos'])

        # Adding model 'Productos'
        db.create_table(u'ficha_granos_basicos_productos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_comercial', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('principio_activo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('categoria', self.gf('django.db.models.fields.IntegerField')()),
            ('presentacion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Productos'])

        # Adding model 'Insumos'
        db.create_table(u'ficha_granos_basicos_insumos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
            ('fecha_siembra', self.gf('django.db.models.fields.DateField')()),
            ('rubro', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Insumos'])

        # Adding model 'TablaInsumos'
        db.create_table(u'ficha_granos_basicos_tablainsumos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Productos'])),
            ('unidades', self.gf('django.db.models.fields.FloatField')()),
            ('bombas', self.gf('django.db.models.fields.FloatField')()),
            ('insumos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Insumos'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['TablaInsumos'])

        # Adding model 'Liga_Nested'
        db.create_table(u'ficha_granos_basicos_liga_nested', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Productos'])),
            ('unidades', self.gf('django.db.models.fields.FloatField')()),
            ('tabla_insumos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.TablaInsumos'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Liga_Nested'])

        # Adding model 'TomaDecisiones'
        db.create_table(u'ficha_granos_basicos_tomadecisiones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['TomaDecisiones'])

        # Adding model 'TablaDecisiones'
        db.create_table(u'ficha_granos_basicos_tabladecisiones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visita', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('decision', self.gf('django.db.models.fields.TextField')()),
            ('seleccion', self.gf('django.db.models.fields.IntegerField')()),
            ('porque', self.gf('django.db.models.fields.TextField')()),
            ('toma_deciciones', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.TomaDecisiones'])),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['TablaDecisiones'])


    def backwards(self, orm):
        # Deleting model 'Monitoreo'
        db.delete_table(u'ficha_granos_basicos_monitoreo')

        # Deleting model 'DatosMonitoreo'
        db.delete_table(u'ficha_granos_basicos_datosmonitoreo')

        # Deleting model 'DatosParcela'
        db.delete_table(u'ficha_granos_basicos_datosparcela')

        # Deleting model 'DistribucionPendiente'
        db.delete_table(u'ficha_granos_basicos_distribucionpendiente')

        # Deleting model 'RecursosSiembra'
        db.delete_table(u'ficha_granos_basicos_recursossiembra')

        # Deleting model 'HistorialRendimiento'
        db.delete_table(u'ficha_granos_basicos_historialrendimiento')

        # Deleting model 'Semillas'
        db.delete_table(u'ficha_granos_basicos_semillas')

        # Deleting model 'ProcedenciaSemilla'
        db.delete_table(u'ficha_granos_basicos_procedenciasemilla')

        # Deleting model 'PruebaGerminacion'
        db.delete_table(u'ficha_granos_basicos_pruebagerminacion')

        # Deleting model 'ParametrosSuelo'
        db.delete_table(u'ficha_granos_basicos_parametrossuelo')

        # Deleting model 'Suelo'
        db.delete_table(u'ficha_granos_basicos_suelo')

        # Deleting model 'Especies'
        db.delete_table(u'ficha_granos_basicos_especies')

        # Deleting model 'FotosEspecies'
        db.delete_table(u'ficha_granos_basicos_fotosespecies')

        # Deleting model 'Macrofauna'
        db.delete_table(u'ficha_granos_basicos_macrofauna')

        # Deleting model 'MonitoreoMalezas'
        db.delete_table(u'ficha_granos_basicos_monitoreomalezas')

        # Deleting model 'TiposMalezas'
        db.delete_table(u'ficha_granos_basicos_tiposmalezas')

        # Deleting model 'TablaMalezas'
        db.delete_table(u'ficha_granos_basicos_tablamalezas')

        # Deleting model 'PoblacionFrijol'
        db.delete_table(u'ficha_granos_basicos_poblacionfrijol')

        # Deleting model 'PoblacionMaiz'
        db.delete_table(u'ficha_granos_basicos_poblacionmaiz')

        # Deleting model 'VigorFrijol'
        db.delete_table(u'ficha_granos_basicos_vigorfrijol')

        # Deleting model 'VigorMaiz'
        db.delete_table(u'ficha_granos_basicos_vigormaiz')

        # Deleting model 'PlagasFrijol'
        db.delete_table(u'ficha_granos_basicos_plagasfrijol')

        # Deleting model 'PlagasMaiz'
        db.delete_table(u'ficha_granos_basicos_plagasmaiz')

        # Deleting model 'EnfermedadesFrijol'
        db.delete_table(u'ficha_granos_basicos_enfermedadesfrijol')

        # Deleting model 'EnfermedadesMaiz'
        db.delete_table(u'ficha_granos_basicos_enfermedadesmaiz')

        # Deleting model 'EstimadoCosechaFrijol'
        db.delete_table(u'ficha_granos_basicos_estimadocosechafrijol')

        # Deleting model 'GranosPlanta'
        db.delete_table(u'ficha_granos_basicos_granosplanta')

        # Deleting model 'EstimadoCosechaMaiz'
        db.delete_table(u'ficha_granos_basicos_estimadocosechamaiz')

        # Deleting model 'EstimadoCosechaMaiz2'
        db.delete_table(u'ficha_granos_basicos_estimadocosechamaiz2')

        # Deleting model 'SobreCosecha'
        db.delete_table(u'ficha_granos_basicos_sobrecosecha')

        # Deleting model 'TratamientoSemilla'
        db.delete_table(u'ficha_granos_basicos_tratamientosemilla')

        # Deleting model 'CuradoSemilla'
        db.delete_table(u'ficha_granos_basicos_curadosemilla')

        # Removing M2M table for field tratamiento on 'CuradoSemilla'
        db.delete_table(db.shorten_name(u'ficha_granos_basicos_curadosemilla_tratamiento'))

        # Deleting model 'Gastos'
        db.delete_table(u'ficha_granos_basicos_gastos')

        # Deleting model 'TablaGastos'
        db.delete_table(u'ficha_granos_basicos_tablagastos')

        # Deleting model 'Productos'
        db.delete_table(u'ficha_granos_basicos_productos')

        # Deleting model 'Insumos'
        db.delete_table(u'ficha_granos_basicos_insumos')

        # Deleting model 'TablaInsumos'
        db.delete_table(u'ficha_granos_basicos_tablainsumos')

        # Deleting model 'Liga_Nested'
        db.delete_table(u'ficha_granos_basicos_liga_nested')

        # Deleting model 'TomaDecisiones'
        db.delete_table(u'ficha_granos_basicos_tomadecisiones')

        # Deleting model 'TablaDecisiones'
        db.delete_table(u'ficha_granos_basicos_tabladecisiones')


    models = {
        u'ficha_granos_basicos.curadosemilla': {
            'Meta': {'object_name': 'CuradoSemilla'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'tratamiento': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ficha_granos_basicos.TratamientoSemilla']", 'symmetrical': 'False'})
        },
        u'ficha_granos_basicos.datosmonitoreo': {
            'Meta': {'object_name': 'DatosMonitoreo'},
            'ciclo_productivo': ('django.db.models.fields.IntegerField', [], {}),
            'cultivo': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_cosecha': ('django.db.models.fields.DateField', [], {}),
            'fecha_siembra': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"})
        },
        u'ficha_granos_basicos.datosparcela': {
            'Meta': {'object_name': 'DatosParcela'},
            'acceso_agua': ('django.db.models.fields.IntegerField', [], {}),
            'direccion_viento': ('django.db.models.fields.IntegerField', [], {}),
            'distancia': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'edad_parcela': ('django.db.models.fields.FloatField', [], {}),
            'fuente_agua': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'percepcion_fertilidad': ('django.db.models.fields.IntegerField', [], {}),
            'profundidad_capa': ('django.db.models.fields.FloatField', [], {}),
            'tamano_parcela': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.distribucionpendiente': {
            'Meta': {'object_name': 'DistribucionPendiente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inclinado': ('django.db.models.fields.FloatField', [], {}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'ondulado': ('django.db.models.fields.FloatField', [], {}),
            'plano': ('django.db.models.fields.FloatField', [], {}),
            'seleccion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.enfermedadesfrijol': {
            'Meta': {'object_name': 'EnfermedadesFrijol'},
            'enfermedad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Especies']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'planta_1': ('django.db.models.fields.IntegerField', [], {}),
            'planta_2': ('django.db.models.fields.IntegerField', [], {}),
            'planta_3': ('django.db.models.fields.IntegerField', [], {}),
            'planta_4': ('django.db.models.fields.IntegerField', [], {}),
            'planta_5': ('django.db.models.fields.IntegerField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.enfermedadesmaiz': {
            'Meta': {'object_name': 'EnfermedadesMaiz'},
            'enfermedad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Especies']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'planta_1': ('django.db.models.fields.IntegerField', [], {}),
            'planta_2': ('django.db.models.fields.IntegerField', [], {}),
            'planta_3': ('django.db.models.fields.IntegerField', [], {}),
            'planta_4': ('django.db.models.fields.IntegerField', [], {}),
            'planta_5': ('django.db.models.fields.IntegerField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.especies': {
            'Meta': {'object_name': 'Especies'},
            'control_biologico': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'control_cultural': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'control_quimico': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dano': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_cientifico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre_popular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rango_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rango_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reconocimiento': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'rubro': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'umbral': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.estimadocosechafrijol': {
            'Meta': {'object_name': 'EstimadoCosechaFrijol'},
            'estacion': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'planta_1': ('django.db.models.fields.IntegerField', [], {}),
            'planta_2': ('django.db.models.fields.IntegerField', [], {}),
            'planta_3': ('django.db.models.fields.IntegerField', [], {}),
            'planta_4': ('django.db.models.fields.IntegerField', [], {}),
            'planta_5': ('django.db.models.fields.IntegerField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.estimadocosechamaiz': {
            'Meta': {'object_name': 'EstimadoCosechaMaiz'},
            'estacion_1': ('django.db.models.fields.IntegerField', [], {}),
            'estacion_2': ('django.db.models.fields.IntegerField', [], {}),
            'estacion_3': ('django.db.models.fields.IntegerField', [], {}),
            'estacion_4': ('django.db.models.fields.IntegerField', [], {}),
            'estacion_5': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mazorca': ('django.db.models.fields.IntegerField', [], {}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'promedio': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.estimadocosechamaiz2': {
            'Meta': {'object_name': 'EstimadoCosechaMaiz2'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mazorca': ('django.db.models.fields.IntegerField', [], {}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'peso': ('django.db.models.fields.FloatField', [], {}),
            'peso_promedio': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.fotosespecies': {
            'Meta': {'object_name': 'FotosEspecies'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Especies']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ficha_granos_basicos.gastos': {
            'Meta': {'object_name': 'Gastos'},
            'fecha_siembra': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'rubro': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.granosplanta': {
            'Meta': {'object_name': 'GranosPlanta'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"})
        },
        u'ficha_granos_basicos.historialrendimiento': {
            'Meta': {'object_name': 'HistorialRendimiento'},
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'ciclo_productivo': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'rendimiento': ('django.db.models.fields.FloatField', [], {}),
            'rubro': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.insumos': {
            'Meta': {'object_name': 'Insumos'},
            'fecha_siembra': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'rubro': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.liga_nested': {
            'Meta': {'object_name': 'Liga_Nested'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Productos']"}),
            'tabla_insumos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.TablaInsumos']"}),
            'unidades': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.macrofauna': {
            'Meta': {'object_name': 'Macrofauna'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Especies']"}),
            'est1': ('django.db.models.fields.IntegerField', [], {}),
            'est2': ('django.db.models.fields.IntegerField', [], {}),
            'est3': ('django.db.models.fields.IntegerField', [], {}),
            'est4': ('django.db.models.fields.IntegerField', [], {}),
            'est5': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'promedio': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.monitoreo': {
            'Meta': {'object_name': 'Monitoreo'},
            'areas': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '17'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Persona']"}),
            'visita': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.monitoreomalezas': {
            'Meta': {'object_name': 'MonitoreoMalezas'},
            'ciperaceas': ('django.db.models.fields.FloatField', [], {}),
            'cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'cobertura_total': ('django.db.models.fields.FloatField', [], {}),
            'gramineas': ('django.db.models.fields.FloatField', [], {}),
            'hoja_ancha': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"})
        },
        u'ficha_granos_basicos.parametrossuelo': {
            'Meta': {'object_name': 'ParametrosSuelo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_critico': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nivel_suficiencia': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'parametro': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'ficha_granos_basicos.plagasfrijol': {
            'Meta': {'object_name': 'PlagasFrijol'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'plaga': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Especies']"}),
            'porcentaje_dano_1': ('django.db.models.fields.FloatField', [], {}),
            'porcentaje_dano_2': ('django.db.models.fields.FloatField', [], {}),
            'porcentaje_dano_3': ('django.db.models.fields.FloatField', [], {}),
            'porcentaje_dano_4': ('django.db.models.fields.FloatField', [], {}),
            'porcentaje_dano_5': ('django.db.models.fields.FloatField', [], {}),
            'presencia_1': ('django.db.models.fields.FloatField', [], {}),
            'presencia_2': ('django.db.models.fields.FloatField', [], {}),
            'presencia_3': ('django.db.models.fields.FloatField', [], {}),
            'presencia_4': ('django.db.models.fields.FloatField', [], {}),
            'presencia_5': ('django.db.models.fields.FloatField', [], {}),
            'promedio_dano': ('django.db.models.fields.FloatField', [], {}),
            'promedio_presencia': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.plagasmaiz': {
            'Meta': {'object_name': 'PlagasMaiz'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'plaga': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Especies']"}),
            'porcentaje_dano_1': ('django.db.models.fields.FloatField', [], {}),
            'porcentaje_dano_2': ('django.db.models.fields.FloatField', [], {}),
            'porcentaje_dano_3': ('django.db.models.fields.FloatField', [], {}),
            'porcentaje_dano_4': ('django.db.models.fields.FloatField', [], {}),
            'porcentaje_dano_5': ('django.db.models.fields.FloatField', [], {}),
            'presencia_1': ('django.db.models.fields.FloatField', [], {}),
            'presencia_2': ('django.db.models.fields.FloatField', [], {}),
            'presencia_3': ('django.db.models.fields.FloatField', [], {}),
            'presencia_4': ('django.db.models.fields.FloatField', [], {}),
            'presencia_5': ('django.db.models.fields.FloatField', [], {}),
            'promedio_dano': ('django.db.models.fields.FloatField', [], {}),
            'promedio_presencia': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.poblacionfrijol': {
            'Meta': {'object_name': 'PoblacionFrijol'},
            'distancia_frijol': ('django.db.models.fields.FloatField', [], {}),
            'est1': ('django.db.models.fields.IntegerField', [], {}),
            'est2': ('django.db.models.fields.IntegerField', [], {}),
            'est3': ('django.db.models.fields.IntegerField', [], {}),
            'est4': ('django.db.models.fields.IntegerField', [], {}),
            'est5': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metros_lineales': ('django.db.models.fields.FloatField', [], {}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'numero_surcos': ('django.db.models.fields.FloatField', [], {}),
            'poblacion': ('django.db.models.fields.FloatField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.poblacionmaiz': {
            'Meta': {'object_name': 'PoblacionMaiz'},
            'distancia_maiz': ('django.db.models.fields.FloatField', [], {}),
            'est1': ('django.db.models.fields.IntegerField', [], {}),
            'est2': ('django.db.models.fields.IntegerField', [], {}),
            'est3': ('django.db.models.fields.IntegerField', [], {}),
            'est4': ('django.db.models.fields.IntegerField', [], {}),
            'est5': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metros_lineales': ('django.db.models.fields.FloatField', [], {}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'numero_surcos': ('django.db.models.fields.FloatField', [], {}),
            'poblacion': ('django.db.models.fields.FloatField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.procedenciasemilla': {
            'Meta': {'object_name': 'ProcedenciaSemilla'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'procedencia': ('django.db.models.fields.IntegerField', [], {}),
            'rubro': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.productos': {
            'Meta': {'object_name': 'Productos'},
            'categoria': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_comercial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'presentacion': ('django.db.models.fields.IntegerField', [], {}),
            'principio_activo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ficha_granos_basicos.pruebagerminacion': {
            'Meta': {'object_name': 'PruebaGerminacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'porcentaje': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {}),
            'rubro': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.recursossiembra': {
            'Meta': {'object_name': 'RecursosSiembra'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {}),
            'rubro': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.semillas': {
            'Meta': {'object_name': 'Semillas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'nombre_frijol': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombre_maiz': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semilla_frijol': ('django.db.models.fields.IntegerField', [], {}),
            'semilla_maiz': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.sobrecosecha': {
            'Meta': {'object_name': 'SobreCosecha'},
            'almacenamiento': ('django.db.models.fields.FloatField', [], {}),
            'cosecha': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'precio_mercado': ('django.db.models.fields.FloatField', [], {}),
            'rubro': ('django.db.models.fields.IntegerField', [], {}),
            'venta': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.suelo': {
            'Meta': {'object_name': 'Suelo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'parametro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.ParametrosSuelo']"}),
            'resultado': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.tabladecisiones': {
            'Meta': {'object_name': 'TablaDecisiones'},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'decision': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'porque': ('django.db.models.fields.TextField', [], {}),
            'seleccion': ('django.db.models.fields.IntegerField', [], {}),
            'toma_deciciones': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.TomaDecisiones']"}),
            'visita': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.tablagastos': {
            'Meta': {'object_name': 'TablaGastos'},
            'actividad': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'dias_persona': ('django.db.models.fields.IntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'gastos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Gastos']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.tablainsumos': {
            'Meta': {'object_name': 'TablaInsumos'},
            'bombas': ('django.db.models.fields.FloatField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insumos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Insumos']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Productos']"}),
            'unidades': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.tablamalezas': {
            'Meta': {'object_name': 'TablaMalezas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maleza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.TiposMalezas']"}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"})
        },
        u'ficha_granos_basicos.tiposmalezas': {
            'Meta': {'object_name': 'TiposMalezas'},
            'categoria': ('django.db.models.fields.IntegerField', [], {}),
            'ciclo': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_cientifico': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombre_popular': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ficha_granos_basicos.tomadecisiones': {
            'Meta': {'object_name': 'TomaDecisiones'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"})
        },
        u'ficha_granos_basicos.tratamientosemilla': {
            'Meta': {'object_name': 'TratamientoSemilla'},
            'dosis': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preparacion': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'ficha_granos_basicos.vigorfrijol': {
            'Meta': {'object_name': 'VigorFrijol'},
            'est1': ('django.db.models.fields.IntegerField', [], {}),
            'est2': ('django.db.models.fields.IntegerField', [], {}),
            'est3': ('django.db.models.fields.IntegerField', [], {}),
            'est4': ('django.db.models.fields.IntegerField', [], {}),
            'est5': ('django.db.models.fields.IntegerField', [], {}),
            'estimado_plantas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'porcentaje': ('django.db.models.fields.FloatField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {})
        },
        u'ficha_granos_basicos.vigormaiz': {
            'Meta': {'object_name': 'VigorMaiz'},
            'est1': ('django.db.models.fields.IntegerField', [], {}),
            'est2': ('django.db.models.fields.IntegerField', [], {}),
            'est3': ('django.db.models.fields.IntegerField', [], {}),
            'est4': ('django.db.models.fields.IntegerField', [], {}),
            'est5': ('django.db.models.fields.IntegerField', [], {}),
            'estimado_plantas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitoreo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'porcentaje': ('django.db.models.fields.FloatField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {})
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

    complete_apps = ['ficha_granos_basicos']