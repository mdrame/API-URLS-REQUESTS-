from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # Home Route 
    return HttpResponse('<h1> Home </h1>')



