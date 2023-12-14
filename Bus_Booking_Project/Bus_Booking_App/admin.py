from django.contrib import admin
from .models import BusRoute, BusSchedule, Booking, Bus

# Register your models here.

admin.site.register(Bus)
admin.site.register(BusRoute)
admin.site.register(BusSchedule)
admin.site.register(Booking)