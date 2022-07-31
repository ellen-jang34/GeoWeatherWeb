# GeoWeatherWeb Project

Weather Information Service Website
-----

### This website is Django-base and provides weather information of the location that is pin-pointed or searched on search bar of the website by a user. 

Features
-----
- Using GeoDjango
- Map SDK API from Google Maps Platform
- Weather infromation from OpenWeatherMap (OWN) API
- 


Setup
-----

- Install **PostGIS**, **SpatiaLite** for Spatial Database
- Create a project 
```
$ django-admin startproject geosite
```
- Create an application within the project 
```
$ python manage.py geosite 
```
- project/setting.py



How to Open the Webpage
-----
1. Run(open) Postgres
2. Activate env
```$ source env/bin/activate
```
3. Within the project, run the server
Before running the server, move to the folder **geosite**.
```$ cd geosite
```
Now, run the server.
```$ python manage.py runserver
```