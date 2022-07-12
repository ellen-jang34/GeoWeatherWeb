from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from .models import WorldBorder

#admin.site.register(WorldBorder, admin.GeoModelAdmin)
#Substituted in the last step from GeoModelAdmin to OSMGeoAdmin
# OpenStreetMap layer in the admin with streets info and more details
admin.site.register(WorldBorder, admin.OSMGeoAdmin)