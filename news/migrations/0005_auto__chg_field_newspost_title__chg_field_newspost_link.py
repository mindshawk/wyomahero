# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'NewsPost.title'
        db.alter_column(u'news_newspost', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'NewsPost.link'
        db.alter_column(u'news_newspost', 'link', self.gf('django.db.models.fields.URLField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'NewsPost.title'
        db.alter_column(u'news_newspost', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'NewsPost.link'
        db.alter_column(u'news_newspost', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'news.newspost': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'NewsPost'},
            'blurb': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['news']