from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['movie_id','title', 'genre','language','synopsis', 'cast', 'duration_minutes', 'release_date','triller_url','status','image_url','slug']

