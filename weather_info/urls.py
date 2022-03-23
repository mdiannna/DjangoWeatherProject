from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather_now', views.weather_now, name='weather_now'),
    path('weather_now_json', views.weather_now_json, name='weather_now_json')
]