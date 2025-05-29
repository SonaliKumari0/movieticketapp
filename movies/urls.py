from django.urls import path
from . import views

urlpatterns = [
    # path('movies/',views.allmovies, name='allmovies'),
    path('movie/<slug>/', views.movieview, name='movieview'),
    path('allmovies/', views.filtered_movies, name='filtered_movies'),
]
