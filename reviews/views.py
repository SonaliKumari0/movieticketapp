from django.shortcuts import render, redirect, get_object_or_404
from .models import Reviews
from movies.models import Movie

def add_review(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')
        Reviews.objects.create(
            user=request.user if request.user.is_authenticated else None,
            movie=movie,
            review_text=review_text,
            rating=rating
        )
        return redirect(f'/movie/{slug}/')

    return render(request, 'reviews/add_review.html', {'movie': movie})


def delete_review(request, review_id):
    review = get_object_or_404(Reviews, review_id=review_id)

    if request.method == 'POST':
        review.delete()

    return redirect(f"/movie/{review.movie.slug}/")


