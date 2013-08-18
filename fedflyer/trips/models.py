from django.db import models
from django.utils.translation import ugettext as _

from model_utils import Choices

from cities.models import City


class Trip(models.Model):
    title = models.CharField(max_length=200, blank=True)
    origin = models.ForeignKey(City)
    notes = models.TextField(blank=True)
    
    def __unicode__(self):
        return u"%s - %s" % (self.origin)

class Destination(models.Model):
    trip = models.ForeignKey(Trip)
    city = models.ForeignKey(City)
    start_date = models.DateField()
    end_date = models.DateField()
    transportation_type_choices = Choices(('air', _('Air')), ('bus', _('Bus')), ('rail', _('Rail')), ('personal_vehicle', _('Personal Vehicle')))
    transportation_type = models.CharField(choices=transportation_type_choices, default=transportation_type_choices.air, max_length=150)
    transportation_cost = models.IntegerField()
    
class Expense(models.Model):
    trip = models.ForeignKey(Trip)
    destination = models.ForeignKey(Destination)
    title = models.CharField(max_length=200)
    amount = models.IntegerField()
    
