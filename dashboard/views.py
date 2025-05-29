from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from datetime import timedelta
from bookings.models import Booking
from movies.models import Movie

def home(request):
    movies = Movie.objects.all()
    return render(request, 'dashboard/home.html', {'movies': movies})

@login_required
def your_orders(request):
    user = request.user
    bookings = Booking.objects.filter(user=user, booking_status='booked').order_by('-booking_time')

    return render(request, 'dashboard/your_orders.html', {
        'bookings': bookings
    })

def check_cancelled(showtime):
    buffer_time = now() + timedelta(minutes=30)
    return showtime > buffer_time

@login_required
def cancel_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
        if check_cancelled(booking.showtime.show_time):
            booking.booking_status = 'cancelled'
            booking.save()
            booking.bookingseats_set.all().delete()
            messages.success(request, "Booking cancelled successfully.")
        else:
            messages.error(request, "Cannot cancel booking within 30 minutes of showtime.")
    except Booking.DoesNotExist:
        messages.error(request, "Booking not found.")
    return redirect('your_orders')

def search_view(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        movies = Movie.objects.filter(title__icontains=search_query)
        return render(request, 'dashboard/search.html', {'movies': movies})
    return redirect('home')
