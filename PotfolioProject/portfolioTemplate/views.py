from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Data Base 
homePageDataBase = [
    {'image': 'Image here',
    'firstOccupation': 'iOS ',
    'secondOccupation': 'BackEnd Web',
    'title': '| Mohammed Drame'
    }
]


def home(request):
    # Home Route 

    context = {
        'homeDataModel': homePageDataBase
    }
    return render(request, 'portfolioTemplate/home.html', context)


# Navigation routes Below 

def about(request):
    
    return render(request, 'portfolioTemplate/about.html')

