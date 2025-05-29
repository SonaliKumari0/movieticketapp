from django.db import models

# Create your models here.
geners = [
    ('Action', 'Action'),
    ('Adventure', 'Adventure'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Fantasy', 'Fantasy'),
    ('Horror', 'Horror'),
    ('Romance', 'Romance'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Thriller', 'Thriller'),
]
languages = [
    ('English', 'English'),
    ('Hindi', 'Hindi'),
    ('Telugu', 'Telugu'),
    ('Tamil', 'Tamil'),
    ('Kannada', 'Kannada'),
    ('Malayalam', 'Malayalam'),
]
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=250,choices=geners)
    language = models.CharField(max_length=100,choices=languages)
    synopsis = models.TextField()
    cast = models.TextField()
    duration_minutes = models.IntegerField()
    release_date = models.DateField()
    triller_url = models.CharField(max_length=2500, blank=True, null=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    slug = models.CharField(max_length=2500, unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "-")
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title