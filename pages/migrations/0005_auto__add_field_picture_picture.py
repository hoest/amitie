# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Picture.picture'
        db.add_column('pages_picture', 'picture',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Picture.picture'
        db.delete_column('pages_picture', 'picture')


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
        },
        'pages.picture': {
            'Meta': {'object_name': 'Picture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Page']"}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['pages']