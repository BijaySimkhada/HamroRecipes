from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    user_name = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    slug = models.SlugField()
    body = models.TextField()
    img = models.ImageField(upload_to="photos/blog/", blank=True)
    date = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title
