from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Duummy Model here 
#index.html model
indexModel = [{ "Name": "Mohammed",
                "Title": " SoftWare Engineer",
                "About_Summery": " Hey my name is Mohammed. Am from  New Jersey"
                #Index model is limitt to the current styling design
            }
                ]


#pofolio products.html model
portfolioModel = [{ "ProjectName": "Y E L P Z",
              "Technology": " Python, Flask, Django, MongoDB",
              "Image": " This is the logo on the project",
              "ReadMore": " This is a button",
               "Summery": " In this article I am going to present you with an easy (and advertisement/malware free) way to download videos from youtube, converting them to mp3 if needed. Also, I will give some more useful hints, for example how to download multiple mp3s using a script, how to break a long mp3 to same-length parts so you could quickly skip tracks when you play it in your stereo etc."
            },   
                    
             {

               "ProjectName": "Bulk Youtube",
              "Technology": " Python, Flask, Django, MongoDB",
              "Image": " This is the logo on the project",
              "ReadMore": " This is a button",
               "Summery": " In this article I am going to present you with an easy (and advertisement/malware free) way to download videos from youtube, converting them to mp3 if needed. Also, I will give some more useful hints, for example how to download multiple mp3s using a script, how to break a long mp3 to same-length parts so you could quickly skip tracks when you play it in your stereo etc."
            },

             {

               "ProjectName": "Gif Search",
              "Technology": " Python, Flask, Django, MongoDB",
              "Image": " This is the logo on the project",
              "ReadMore": " This is a button",
               "Summery": " In this article I am going to present you with an easy (and advertisement/malware free) way to download videos from youtube, converting them to mp3 if needed. Also, I will give some more useful hints, for example how to download multiple mp3s using a script, how to break a long mp3 to same-length parts so you could quickly skip tracks when you play it in your stereo etc."
            }
                ]




#home view
def index(request):
    ''' Index Page  model consist of 3 datas list above as dummyModel but
     is not limited to. You cac customize the model to you liking  '''

    contextt = {
                 'dummyModel': indexModel
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



