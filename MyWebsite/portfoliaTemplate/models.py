from django.db import models

# Create your models here.

# class projectImage(models.Model):

# class projectLink(models.Model):

# project name class object
class ProjectName(models.Model):
    name_text = models.CharField(max_length=200)

    def __str__(self):
        return self.name_text


#project description class object 
# class ProjectDescription(models.Model):
#     descrition_text = models.CharField(max_length=1000)

# class ProjectTechnologyUsed(models.Model):
#     tecnology_text = models.CharField(max_length=1000)


# class ProjectName(models.Model):

# class projectLink(models.Model):


    
