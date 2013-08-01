# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'videos_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('embed_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'videos', ['Video'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'videos_video')


    models = {
        u'videos.video': {
            'Meta': {'ordering': "('modified',)", 'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['videos']