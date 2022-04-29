from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("login/", views.loginUser, name = 'login'),
    path("registration/", views.registration, name = 'registration'),
    path("logout/", views.logoutUser, name = 'logout'),
    
]