from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    r_name = models.CharField(max_length=25, unique=True)
    video = models.FileField(upload_to='videos/recipe', blank=True, null=True)  # multi-value dict error
    seen=models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    category = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    img = models.ImageField(upload_to="photos/recipe", blank=True, null=True)
    created_at = models.DateField(null=True)

    def __str__(self):
        return self.r_name


class Incredients(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, blank=False)
    qty = models.FloatField(null=False)
    unit = models.CharField(max_length=25)


class Step(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    step_no = models.IntegerField(default=1)
    step_name = models.TextField(default=1)
