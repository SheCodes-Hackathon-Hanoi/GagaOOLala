from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Add custom fields
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('host', 'Host'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

    phone = models.CharField(max_length=15, blank=False)
    # print("3"+ phone)


class TravelList(models.Model):
    title = models.TextField(default="", blank=False)
    hostName = models.TextField(default="", blank=False)
    hostPhone = models.TextField(default="", blank=False)
    location = models.TextField(default="", blank=False)
    activities = models.TextField(default="", blank=False)
    price = models.IntegerField(default=0, blank=False)

class Booking(models.Model):
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location_id = models.ForeignKey(TravelList, on_delete=models.CASCADE)
    start_date = models.DateField(default="", blank = False)
    end_date = models.DateField(default="", blank = False)
    total_price = models.IntegerField(default=0, blank=False)
    status = models.CharField(max_length=20)

class Review(models.Model):
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()

class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location = models.ForeignKey(TravelList, on_delete=models.CASCADE)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    STATUS_CHOICES = (
        ('waiting', 'Waiting'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')

class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()