from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeContent, About, Portfolio
# Create your views here.

# Temporary Data Base 
# homePageDataBase = [
#     {'image': 'Image here',
#     'firstOccupation': 'iOS ',
#     'secondOccupation': 'BackEnd Web',
#     'title': '| Mohammed Drame'
#     }
# ]


def home(request):
    # Home Route 

    context = {
        'homeDataModel': HomeContent.objects.all()
    }
    return render(request, 'portfolioTemplate/home.html', context)


# Navigation routes Below 

def about(request):
    contexts = {
        'homeDataModel': About.objects.all()
    }
    return render(request, 'portfolioTemplate/about.html', contexts)


def portfolio(request):
    contextss = {
        'homeDataModel': Portfolio.objects.all()
    }
    return render(request, 'portfolioTemplate/portfolio.html', contextss)