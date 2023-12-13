from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from account.models import CustomUser

class Bus(models.Model):
    name = models.CharField(max_length=200)
    bus_no = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class BusRoute(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    duration = models.DurationField()
    distance = models.FloatField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"

class BusSchedule(models.Model):
    name = models.ForeignKey(Bus,on_delete=models.CASCADE,default=1)
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    schedule = models.ForeignKey(BusSchedule, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

