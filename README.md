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

1. Install **PostGIS**, **Postgres**, **SpatiaLite** for Spatial Database
2.  Create a project 
```
$ django-admin startproject geosite
```
3. Create an application within the project 
```
$ python manage.py geosite 
```
4. geosite/setting.py in the geosite project

-  Change the database connection settings to match the setup(your installed database)
```
DATABASES = {
    'default': {

        'ENGINE': 'django.contrib.gis.db.backends.postgis',

        'NAME': 'geodjango',

        'USER': 'postgres',

        'PASSWORD': 'tonycoding',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}
```
- Modify Installed App to include **django.contrib.gis**, **blog** , and **mapwidgets**.
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'blog',
    'mapwidgets',
]
```




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
