from django.contrib import admin
from .models import Booking, BookingSeats
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'showtime', 'booking_time', 'total_amount', 'booking_status']
  
  
@admin.register(BookingSeats)
class BookingSeatsAdmin(admin.ModelAdmin):
    list_display = ['booking', 'seat']
    
