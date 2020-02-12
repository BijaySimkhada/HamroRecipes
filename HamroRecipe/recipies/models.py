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
    step1 = models.TextField()
    step2 = models.TextField()
    step3 = models.TextField()
    step4 = models.TextField(blank=True)
    step5 = models.TextField(blank=True)
    step6 = models.TextField(blank=True)
    step7 = models.TextField(blank=True)
    step8 = models.TextField(blank=True)
    step9 = models.TextField(blank=True)
    step10 = models.TextField(blank=True)
    step11 = models.TextField(blank=True)
    step12 = models.TextField(blank=True)
    step13 = models.TextField(blank=True)
    step14 = models.TextField(blank=True)
    step15 = models.TextField(blank=True)
    step16 = models.TextField(blank=True)

def __str__(self):
   return self.r_name