from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is index page")

def property(request):
    return HttpResponse("This is property page")

def about(request):
    return HttpResponse("This is about page")