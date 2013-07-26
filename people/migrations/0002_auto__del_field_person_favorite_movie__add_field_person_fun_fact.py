# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Person.favorite_movie'
        db.delete_column('people_person', 'favorite_movie')

        # Adding field 'Person.fun_fact'
        db.add_column('people_person', 'fun_fact',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 7, 22, 0, 0), max_length=80),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Person.favorite_movie'
        raise RuntimeError("Cannot reverse this migration. 'Person.favorite_movie' and its values cannot be restored.")
        # Deleting field 'Person.fun_fact'
        db.delete_column('people_person', 'fun_fact')


    models = {
        'people.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'fun_fact': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['people']