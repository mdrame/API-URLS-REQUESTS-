from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse('About page')

def portfolio(request):
    return HttpResponse('Portfolio page')

def contact(request):
    return HttpResponse('Contact page')

