from rest_framework import serializers
from .models import TravelList, CustomUser, Booking, Review, Favor

class TravelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelList
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class FavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favor
        fields = '__all__'