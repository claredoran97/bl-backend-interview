from django.shortcuts import render, get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view 
from .forms import InputForm
from .models import weatherModel
from .serializers import WeatherSerializer
from .openWeather import OpenWeather
from datetime import datetime, timedelta
 
def index(request):
  return HttpResponse("Hello")

# Create your views here.
def home_view(request):
  if request.method == "GET":
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)
  elif request.method == "POST":
    print("HEY!")
    
    current_city = request.POST.get('city', None).lower()
    print(f'Curerent city: {current_city}')
    query_result = weatherModel.objects.filter(city=current_city).exists()
    print(f'Query RESULT: {query_result}')

    if query_result == True:
      current_weather = weatherModel.objects.get(city=current_city)
      print(current_weather.queryDate)
      print(datetime.now()-timedelta(hours=4))
      if current_weather.queryDate < timezone.now()-timedelta(hours=4):
        weatherBool = weatherQuery(current_city)
        if weatherBool != False:
          current_weather = weatherModel.objects.get(city=current_city)
          current_temp = current_weather.temprature
        else:
          current_temp = "not available/api issues"
      else:
        current_temp = current_weather.temprature
    else:
      weatherBool = weatherQuery(current_city)
      print(weatherBool)
      if weatherBool != False:
        current_weather = weatherModel.objects.get(city=current_city)
        current_temp = current_weather.temprature
      else:
        current_temp = "not available/api issues"
    
    return render(request, 'home.html', {'form': InputForm(), 'temperature': current_temp, 'city': current_city})


def weatherQuery(city):
  openWeatherObj = OpenWeather(city)
  weatherResult = openWeatherObj.returnResult()
  print()
  print(weatherResult)
  if weatherResult["temprature"] != None:
    current_weatherModel = weatherModel(city=weatherResult["city"], temprature = weatherResult["temprature"])
    current_weatherModel.save()
    return True
  else:
    return False



