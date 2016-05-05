# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Visitas'
        db.create_table(u'ficha_granos_basicos_visitas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha_granos_basicos.Monitoreo'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('visita', self.gf('django.db.models.fields.IntegerField')()),
            ('areas', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=17)),
        ))
        db.send_create_signal(u'ficha_granos_basicos', ['Visitas'])

        # Deleting field 'EstimadoCosechaMaiz2.monitoreo'
        db.delete_column(u'ficha_granos_basicos_estimadocosechamaiz2', 'monitoreo_id')

        # Adding field 'EstimadoCosechaMaiz2.visita'
        db.add_column(u'ficha_granos_basicos_estimadocosechamaiz2', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)


        # Changing field 'TiposMalezas.nombre_cientifico'
        db.alter_column(u'ficha_granos_basicos_tiposmalezas', 'nombre_cientifico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
        # Deleting field 'GranosPlanta.monitoreo'
        db.delete_column(u'ficha_granos_basicos_granosplanta', 'monitoreo_id')

        # Adding field 'GranosPlanta.visita'
        db.add_column(u'ficha_granos_basicos_granosplanta', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'MonitoreoMalezas.monitoreo'
        db.delete_column(u'ficha_granos_basicos_monitoreomalezas', 'monitoreo_id')

        # Adding field 'MonitoreoMalezas.visita'
        db.add_column(u'ficha_granos_basicos_monitoreomalezas', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'VigorFrijol.monitoreo'
        db.delete_column(u'ficha_granos_basicos_vigorfrijol', 'monitoreo_id')

        # Adding field 'VigorFrijol.visita'
        db.add_column(u'ficha_granos_basicos_vigorfrijol', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'Macrofauna.monitoreo'
        db.delete_column(u'ficha_granos_basicos_macrofauna', 'monitoreo_id')

        # Adding field 'Macrofauna.visita'
        db.add_column(u'ficha_granos_basicos_macrofauna', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'PoblacionFrijol.monitoreo'
        db.delete_column(u'ficha_granos_basicos_poblacionfrijol', 'monitoreo_id')

        # Adding field 'PoblacionFrijol.visita'
        db.add_column(u'ficha_granos_basicos_poblacionfrijol', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'Suelo.monitoreo'
        db.delete_column(u'ficha_granos_basicos_suelo', 'monitoreo_id')

        # Adding field 'Suelo.visita'
        db.add_column(u'ficha_granos_basicos_suelo', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'EnfermedadesMaiz.monitoreo'
        db.delete_column(u'ficha_granos_basicos_enfermedadesmaiz', 'monitoreo_id')

        # Adding field 'EnfermedadesMaiz.visita'
        db.add_column(u'ficha_granos_basicos_enfermedadesmaiz', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'EnfermedadesFrijol.monitoreo'
        db.delete_column(u'ficha_granos_basicos_enfermedadesfrijol', 'monitoreo_id')

        # Adding field 'EnfermedadesFrijol.visita'
        db.add_column(u'ficha_granos_basicos_enfermedadesfrijol', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'SobreCosecha.monitoreo'
        db.delete_column(u'ficha_granos_basicos_sobrecosecha', 'monitoreo_id')

        # Adding field 'SobreCosecha.visita'
        db.add_column(u'ficha_granos_basicos_sobrecosecha', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'PoblacionMaiz.monitoreo'
        db.delete_column(u'ficha_granos_basicos_poblacionmaiz', 'monitoreo_id')

        # Adding field 'PoblacionMaiz.visita'
        db.add_column(u'ficha_granos_basicos_poblacionmaiz', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'TablaMalezas.monitoreo'
        db.delete_column(u'ficha_granos_basicos_tablamalezas', 'monitoreo_id')

        # Adding field 'TablaMalezas.visita'
        db.add_column(u'ficha_granos_basicos_tablamalezas', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'PruebaGerminacion.monitoreo'
        db.delete_column(u'ficha_granos_basicos_pruebagerminacion', 'monitoreo_id')

        # Adding field 'PruebaGerminacion.visita'
        db.add_column(u'ficha_granos_basicos_pruebagerminacion', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'PlagasFrijol.monitoreo'
        db.delete_column(u'ficha_granos_basicos_plagasfrijol', 'monitoreo_id')

        # Adding field 'PlagasFrijol.visita'
        db.add_column(u'ficha_granos_basicos_plagasfrijol', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'Semillas.semilla_frijol'
        db.delete_column(u'ficha_granos_basicos_semillas', 'semilla_frijol')

        # Deleting field 'Semillas.semilla_maiz'
        db.delete_column(u'ficha_granos_basicos_semillas', 'semilla_maiz')

        # Deleting field 'Semillas.nombre_maiz'
        db.delete_column(u'ficha_granos_basicos_semillas', 'nombre_maiz')

        # Deleting field 'Semillas.monitoreo'
        db.delete_column(u'ficha_granos_basicos_semillas', 'monitoreo_id')

        # Deleting field 'Semillas.nombre_frijol'
        db.delete_column(u'ficha_granos_basicos_semillas', 'nombre_frijol')

        # Adding field 'Semillas.rubro'
        db.add_column(u'ficha_granos_basicos_semillas', 'rubro',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'Semillas.tipo_semilla'
        db.add_column(u'ficha_granos_basicos_semillas', 'tipo_semilla',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'Semillas.nombre_semilla'
        db.add_column(u'ficha_granos_basicos_semillas', 'nombre_semilla',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Semillas.visita'
        db.add_column(u'ficha_granos_basicos_semillas', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'DistribucionPendiente.ondulado'
        db.delete_column(u'ficha_granos_basicos_distribucionpendiente', 'ondulado')

        # Deleting field 'Monitoreo.fecha'
        db.delete_column(u'ficha_granos_basicos_monitoreo', 'fecha')

        # Deleting field 'Monitoreo.visita'
        db.delete_column(u'ficha_granos_basicos_monitoreo', 'visita')

        # Deleting field 'Monitoreo.areas'
        db.delete_column(u'ficha_granos_basicos_monitoreo', 'areas')

        # Deleting field 'CuradoSemilla.monitoreo'
        db.delete_column(u'ficha_granos_basicos_curadosemilla', 'monitoreo_id')

        # Adding field 'CuradoSemilla.visita'
        db.add_column(u'ficha_granos_basicos_curadosemilla', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'PlagasMaiz.monitoreo'
        db.delete_column(u'ficha_granos_basicos_plagasmaiz', 'monitoreo_id')

        # Adding field 'PlagasMaiz.visita'
        db.add_column(u'ficha_granos_basicos_plagasmaiz', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'EstimadoCosechaFrijol.monitoreo'
        db.delete_column(u'ficha_granos_basicos_estimadocosechafrijol', 'monitoreo_id')

        # Adding field 'EstimadoCosechaFrijol.visita'
        db.add_column(u'ficha_granos_basicos_estimadocosechafrijol', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Adding field 'DatosMonitoreo.area_siembra'
        db.add_column(u'ficha_granos_basicos_datosmonitoreo', 'area_siembra',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)


        # Changing field 'DatosMonitoreo.fecha_siembra'
        db.alter_column(u'ficha_granos_basicos_datosmonitoreo', 'fecha_siembra', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'DatosMonitoreo.fecha_cosecha'
        db.alter_column(u'ficha_granos_basicos_datosmonitoreo', 'fecha_cosecha', self.gf('django.db.models.fields.DateField')(null=True))
        # Deleting field 'ProcedenciaSemilla.monitoreo'
        db.delete_column(u'ficha_granos_basicos_procedenciasemilla', 'monitoreo_id')

        # Adding field 'ProcedenciaSemilla.visita'
        db.add_column(u'ficha_granos_basicos_procedenciasemilla', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'VigorMaiz.monitoreo'
        db.delete_column(u'ficha_granos_basicos_vigormaiz', 'monitoreo_id')

        # Adding field 'VigorMaiz.visita'
        db.add_column(u'ficha_granos_basicos_vigormaiz', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)

        # Deleting field 'EstimadoCosechaMaiz.monitoreo'
        db.delete_column(u'ficha_granos_basicos_estimadocosechamaiz', 'monitoreo_id')

        # Adding field 'EstimadoCosechaMaiz.visita'
        db.add_column(u'ficha_granos_basicos_estimadocosechamaiz', 'visita',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Visitas']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Visitas'
        db.delete_table(u'ficha_granos_basicos_visitas')

        # Adding field 'EstimadoCosechaMaiz2.monitoreo'
        db.add_column(u'ficha_granos_basicos_estimadocosechamaiz2', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'EstimadoCosechaMaiz2.visita'
        db.delete_column(u'ficha_granos_basicos_estimadocosechamaiz2', 'visita_id')


        # Changing field 'TiposMalezas.nombre_cientifico'
        db.alter_column(u'ficha_granos_basicos_tiposmalezas', 'nombre_cientifico', self.gf('django.db.models.fields.CharField')(default=2, max_length=100))
        # Adding field 'GranosPlanta.monitoreo'
        db.add_column(u'ficha_granos_basicos_granosplanta', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'GranosPlanta.visita'
        db.delete_column(u'ficha_granos_basicos_granosplanta', 'visita_id')

        # Adding field 'MonitoreoMalezas.monitoreo'
        db.add_column(u'ficha_granos_basicos_monitoreomalezas', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'MonitoreoMalezas.visita'
        db.delete_column(u'ficha_granos_basicos_monitoreomalezas', 'visita_id')

        # Adding field 'VigorFrijol.monitoreo'
        db.add_column(u'ficha_granos_basicos_vigorfrijol', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'VigorFrijol.visita'
        db.delete_column(u'ficha_granos_basicos_vigorfrijol', 'visita_id')

        # Adding field 'Macrofauna.monitoreo'
        db.add_column(u'ficha_granos_basicos_macrofauna', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'Macrofauna.visita'
        db.delete_column(u'ficha_granos_basicos_macrofauna', 'visita_id')

        # Adding field 'PoblacionFrijol.monitoreo'
        db.add_column(u'ficha_granos_basicos_poblacionfrijol', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'PoblacionFrijol.visita'
        db.delete_column(u'ficha_granos_basicos_poblacionfrijol', 'visita_id')

        # Adding field 'Suelo.monitoreo'
        db.add_column(u'ficha_granos_basicos_suelo', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'Suelo.visita'
        db.delete_column(u'ficha_granos_basicos_suelo', 'visita_id')

        # Adding field 'EnfermedadesMaiz.monitoreo'
        db.add_column(u'ficha_granos_basicos_enfermedadesmaiz', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'EnfermedadesMaiz.visita'
        db.delete_column(u'ficha_granos_basicos_enfermedadesmaiz', 'visita_id')

        # Adding field 'EnfermedadesFrijol.monitoreo'
        db.add_column(u'ficha_granos_basicos_enfermedadesfrijol', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'EnfermedadesFrijol.visita'
        db.delete_column(u'ficha_granos_basicos_enfermedadesfrijol', 'visita_id')

        # Adding field 'SobreCosecha.monitoreo'
        db.add_column(u'ficha_granos_basicos_sobrecosecha', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'SobreCosecha.visita'
        db.delete_column(u'ficha_granos_basicos_sobrecosecha', 'visita_id')

        # Adding field 'PoblacionMaiz.monitoreo'
        db.add_column(u'ficha_granos_basicos_poblacionmaiz', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'PoblacionMaiz.visita'
        db.delete_column(u'ficha_granos_basicos_poblacionmaiz', 'visita_id')

        # Adding field 'TablaMalezas.monitoreo'
        db.add_column(u'ficha_granos_basicos_tablamalezas', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'TablaMalezas.visita'
        db.delete_column(u'ficha_granos_basicos_tablamalezas', 'visita_id')

        # Adding field 'PruebaGerminacion.monitoreo'
        db.add_column(u'ficha_granos_basicos_pruebagerminacion', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'PruebaGerminacion.visita'
        db.delete_column(u'ficha_granos_basicos_pruebagerminacion', 'visita_id')

        # Adding field 'PlagasFrijol.monitoreo'
        db.add_column(u'ficha_granos_basicos_plagasfrijol', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'PlagasFrijol.visita'
        db.delete_column(u'ficha_granos_basicos_plagasfrijol', 'visita_id')

        # Adding field 'Semillas.semilla_frijol'
        db.add_column(u'ficha_granos_basicos_semillas', 'semilla_frijol',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'Semillas.semilla_maiz'
        db.add_column(u'ficha_granos_basicos_semillas', 'semilla_maiz',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'Semillas.nombre_maiz'
        db.add_column(u'ficha_granos_basicos_semillas', 'nombre_maiz',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Semillas.monitoreo'
        db.add_column(u'ficha_granos_basicos_semillas', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Adding field 'Semillas.nombre_frijol'
        db.add_column(u'ficha_granos_basicos_semillas', 'nombre_frijol',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=100),
                      keep_default=False)

        # Deleting field 'Semillas.rubro'
        db.delete_column(u'ficha_granos_basicos_semillas', 'rubro')

        # Deleting field 'Semillas.tipo_semilla'
        db.delete_column(u'ficha_granos_basicos_semillas', 'tipo_semilla')

        # Deleting field 'Semillas.nombre_semilla'
        db.delete_column(u'ficha_granos_basicos_semillas', 'nombre_semilla')

        # Deleting field 'Semillas.visita'
        db.delete_column(u'ficha_granos_basicos_semillas', 'visita_id')

        # Adding field 'DistribucionPendiente.ondulado'
        db.add_column(u'ficha_granos_basicos_distribucionpendiente', 'ondulado',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Monitoreo.fecha'
        db.add_column(u'ficha_granos_basicos_monitoreo', 'fecha',
                      self.gf('django.db.models.fields.DateField')(default=2),
                      keep_default=False)

        # Adding field 'Monitoreo.visita'
        db.add_column(u'ficha_granos_basicos_monitoreo', 'visita',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'Monitoreo.areas'
        db.add_column(u'ficha_granos_basicos_monitoreo', 'areas',
                      self.gf('multiselectfield.db.fields.MultiSelectField')(default=2, max_length=17),
                      keep_default=False)

        # Adding field 'CuradoSemilla.monitoreo'
        db.add_column(u'ficha_granos_basicos_curadosemilla', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'CuradoSemilla.visita'
        db.delete_column(u'ficha_granos_basicos_curadosemilla', 'visita_id')

        # Adding field 'PlagasMaiz.monitoreo'
        db.add_column(u'ficha_granos_basicos_plagasmaiz', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'PlagasMaiz.visita'
        db.delete_column(u'ficha_granos_basicos_plagasmaiz', 'visita_id')

        # Adding field 'EstimadoCosechaFrijol.monitoreo'
        db.add_column(u'ficha_granos_basicos_estimadocosechafrijol', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'EstimadoCosechaFrijol.visita'
        db.delete_column(u'ficha_granos_basicos_estimadocosechafrijol', 'visita_id')

        # Deleting field 'DatosMonitoreo.area_siembra'
        db.delete_column(u'ficha_granos_basicos_datosmonitoreo', 'area_siembra')


        # Changing field 'DatosMonitoreo.fecha_siembra'
        db.alter_column(u'ficha_granos_basicos_datosmonitoreo', 'fecha_siembra', self.gf('django.db.models.fields.DateField')(default=2))

        # Changing field 'DatosMonitoreo.fecha_cosecha'
        db.alter_column(u'ficha_granos_basicos_datosmonitoreo', 'fecha_cosecha', self.gf('django.db.models.fields.DateField')(default=2))
        # Adding field 'ProcedenciaSemilla.monitoreo'
        db.add_column(u'ficha_granos_basicos_procedenciasemilla', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'ProcedenciaSemilla.visita'
        db.delete_column(u'ficha_granos_basicos_procedenciasemilla', 'visita_id')

        # Adding field 'VigorMaiz.monitoreo'
        db.add_column(u'ficha_granos_basicos_vigormaiz', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'VigorMaiz.visita'
        db.delete_column(u'ficha_granos_basicos_vigormaiz', 'visita_id')

        # Adding field 'EstimadoCosechaMaiz.monitoreo'
        db.add_column(u'ficha_granos_basicos_estimadocosechamaiz', 'monitoreo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ficha_granos_basicos.Monitoreo']),
                      keep_default=False)

        # Deleting field 'EstimadoCosechaMaiz.visita'
        db.delete_column(u'ficha_granos_basicos_estimadocosechamaiz', 'visita_id')


    models = {
        u'ficha_granos_basicos.curadosemilla': {
            'Meta': {'object_name': 'CuradoSemilla'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tratamiento': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ficha_granos_basicos.TratamientoSemilla']", 'symmetrical': 'False'}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.datosmonitoreo': {
            'Meta': {'object_name': 'DatosMonitoreo'},
            'area_siembra': ('django.db.models.fields.FloatField', [], {}),
            'ciclo_productivo': ('django.db.models.fields.IntegerField', [], {}),
            'cultivo': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_cosecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_siembra': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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
            'plano': ('django.db.models.fields.FloatField', [], {}),
            'seleccion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ficha_granos_basicos.enfermedadesfrijol': {
            'Meta': {'object_name': 'EnfermedadesFrijol'},
            'enfermedad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Especies']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'planta_1': ('django.db.models.fields.IntegerField', [], {}),
            'planta_2': ('django.db.models.fields.IntegerField', [], {}),
            'planta_3': ('django.db.models.fields.IntegerField', [], {}),
            'planta_4': ('django.db.models.fields.IntegerField', [], {}),
            'planta_5': ('django.db.models.fields.IntegerField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.enfermedadesmaiz': {
            'Meta': {'object_name': 'EnfermedadesMaiz'},
            'enfermedad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Especies']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'planta_1': ('django.db.models.fields.IntegerField', [], {}),
            'planta_2': ('django.db.models.fields.IntegerField', [], {}),
            'planta_3': ('django.db.models.fields.IntegerField', [], {}),
            'planta_4': ('django.db.models.fields.IntegerField', [], {}),
            'planta_5': ('django.db.models.fields.IntegerField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'planta_1': ('django.db.models.fields.IntegerField', [], {}),
            'planta_2': ('django.db.models.fields.IntegerField', [], {}),
            'planta_3': ('django.db.models.fields.IntegerField', [], {}),
            'planta_4': ('django.db.models.fields.IntegerField', [], {}),
            'planta_5': ('django.db.models.fields.IntegerField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.estimadocosechamaiz2': {
            'Meta': {'object_name': 'EstimadoCosechaMaiz2'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mazorca': ('django.db.models.fields.IntegerField', [], {}),
            'peso': ('django.db.models.fields.FloatField', [], {}),
            'peso_promedio': ('django.db.models.fields.IntegerField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.monitoreo': {
            'Meta': {'object_name': 'Monitoreo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Persona']"})
        },
        u'ficha_granos_basicos.monitoreomalezas': {
            'Meta': {'object_name': 'MonitoreoMalezas'},
            'ciperaceas': ('django.db.models.fields.FloatField', [], {}),
            'cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'cobertura_total': ('django.db.models.fields.FloatField', [], {}),
            'gramineas': ('django.db.models.fields.FloatField', [], {}),
            'hoja_ancha': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'promedio_presencia': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.plagasmaiz': {
            'Meta': {'object_name': 'PlagasMaiz'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'promedio_presencia': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'numero_surcos': ('django.db.models.fields.FloatField', [], {}),
            'poblacion': ('django.db.models.fields.FloatField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'numero_surcos': ('django.db.models.fields.FloatField', [], {}),
            'poblacion': ('django.db.models.fields.FloatField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.procedenciasemilla': {
            'Meta': {'object_name': 'ProcedenciaSemilla'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'procedencia': ('django.db.models.fields.IntegerField', [], {}),
            'rubro': ('django.db.models.fields.IntegerField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'porcentaje': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {}),
            'rubro': ('django.db.models.fields.IntegerField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'nombre_semilla': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rubro': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_semilla': ('django.db.models.fields.IntegerField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.sobrecosecha': {
            'Meta': {'object_name': 'SobreCosecha'},
            'almacenamiento': ('django.db.models.fields.FloatField', [], {}),
            'cosecha': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_mercado': ('django.db.models.fields.FloatField', [], {}),
            'rubro': ('django.db.models.fields.IntegerField', [], {}),
            'venta': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.suelo': {
            'Meta': {'object_name': 'Suelo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parametro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.ParametrosSuelo']"}),
            'resultado': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.tiposmalezas': {
            'Meta': {'object_name': 'TiposMalezas'},
            'categoria': ('django.db.models.fields.IntegerField', [], {}),
            'ciclo': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_cientifico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'porcentaje': ('django.db.models.fields.FloatField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
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
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'porcentaje': ('django.db.models.fields.FloatField', [], {}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Visitas']"})
        },
        u'ficha_granos_basicos.visitas': {
            'Meta': {'object_name': 'Visitas'},
            'areas': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '17'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ficha_granos_basicos.Monitoreo']"}),
            'visita': ('django.db.models.fields.IntegerField', [], {})
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