from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#  model 
class Model(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about_Summery = models.CharField(max_length=300)



    def __stry__(self):
        return self.name 


#  model 
class PortfolioModel(models.Model):

    projectName = models.CharField(max_length=100)
    ganguages = models.CharField(max_length=200)
    gitHub_link = models.CharField(max_length=300)
    # images


    def __stry__(self):
        return self.projectName


