from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showIndex, name='home'),
    path('contact', views.showContact, name="contact"),
    path('institutes', views.showInstitutes, name="institutes"),
    path('recipe', views.showRecipe, name="recipe"),
    path('recipe-posts', views.showRecipePost, name="rpost"),
    path('genrec',views.sendForm,name='genrec'),
]