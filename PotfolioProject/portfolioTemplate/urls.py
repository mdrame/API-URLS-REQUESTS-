from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [ 
    path('', views.home, name="home"), #'' automatically means home route
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio")
]