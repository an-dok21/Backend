from django.shortcuts import render, get_object_or_404
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from constants import WEATHER_API_KEY

'''
@ Class WeatherAPIView(APIView)
  Find City's weather status based on name
'''
class WeatherAPIView(APIView):
    def get(self, request, city, *args, **kwargs):
        api_key = WEATHER_API_KEY
        url_current = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
        url_forecast = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=5'

        response_current = requests.get(url_current)
        response_forecast = requests.get(url_forecast)

        if response_current.status_code == 200 and response_forecast.status_code == 200:
            current_data = response_current.json()
            forecast_data = response_forecast.json()

            weather_data = {
                'current': {
                    'location': current_data['location']['name'],
                    'temperature': current_data['current']['temp_c'],
                    'wind_speed': current_data['current']['wind_kph'] / 3.6,
                    'humidity': current_data['current']['humidity'],
                    'condition': current_data['current']['condition']['text'],
                    'icon': current_data['current']['condition']['icon'],
                },
                'forecast': [
                    {
                        'date': day['date'],
                        'temperature': day['day']['avgtemp_c'],
                        'wind_speed': day['day']['maxwind_kph'] / 3.6,
                        'humidity': day['day']['avghumidity'],
                        'condition': day['day']['condition']['text'],
                        'icon': day['day']['condition']['icon'],
                    } for day in forecast_data['forecast']['forecastday']
                ]
            }

            return Response(weather_data, status=status.HTTP_200_OK)
        
        return Response({'error': 'Cannot find data'}, status=status.HTTP_400_BAD_REQUEST)
    

