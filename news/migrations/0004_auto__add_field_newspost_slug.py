# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewsPost.slug'
        db.add_column(u'news_newspost', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='slug', unique=True, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewsPost.slug'
        db.delete_column(u'news_newspost', 'slug')


    models = {
        u'news.newspost': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'NewsPost'},
            'blurb': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['news']