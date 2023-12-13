
import django_filters
from .models import BusRoute, BusSchedule

class BusRouteFilter(django_filters.FilterSet):
    class Meta:
        model = BusRoute
        fields = {
            'origin': ['exact', 'contains', 'startswith'],
            'destination': ['exact', 'contains', 'startswith'],
            'duration': ['exact'],
            'distance': ['exact'],
        }

class BusScheduleFilter(django_filters.FilterSet):
    class Meta:
        model = BusSchedule
        fields = {
            'name__name':['exact','contains','startswith'],
            'route__origin': ['exact', 'contains', 'startswith'],
            'route__destination': ['exact', 'contains', 'startswith'],
            'departure_time': ['exact', 'contains', 'startswith'],
            'available_seats': ['exact'],
        }
