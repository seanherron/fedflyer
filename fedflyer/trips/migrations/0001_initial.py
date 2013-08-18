# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trip'
        db.create_table(u'trips_trip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities.City'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'trips', ['Trip'])

        # Adding model 'Destination'
        db.create_table(u'trips_destination', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trips.Trip'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities.City'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('transportation_type', self.gf('django.db.models.fields.CharField')(default='air', max_length=150)),
            ('transportation_cost', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'trips', ['Destination'])

        # Adding model 'Expenses'
        db.create_table(u'trips_expenses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trips.Destination'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'trips', ['Expenses'])


    def backwards(self, orm):
        # Deleting model 'Trip'
        db.delete_table(u'trips_trip')

        # Deleting model 'Destination'
        db.delete_table(u'trips_destination')

        # Deleting model 'Expenses'
        db.delete_table(u'trips_expenses')


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
        },
        u'trips.destination': {
            'Meta': {'object_name': 'Destination'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.City']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'transportation_cost': ('django.db.models.fields.IntegerField', [], {}),
            'transportation_type': ('django.db.models.fields.CharField', [], {'default': "'air'", 'max_length': '150'}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trips.Trip']"})
        },
        u'trips.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trips.Destination']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'trips.trip': {
            'Meta': {'object_name': 'Trip'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.City']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['trips']