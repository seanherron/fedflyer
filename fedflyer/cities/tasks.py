from celery import task
from django.db.transaction import commit_on_success

import unicodecsv

from cities.models import City


@task()
@commit_on_success
def import_airports(path):
    with open(path, 'rb') as file:
        cities = unicodecsv.reader(file, delimiter=',')
        for row in cities:
            city = City()
            city.name = row[2]
            city.country = row[3]
            city.iata_code = row[4]
            city.icao_code = row[5]
            city.latitude = row[6]
            city.longitude = row[7]
            city.airport_name = row[1]
            city.save()
    