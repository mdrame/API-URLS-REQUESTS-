from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from .models import IndexModel
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
                 'dummyModel': IndexModel.objects.all()
                }

    return render(request, "index.html", contextt)

#about view
def portfolio(request):

    contextt = {
                 'portfolioModel': portfolioModel
                }
   
    return render(request, "portfolio.html", contextt)


def detailViewPortfolio(request):

    contextt = {
                 'detailViewPortfolio': portfolioModel
                }
   
    return render(request, "detailViewPortfolio.html", contextt)


#portfolio view
def about(request):
    return HttpResponse('About page')

#contact view
def contact(request):
    return HttpResponse('Contact page')

# Todo: 
    # 1. Touch Resume.html, about & contact. 
    # 2. Pass Data back and foward
    # 3. Create DataBase Model for all needed pages
    # 5. Create Suber User
    # 6. Start Styling



