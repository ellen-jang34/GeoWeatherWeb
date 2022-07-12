from django import forms

from .models import Post, City, CityWeather
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticMapWidget, GoogleStaticOverlayMapWidget



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)




class CityCreateForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name', 'location')
        widgets = {
            'location': GooglePointFieldWidget,
        }


class CityDetailForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name', 'location')
        widgets = {
            'location': GoogleStaticOverlayMapWidget(zoom=12, thumbnail_size='50x50', size='640x640'),
        }

class CityWeatherForm(forms.ModelForm):

    class Meta:
        model = CityWeather
        fields = ('name', 'weather')