from django.db import models

# Create your models here.

class TravelListModel(models.Model):
    title = models.TextField(default="", blank=False)
    hostName = models.TextField(default="", blank=False)
    hostPhone = models.TextField(default="", blank=False)
    location = models.TextField(default="", blank=False)
    activities = models.TextField(default="", blank=False)
    price = models.IntegerField(default=0, blank=False)