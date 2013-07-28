# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'core_contact')


    def backwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'core_contact', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['Contact'])


    models = {
        
    }

    complete_apps = ['core']