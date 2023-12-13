from rest_framework import serializers
from .models import BusRoute, BusSchedule, Booking

class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute
        fields = '__all__'

class BusScheduleSerializer(serializers.ModelSerializer):
    route= serializers.StringRelatedField()
    name = serializers.StringRelatedField()
    class Meta:
        model = BusSchedule
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
