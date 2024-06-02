from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    location = serializers.CharField(max_length=100)
    temperature = serializers.FloatField()
    wind_speed = serializers.FloatField()
    humidity = serializers.IntegerField()
    condition = serializers.CharField(max_length=100)
    icon = serializers.CharField(max_length=100)