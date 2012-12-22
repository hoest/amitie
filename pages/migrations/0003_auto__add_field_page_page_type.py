# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.page_type'
        db.add_column('pages_page', 'page_type',
                      self.gf('django.db.models.fields.CharField')(default='all', max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Page.page_type'
        db.delete_column('pages_page', 'page_type')


    models = {
        'pages.page': {
            'Meta': {'object_name': 'Page'},
            'alias': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_type': ('django.db.models.fields.CharField', [], {'default': "'all'", 'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['pages']