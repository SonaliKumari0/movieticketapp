from django.urls import path
from . import views

urlpatterns = [
    path('movies/<slug:slug>/add-review/', views.add_review, name='add_review'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
]
