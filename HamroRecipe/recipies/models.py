from django.db import models

# Create your models here.


class Recipe(models.Model):
    r_name = models.CharField(max_length=25)
    description = models.TextField()
    username = models.CharField(max_length=25)
    category = models.CharField(max_length=25) #contentinental hoki local hoki bla bla bla
    type = models.CharField(max_length=25)
    img = models.ImageField(upload_to="photos/recipe", blank=True)
    incredients = models.TextField(blank=False, default=1)
    step = models.TextField()

def __str__(self):
   return self.r_name
