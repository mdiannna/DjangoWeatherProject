from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import DailyWeather
# from django.template import loader
from django.shortcuts import render

# Create your views here.
def index(request):
    latest_weather_data_lst = DailyWeather.objects.order_by('timestamp')
    # template = loader.get_template('weather_info/index.html')
    context = {
        'latest_weather_data_lst': latest_weather_data_lst
    }

    return render(request, 'weather_info/index.html', context)
    # return HttpResponse(template.render(context, request))
    

def current_weather(request):

    weather_API_URL = 'https://api.openweathermap.org/data/2.5/weather'

    f = open('openweather_api_key.txt')
    api_KEY = str(f.read()).strip().replace("\n", "")

    munich_lat = 48.1113816
    munich_lon = 11.5756536

    request_URL = weather_API_URL + "?" + "lat=" + str(munich_lat) + "&lon=" + str(munich_lon) + "&appid=" +api_KEY

    print("request_url:", request_URL)


    r = requests.get(request_URL)
    print("text:", r.text)
    print("json:", r.json())
    
    return HttpResponse("Here will be the current weather prediction + request url:"+str( request_URL)  + str(r.json()))