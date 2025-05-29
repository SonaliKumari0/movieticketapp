from django.db import models
from bookings.models import Booking
from accounts.models import User
# Create your models here.

class Payments(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=[('UPI', 'UPI'), ('CARD', 'CARD'), ('NETBANKING', 'NETBANKING')])
    amount = models.IntegerField()
    status = models.CharField(max_length=50, choices=[('SUCCESS', 'SUCCESS'), ('FAILED', 'FAILED')])
    transaction_time = models.DateTimeField(auto_now_add=True)