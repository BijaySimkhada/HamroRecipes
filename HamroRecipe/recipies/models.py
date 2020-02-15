from django.db import models

# Create your models here.


class Recipe(models.Model):
    r_id = models.IntegerField(auto_created=True, default=1)
    r_name = models.CharField(max_length=25, unique=True)
    video = models.FileField(upload_to='videos/', blank=True) #multi-value dict error
    username = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    img = models.ImageField(upload_to="photos/recipe", blank=True)

    def __str__(self):
        return self.r_name


class Incredients(models.Model):
    r_name = models.ForeignKey(Recipe, default=1, on_delete=models.SET_DEFAULT)
    inc_1 = models.CharField(max_length=20)
    inc_2 = models.CharField(max_length=20)
    inc_3 = models.CharField(max_length=20)
    inc_4 = models.CharField(max_length=20)
    inc_5 = models.CharField(max_length=20)
    inc_6 = models.CharField(max_length=20, blank=True)
    inc_7 = models.CharField(max_length=20, blank=True)
    inc_8 = models.CharField(max_length=20, blank=True)
    inc_9 = models.CharField(max_length=20, blank=True)
    inc_10 = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.r_id


class Step(models.Model):
    r_name = models.ForeignKey(Recipe,default=1, on_delete=models.SET_DEFAULT)
    step1 = models.CharField(max_length=255)
    step2 = models.CharField(max_length=255)
    step3 = models.CharField(max_length=255)
    step4 = models.CharField(max_length=255)
    step5 = models.CharField(max_length=255)
    step6 = models.CharField(max_length=255, blank=True)
    step7 = models.CharField(max_length=255, blank=True)
    step8 = models.CharField(max_length=255, blank=True)
    step9 = models.CharField(max_length=255, blank=True)
    step10 = models.CharField(max_length=255, blank=True)
    step11 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.r_id
