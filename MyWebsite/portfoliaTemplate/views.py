from django.shortcuts import render
from django.http import HttpResponse

from .models import ProjectName

# Create your views here.


def home(request ):
    return render(request, 'home.html', {})


def result(request, projectName_id):
    response = "You're looking at the results of product %s."
    return HttpResponse(response % projectName_id)



