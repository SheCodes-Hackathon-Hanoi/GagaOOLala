# views.py
# from datetime import datetime
from datetime import datetime
from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Count
from travel.models import TravelList, CustomUser, Booking, Review, Favor, Point
from .serializers import (
    TravelListSerializer,
    CustomUserSerializer,
    BookingSerializer,
    ReviewSerializer,
    FavorSerializer,
    # PointSerializer,
)
from django.db.models import F
import os


# Create your views here.
@api_view(["GET"])
def listTrending(request):
    most_booked_travels = TravelList.objects.annotate(
        booking_count=Count("booking")
    ).order_by("-booking_count")[:3]

    travels = []
    for travel in most_booked_travels:
        if travel:
            travel_dict = model_to_dict(
                travel,
                fields=[
                    "id",
                    "title",
                    "hostName",
                    "hostPhone",
                    "location",
                    "price",
                    "place",
                    "type",
                ],
            )
            file_name = os.path.basename(travel.homestay_img.path)
            travel_dict["homestay_img"] = file_name
            travels.append(travel_dict)
    return JsonResponse(travels, safe=False)

def calculate_points(user_id_, travel_id):
    # Fetch the user, travel item, and user's favor using the provided IDs
    user = CustomUser.objects.get(id=user_id_)

    travel_item = TravelList.objects.get(id=travel_id)
    print("go here")
    user_favor = Favor.objects.get(user_id=user_id_)
    age = datetime.now().year - user.dob.year
    # Initialize points
    points = 0

    # Check if user's favor matches the place
    if user_favor.mountain and travel_item.place == "mountain":
        points += 40
    if user_favor.sea and travel_item.place == "sea":
        points += 40

    # Check age and price conditions
    # age =
    if age < 22 and travel_item.price < 1000000:
        points += 20

    # Check if user's favor matches the type
    if user_favor.risky and travel_item.type == "risky":
        points += 40
    if user_favor.resortive and travel_item.type == "resortive":
        points += 40
    return points


@api_view(["POST"])
def listRecommend(request):
    user_id = request.data["user_id"]  # Get the user_id from the request data

    # Retrieve all TravelList objects
    travel_items = TravelList.objects.all()

    # Calculate points for each travel item and store them in a dictionary
    points = {}
    for item in travel_items:
        print(item.id)
        point = calculate_points(user_id, item.id)
        points[item.id] = point

    # Sort the travel items by their points in descending order
    sorted_items = sorted(
        travel_items, key=lambda item: points.get(item.id, 0), reverse=True
    )

    # Get the top 3 travel items
    top_3_items = sorted_items[:3]



    # Create a response dictionary with the top 3 items and their points
    response_data = []
    for item in top_3_items:
        response_data.append(
            {
                "travel_id": item.id,
                "title": item.title,  # Replace with the actual field name
                "points": points.get(item.id, 0),
                "homestay_img": os.path.basename(item.homestay_img.path),
            }
        )

    return JsonResponse({"recommendations": response_data})


class TravelListView(viewsets.ModelViewSet):
    serializer_class = TravelListSerializer
    queryset = TravelList.objects.all()


class CustomUserView(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class FavorView(viewsets.ModelViewSet):
    serializer_class = FavorSerializer
    queryset = Favor.objects.all()