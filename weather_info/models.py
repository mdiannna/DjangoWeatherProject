from django.db import models
from django.utils import timezone

# Create your models here.
class DailyWeatherObject(models.Model):
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField('timestamp')
    temperature = models.IntegerField()
    wind = models.IntegerField()
    humidity = models.IntegerField()

    SUNNY = "SUN"
    WINDY = "WIND"
    SNOWY = "SNOW"
    FOGGY = "FOG"
    RAINY = "RAIN"
    WARM = "WARM"
    COLD = "COLD"
    UNDEFINED = "-"

    WEATHER_TYPE_CHOICES = [
        (SUNNY, 'sunny'),
        (WINDY, 'windy'),
        (SNOWY, 'snowy'),
        (FOGGY, 'foggy'),
        (RAINY, 'rainy'),
        (WARM, 'warm'),
        (COLD, 'cold'),
        (UNDEFINED, 'undefined')
    ]
   
    weather_type = models.CharField(max_length=4, choices=WEATHER_TYPE_CHOICES, default=UNDEFINED)


    def __str__(self):
        return self.description

    # def was_published_recently(self):
    #     return self.timestamp >= timezone.now() - datetime.timedelta(days=1)