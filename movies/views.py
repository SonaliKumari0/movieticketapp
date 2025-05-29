from django.shortcuts import render, get_object_or_404
from .models import Movie
from reviews.models import Reviews
from django.db.models import Avg
from datetime import datetime

def allmovies(request):
    movies = Movie.objects.all().order_by('-release_date')  
    context = {
        'movies': movies
    }
    return render(request, 'movies/movies.html', context)


def movieview(request, slug):
    if Movie.objects.filter(slug=slug).exists():
        today = datetime.today().date()
        movie = Movie.objects.get(slug=slug)
        if Reviews.objects.filter(movie=movie).exists():
            reviews = Reviews.objects.filter(movie=movie)
            no_user = reviews.count()
            rating = reviews.aggregate(avg_rating=Avg('rating'))
            context = {
                'movie': movie,
                'rating': rating['avg_rating'],
                'no_user': no_user,
                'reviews': reviews,
                'today': today,
            }
            return render(request, 'movies/movieview.html', context)
    return render(request, 'movies/404.html', status=404) 

from django.shortcuts import render
from .models import Movie

def filtered_movies(request):
    movies = Movie.objects.all().order_by('-release_date')

    selected_language = request.GET.get('language')
    selected_genre = request.GET.get('genre')
    search_query = request.GET.get('q')

    if selected_language:
        movies = movies.filter(language=selected_language)

    if selected_genre:
        movies = movies.filter(genre=selected_genre)

    if search_query:
        movies = movies.filter(title__icontains=search_query)

    languages = [lang[0] for lang in Movie._meta.get_field('language').choices]
    genres = [g[0] for g in Movie._meta.get_field('genre').choices]

    context = {
        'movies': movies,
        'languages': languages,
        'genres': genres,
        'selected_language': selected_language,
        'selected_genre': selected_genre,
        'search_query': search_query,
    }

    return render(request, 'movies/movies.html', context)
