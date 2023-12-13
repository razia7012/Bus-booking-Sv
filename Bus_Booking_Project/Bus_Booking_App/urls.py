from django.urls import path
from .views import BusRouteList, BusScheduleList, BookingList

urlpatterns = [
    path('routes/', BusRouteList.as_view(), name='bus-route-list'),
    path('schedules/', BusScheduleList.as_view(), name='bus-schedule-list'),
    path('bookings/', BookingList.as_view(), name='booking-list'),
]
