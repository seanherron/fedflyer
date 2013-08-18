# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'cities_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('iata_code', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('icao_code', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('airport_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'cities', ['City'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'cities_city')


    models = {
        u'cities.city': {
            'Meta': {'object_name': 'City'},
            'airport_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'iata_code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'icao_code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['cities']