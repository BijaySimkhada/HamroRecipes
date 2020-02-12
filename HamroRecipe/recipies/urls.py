from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showIndex, name='home'),
    path('contact', views.showContact, name="contact"),
    path('recipe', views.showRecipe, name="recipe"),
]