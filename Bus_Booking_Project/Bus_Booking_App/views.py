from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import BusRoute, BusSchedule, Booking
from .serializers import BusRouteSerializer, BusScheduleSerializer, BookingSerializer

class BusRouteList(generics.ListCreateAPIView):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer
    permission_classes = [permissions.IsAuthenticated]

class BusScheduleList(generics.ListCreateAPIView):
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


