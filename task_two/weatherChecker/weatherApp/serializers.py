from rest_framework import serializers
from .models import weatherModel


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = weatherModel
        fields = "__all__"