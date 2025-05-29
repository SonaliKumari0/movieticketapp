from django.db import models
from accounts.models import User
from theater.models import Showtimes, Seats, Theaters
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    showtime = models.ForeignKey(Showtimes, on_delete=models.SET_NULL, null=True, blank=True)
    booking_time = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(max_length=20, choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'),('Pending', 'Pending')])

    def __str__(self):
        return f"Booking by {self.user.username} for {self.showtime.movie.title} on {self.showtime.show_time}"
    
class BookingSeats(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seats, on_delete=models.SET_NULL, null=True, blank=True)
    