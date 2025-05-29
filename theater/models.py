from django.db import models
from accounts.models import User
from movies.models import Movie
# Create your models here.
class Theaters(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL , null=True, blank=True)
    
    def __str__(self):
        return self.name


class Showtimes(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL,null=True, blank=True)
    theater = models.ForeignKey(Theaters, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    screen_number = models.CharField(null=True, blank=True)
    
    
class Seats(models.Model):
    theater= models.ForeignKey(Theaters, on_delete=models.CASCADE)
    screen_number = models.CharField(max_length=100, null=True, blank=True)
    row_label = models.CharField(max_length=10)
    seat_number = models.CharField(max_length=10)
    seat_type = models.CharField(max_length=10, choices=[('VIP', 'VIP'), ('Regular', 'Regular')])
    
    