from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.registerview, name='register'),  
    path ('home/',views.home,name='home'),
    path ('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
]
    