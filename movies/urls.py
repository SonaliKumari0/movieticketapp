from django.urls import path
from . import views

urlpatterns = [
    path('allmovies/', views.all_movies, name='all_movies'),
]
