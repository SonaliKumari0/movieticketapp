from django.urls import path
from . import views

urlpatterns = [
    path('your-orders/', views.your_orders, name='your_orders'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('search/', views.search_view, name='search'),
]
