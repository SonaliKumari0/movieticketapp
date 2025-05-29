from django.db import models
from accounts.models import User
from movies.models import Movie
# Create your models here.
class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
