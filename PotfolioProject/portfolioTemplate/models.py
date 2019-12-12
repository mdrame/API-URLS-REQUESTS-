from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Model for the Home page
class HomeContent(models.Model):
    # home page jumboTron
    image = models.ImageField(upload_to='profile_image', blank=True)
    # Left Text
    firstOccupaion = models.CharField(max_length=40000)
    # Right Text
    secondOccupation = models.CharField(max_length=40000)
    # Webpage tittle 
    pageTittle = models.CharField(max_length=40000)

    def __str__(self):
        return self.image



# -------- Home Content Model Ends Here -----
# -------------------------------------------



class About(models.Model):
    #big h1 text
    aboutH1 = models.CharField(max_length=40000)
    # about h3 text 
    describeYourSelf =  models.TextField()
    # image floating on the right
    aboutImage = models.ImageField(upload_to='profile_image', blank=True)


# -------- About Content Model Ends Here -----
# -------------------------------------------


class Portfolio(models.Model):
    # dateProjectAdded = Come Back to this 
    projectName = models.CharField(max_length=40000)
    aboutProject = models.TextField()
    projectImageOne = models.ImageField(upload_to='profile_image', blank=True)
    projecImageTwo = models.ImageField(upload_to='profile_image', blank=True)
    projectImageThree = models.ImageField(upload_to='profile_image', blank=True)
    projectImageFour = models.ImageField(upload_to='profile_image', blank=True)
    projectImageFive = models.ImageField(upload_to='profile_image', blank=True)
    projectLink = models.CharField(max_length=40000)
   

