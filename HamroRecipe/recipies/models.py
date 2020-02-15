from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    r_name = models.CharField(max_length=25, unique=True)
    video = models.FileField(upload_to='videos/', blank=True)  # multi-value dict error
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    category = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    img = models.ImageField(upload_to="photos/recipe", blank=True)
    created_at = models.DateField(null=True)


class Incredients(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, blank=False)
    qty = models.FloatField(null=False)


class Step(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    step_no = models.IntegerField
    step_name = models.TextField
