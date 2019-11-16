from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from .models import Model, PortfolioModel
from django.views.generic import ListView, DetailView
# Create your views here.




# # Duummy Model here 
# #index.html model
# indexModel = [{ "Name": "Mohammed",
#                 "Title": " SoftWare Engineer",
#                 "About_Summery": " Hey my name is Mohammed. Am from  New Jersey"
#                 #Index model is limitt to the current styling design
#             }
#                 ]  

#home view
def index(request):
    ''' Index Page  model consist of 3 datas list above as dummyModel but
     is not limited to. You cac customize the model to you liking  '''

    contextt = {
                 'dummyModel': Model.objects.all()
                }

    return render(request, "index.html", contextt)


def portfolio(request):

    contextt = {
                 'context': PortfolioModel.objects.all()
                }
   
    return render(request, "portfolio.html", contextt)


def detail(request):
    contex = {
        'context': PortfolioModel.objects.all()
    }
    return render(request, 'detail.html', contex )


def about(request):
    return HttpResponse('About page')

def contact(request):
    return HttpResponse('Contact page')

# Todo: 
    # 1. Touch Resume.html, about & contact. 
    # 2. Pass Data back and foward
    # 3. Create DataBase Model for all needed pages
    # 5. Create Suber User
    # 6. Start Styling


# class ContactDetailView(DetailView):
#     template_name = "detail.html"
#     model = contact
#     context_object_name = 'contact'

