from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import BusRoute, BusSchedule, Booking
from .serializers import BusRouteSerializer, BusScheduleSerializer, BookingSerializer

class BusRouteList(generics.ListCreateAPIView):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer

class BusScheduleList(generics.ListCreateAPIView):
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


