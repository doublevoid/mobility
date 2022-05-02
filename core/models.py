from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    language = models.CharField(max_length=2)
    currency = models.CharField(max_length=3)  # based on currency codes max length


class Location(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    geojson = models.JSONField()
    # although it will probably be contained within the geojson, it is better to put both lat/lng on
    # columns, so it will be faster to filter when we want to get every location that has the
    # specific lat/lng we want
    lat = models.FloatField()
    lng = models.FloatField()
    provider = models.ForeignKey(Provider, models.CASCADE)
