from django.contrib import admin

# Register your models here.
from .models import DailyWeather

admin.site.register(DailyWeather)

