from django.shortcuts import render
from django.http import HttpResponse

from .models import ProjectName

# Create your views here.


def home(request ):
    obj = ProjectName.objects.get(id=2                                                                                )
    context = { "Name": obj.name_text }
    
    return render(request, 'home.html',  context)


def result(request, projectName_id):
    response = "You're looking at the results of product %s."
    return HttpResponse(response % projectName_id)



