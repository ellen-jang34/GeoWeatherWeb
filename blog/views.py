from django.shortcuts import render

#google map
from django.views.generic import FormView, ListView, UpdateView
from django.urls import reverse

from .forms import CityCreateForm, CityDetailForm
from .models import City, CityWeather
# Create your views here.

from .forms import PostForm

#dailyweather
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from pyowm import OWM
from django.utils import timezone

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


class CityListView(ListView):
    queryset = City.objects.all()
    template_name = "cities/list.html"
    context_object_name = "cities"


class CityDetailView(UpdateView):
    form_class = CityDetailForm
    model = City
    template_name = "cities/detail.html"

    # CityWeather.objects.latest('pub_date')

class CityCreateView(FormView):
    template_name = "cities/form.html"
    form_class = CityCreateForm
    success_url = '/cities/hello/'

    def form_valid(self, form):
        print(form.cleaned_data.get("location"))
        print(type(form.cleaned_data.get("location")))

        API_key = '7e7dae4857ca4c6e4f1566f301e5e591'
        owm = OWM(API_key) 
        mgr = owm.weather_manager()
        obs = mgr.weather_at_coords((form.cleaned_data.get("location")[0]), (form.cleaned_data.get("location")[1]))
        w = obs.weather
        res = w.status # Clouds
        res1 = w.detailed_status # scattered clouds 
        w2 = obs.weather.wind() # {'speed': 3.6, 'deg': 250} 
        weather = res ; res1 ; w2  

        queryset = City.objects.all()
        c = CityWeather(name=form.cleaned_data.get('name'), weather= weather, pub_date=timezone.now())
        c.save()
        #print(weather)
        form.save()
        
        return super(CityCreateView, self).form_valid(form)

def wordview(request):
    response = CityWeather.objects.latest('pub_date')
    return HttpResponse(response.weather)
