# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Imagen'
        db.create_table(u'foros_imagen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('nombre_img', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('foto', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('tags_img', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal(u'foros', ['Imagen'])

        # Adding model 'Documentos'
        db.create_table(u'foros_documentos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('nombre_doc', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tags_doc', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal(u'foros', ['Documentos'])

        # Adding model 'Videos'
        db.create_table(u'foros_videos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('nombre_video', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('tags_vid', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal(u'foros', ['Videos'])

        # Adding model 'Audios'
        db.create_table(u'foros_audios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('nombre_audio', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tags_aud', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal(u'foros', ['Audios'])

        # Adding model 'Foros'
        db.create_table(u'foros_foros', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('creacion', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 1, 28, 0, 0))),
            ('apertura', self.gf('django.db.models.fields.DateField')()),
            ('cierre', self.gf('django.db.models.fields.DateField')()),
            ('fecha_skype', self.gf('django.db.models.fields.DateField')()),
            ('memoria', self.gf('django.db.models.fields.DateField')()),
            ('contenido', self.gf('ckeditor.fields.RichTextField')()),
            ('contraparte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'foros', ['Foros'])

        # Adding model 'Aportes'
        db.create_table(u'foros_aportes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foros.Foros'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 1, 28, 0, 0))),
            ('contenido', self.gf('ckeditor.fields.RichTextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'foros', ['Aportes'])

        # Adding model 'Comentarios'
        db.create_table(u'foros_comentarios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 1, 28, 0, 0))),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('comentario', self.gf('ckeditor.fields.RichTextField')()),
            ('aporte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foros.Aportes'])),
        ))
        db.send_create_signal(u'foros', ['Comentarios'])


    def backwards(self, orm):
        # Deleting model 'Imagen'
        db.delete_table(u'foros_imagen')

        # Deleting model 'Documentos'
        db.delete_table(u'foros_documentos')

        # Deleting model 'Videos'
        db.delete_table(u'foros_videos')

        # Deleting model 'Audios'
        db.delete_table(u'foros_audios')

        # Deleting model 'Foros'
        db.delete_table(u'foros_foros')

        # Deleting model 'Aportes'
        db.delete_table(u'foros_aportes')

        # Deleting model 'Comentarios'
        db.delete_table(u'foros_comentarios')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'foros.aportes': {
            'Meta': {'object_name': 'Aportes'},
            'contenido': ('ckeditor.fields.RichTextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 1, 28, 0, 0)'}),
            'foro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foros.Foros']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'foros.audios': {
            'Meta': {'object_name': 'Audios'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_audio': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tags_aud': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        u'foros.comentarios': {
            'Meta': {'object_name': 'Comentarios'},
            'aporte': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foros.Aportes']"}),
            'comentario': ('ckeditor.fields.RichTextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 1, 28, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'foros.documentos': {
            'Meta': {'object_name': 'Documentos'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_doc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tags_doc': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        u'foros.foros': {
            'Meta': {'ordering': "('-creacion', 'id')", 'object_name': 'Foros'},
            'apertura': ('django.db.models.fields.DateField', [], {}),
            'cierre': ('django.db.models.fields.DateField', [], {}),
            'contenido': ('ckeditor.fields.RichTextField', [], {}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'creacion': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 1, 28, 0, 0)'}),
            'fecha_skype': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memoria': ('django.db.models.fields.DateField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'foros.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_img': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tags_img': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        u'foros.videos': {
            'Meta': {'object_name': 'Videos'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_video': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tags_vid': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['foros']