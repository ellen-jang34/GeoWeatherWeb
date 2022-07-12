# Generated by Django 3.2.5 on 2021-08-19 09:28

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(help_text='Use map widget for point the house location', srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(help_text='Use map widget for point the house location', srid=4326)),
                ('name', models.CharField(max_length=255)),
                ('location_has_default', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(-104.9903, 39.7392), srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('address', models.TextField()),
                ('neighbour_of_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.house')),
            ],
        ),
    ]
