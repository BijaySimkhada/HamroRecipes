from django.shortcuts import render, redirect
from .models import Recipe
# Create your views here.


def showIndex(request):
    return render(request, 'pages/Indexpage.html', { 'title':'Homepage | HamroRecipe'})


def showContact(request):
    return render(request, 'pages/contact.html', {'title':"Contact | HamroRecipe"})


def showInstitutes(request):
    return render(request, 'pages/institutes.html', {'title':"Institutes | HamroRecipe"})


def showRecipe(request):
    if request.method == 'POST':
        r_name = request.POST['r_name']
        username = request.POST['username']
        description = request.POST['description']
        incredients = request.POST['incredients']
        img = request.FILES['image']
        category = request.POST['category']
        type = request.POST['type']
        step = request.POST['step']
        recipe = Recipe(r_name=r_name, username=username, img=img, category=category, description=description,
                        type=type, incredients=incredients, step=step )
        recipe.save()
        return redirect("recipe")
    else:
        all_recipe = Recipe.objects.all()
        return render(request, 'recipe.html', {'recipes':all_recipe})


def showRecipePost(request):
    all_recipe = Recipe.objects.all()
    steps = (
        all_recipe.step1,all_recipe.step2, all_recipe.step3, all_recipe.step4, all_recipe.step5, all_recipe.step6, all_recipe.step7,
        all_recipe.step8, all_recipe.step9, all_recipe.step10, all_recipe.step11, all_recipe.step12, all_recipe.step13, all_recipe.step14,
        all_recipe.step15, all_recipe.step16,
    )
    return render(request, 'recipepost.html',{'title':'Recipe|HamroRecipe', 'recipes':all_recipe, 'steps':steps})