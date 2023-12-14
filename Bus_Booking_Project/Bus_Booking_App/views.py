

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .models import BusRoute, BusSchedule, Booking
from .serializers import BusRouteSerializer, BusScheduleSerializer, BookingSerializer
from .filters import BusRouteFilter, BusScheduleFilter

class BusRouteList(generics.ListCreateAPIView):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BusRouteFilter

class BusScheduleList(generics.ListCreateAPIView):
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BusScheduleFilter

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

