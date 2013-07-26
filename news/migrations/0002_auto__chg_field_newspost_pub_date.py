# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'NewsPost.pub_date'
        db.alter_column('news_newspost', 'pub_date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'NewsPost.pub_date'
        db.alter_column('news_newspost', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        'news.newspost': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'NewsPost'},
            'blurb': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['news']