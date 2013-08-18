from django.db import models
from django.utils.translation import ugettext as _

class City(models.Model):
    name = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    iata_code = models.CharField(max_length=4, blank=True)
    icao_code = models.CharField(max_length=4, blank=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    airport_name = models.CharField(max_length=200, blank=True)