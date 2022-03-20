from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('current_weather', views.current_weather, name='current_weather')
]