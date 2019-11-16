from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# home page model 
class IndexModel(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about_Summery = models.CharField(max_length=300)

    def __stry__(self):
        return self.name 


