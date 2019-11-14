from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Duummy Model here 

dummyModel = [{ "Name": "Mohammed",
              "Title": " SoftWare Engineer",
              "About_Summury": " Hey my name is Mohammed. Am from  New Jersey"
            }, 
            { "Name": "Mohammed",
              "Title": " SoftWare Engineer",
              "About_Summury": " Hey my name is Mohammed. Am from  New Jersey"
            },
            { "Name": "Mohammed",
              "Title": " SoftWare Engineer",
              "About_Summury": " Hey my name is Mohammed. Am from  New Jersey"
            },
            { "Name": "Mohammed",
              "Title": " SoftWare Engineer",
              "About_Summury": " Hey my name is Mohammed. Am from  New Jersey"
            }
                ]


#home view
def index(request):
    ''' Index Page  model consist of 3 datas list above as dummyModel but
     is not limited to. You cac customize the model to you liking  '''

    contextt = {
                 'dummyModel': dummyModel
                }

    return render(request, "index.html", contextt)

#about view
def about(request):
    return HttpResponse('About page')

#portfolio view
def portfolio(request):
    return HttpResponse('Portfolio page')

#contact view
def contact(request):
    return HttpResponse('Contact page')

