from django.shortcuts import render
from .models import Recipe
# Create your views here.


def showIndex(request):
    return render(request, 'pages/Indexpage.html', { 'title':'Homepage | HamroRecipe'})


def showContact(request):
    return render(request, 'pages/contact.html', {'title':"Contact | HamroRecipe"})


def showRecipe(request):
    context = {}
    all_recipe = Recipe.objects.all();
    return render(request, 'recipe.html', {'recipes':all_recipe})