from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('profile/', views.Profile, name='profile'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
]