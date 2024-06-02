from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city>/', views.WeatherAPIView.as_view(), name='weather_api'),
]
