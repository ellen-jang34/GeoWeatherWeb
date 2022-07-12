from django.urls import path, re_path 
from . import views

from .views import CityCreateView, CityListView, CityDetailView

app_name = 'cities'

urlpatterns = [
    path('post/new/', views.post_new, name='post_new'),
    path('', CityListView.as_view(), name="list"),
    re_path(r'^(?P<pk>\d+)/$', CityDetailView.as_view(), name="detail"),
    re_path(r'^create/$', CityCreateView.as_view(), name="create"),
    path('hello/', views.wordview, name="wordview")
]