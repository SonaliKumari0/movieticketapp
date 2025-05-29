from django.contrib import admin
from .models import Theaters ,Showtimes, Seats
# Register your models here.

class ShowtimesInline(admin.TabularInline):
    model = Showtimes
    extra = 5  

@admin.register(Theaters)
class TheatersAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'address', 'manager']
    inlines = [ShowtimesInline] 
    
@admin.register(Showtimes)
class ShowtimesAdmin(admin.ModelAdmin):
    list_display = ['movie', 'theater', 'show_time', 'screen_number']
    
@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ['id','theater', 'screen_number', 'row_label', 'seat_number', 'seat_type']
    
