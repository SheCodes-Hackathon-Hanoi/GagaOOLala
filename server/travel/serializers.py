from rest_framework import serializers
from .models import TravelList

class TravelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelList