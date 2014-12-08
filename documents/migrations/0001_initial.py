# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DocumentAuthor'
        db.create_table(u'documents_documentauthor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'documents', ['DocumentAuthor'])

        # Adding model 'Document'
        db.create_table(u'documents_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doc_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='author_of', to=orm['documents.DocumentAuthor'])),
            ('file', self.gf('filebrowser.fields.FileBrowseField')(max_length=255)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('uploaded_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('observed_item', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('uploaded_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='uploader_of', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'documents', ['Document'])

        # Adding model 'ObservedPerson'
        db.create_table(u'documents_observedperson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(related_name='observed_persons', to=orm['documents.Document'])),
        ))
        db.send_create_signal(u'documents', ['ObservedPerson'])


    def backwards(self, orm):
        # Deleting model 'DocumentAuthor'
        db.delete_table(u'documents_documentauthor')

        # Deleting model 'Document'
        db.delete_table(u'documents_document')

        # Deleting model 'ObservedPerson'
        db.delete_table(u'documents_observedperson')


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
        u'documents.document': {
            'Meta': {'object_name': 'Document'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'author_of'", 'to': u"orm['documents.DocumentAuthor']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doc_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'file': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observed_item': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'uploaded_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uploader_of'", 'to': u"orm['auth.User']"}),
            'uploaded_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'documents.documentauthor': {
            'Meta': {'object_name': 'DocumentAuthor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'documents.observedperson': {
            'Meta': {'object_name': 'ObservedPerson'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'observed_persons'", 'to': u"orm['documents.Document']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['documents']