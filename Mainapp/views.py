from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def HomePage(request):
    return HttpResponse('Home Page')

def Profile(request):
    return HttpResponse('Profile Page')

def Login(request):
    return HttpResponse('Login Page')

def Register(request):
    return HttpResponse('Register Page')

