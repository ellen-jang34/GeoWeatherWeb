from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
#google map
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
DEFAULT_LOCATION_POINT = Point(-104.9903, 39.7392)
#dailyweather
from pyowm.utils.geo import Polygon

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#google map
class House(models.Model):
    location = models.PointField(help_text="Use map widget for point the house location")
    name = models.CharField(max_length=255)
    location_has_default = models.PointField(default=DEFAULT_LOCATION_POINT)

    def __str__(self):
        return self.name


class Neighbour(models.Model):
    neighbour_of_house = models.ForeignKey(House, on_delete=models.CASCADE)
    location = models.PointField(null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.address

class City(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField(help_text="Use map widget for point the house location")

    def __str__(self):
        return self.name

class CityWeather(models.Model):
    name = models.CharField(max_length=255)
    weather = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
            return self.name