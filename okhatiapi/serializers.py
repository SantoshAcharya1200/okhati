# serializers.py
from rest_framework import serializers
from .models import OpeningHours, ExceptionDay

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'
        read_only_fields = ("user",)

class ExceptionDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExceptionDay
        fields = '__all__'
