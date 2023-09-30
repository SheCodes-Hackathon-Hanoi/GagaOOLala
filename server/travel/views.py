from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Count
from travel.models import TravelList, Booking
from .serializers import TravelListSerializer

# Create your views here.
@api_view(['GET'])
def listTrending():
    most_booked_travels = TravelList.objects.annotate(booking_count=Count('booking')).order_by('-booking_count')[:5]
    travels = []
    for travel in most_booked_travels:
        if travel:
            travels.append(travel)
    return Response(travels)

class TravelListView(viewsets.ModelViewSet):
    serializer_class = TravelListSerializer
    queryset = TravelList.objects.all()
