from django.shortcuts import render, redirect
from .models import Recipe, Incredients, Step
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse


# Create your views here.


def showIndex(request):
    rec = Recipe.objects.order_by('-created_at').all()[:4]
    return render(request, 'pages/Indexpage.html', {'title': 'Homepage | HamroRecipe', 'recipes':rec})


def showContact(request):
    return render(request, 'pages/contact.html', {'title': "Contact | HamroRecipe"})


def showInstitutes(request):
    return render(request, 'pages/institutes.html', {'title': "Institutes | HamroRecipe"})


def showRecipe(request):
    if request.method == 'POST':
        if request.POST['r_name'] == '' and request.POST['cats'] == '' and request.POST['type'] == '':
            messages.warning(request, 'Invalid Input')
            return redirect('recipe')
        else:
            new_rec = Recipe()
            new_rec.username = request.user
            new_rec.r_name = request.POST['r_name']
            new_rec.category = request.POST['cats']
            new_rec.type = request.POST['type']
            if request.FILES:
                new_rec.img = request.FILES['image']
                new_rec.video = request.FILES['videos']
            new_rec.created_at = datetime.now()
            saved = new_rec.save()
            # return HttpResponse(new_rec.id)
            for i in range(1, int(request.POST['ingcount']) + 1):
                if request.POST['inc' + str(i)] == '' and request.POST['qty' + str(i)] == '':
                    messages.warning(request, 'Invalid Input')
                else:
                    new_ing = Incredients()
                    new_ing.recipe_id = new_rec
                    new_ing.name = request.POST['inc' + str(i)]
                    new_ing.qty = request.POST['qty' + str(i)]
                    new_ing.unit = request.POST['unit' + str(i)]
                    new_ing.save()
            for i in range(1, int(request.POST['pcount']) + 1):
                if request.POST['step' + str(i)] == '':
                    messages.warning(request, 'Invalid Input')
                else:
                    new_stp = Step()
                    new_stp.recipe_id = new_rec
                    new_stp.step_name = request.POST['step' + str(i)]
                    new_stp.save()
        messages.success(request, 'Your Recipe Has Been Successfully Inserted')
        return redirect('recipe')
    else:
        rec = Recipe.objects.order_by('-created_at').all()[:10]
        return render(request, 'recipe.html', {'recipes': rec, 'count': range(1, 15)})



def sendForm(request):
    if request.method == 'POST':
        if request.POST['r_name'] == '' and request.POST['cat'] == '' and request.POST['type'] == '':
            messages.warning(request, 'Invalid Input')
            return redirect('recipe')
        else:
            return render(request, 'ingredients.html', {'r_name': request.POST['r_name'],
                                                        'cat': request.POST['cat'], 'type': request.POST['type'],
                                                        'ingcount': request.POST['ingcount'],
                                                        'pcount': request.POST['pcount'],
                                                        'irange': range(1, int(request.POST['ingcount']) + 1),
                                                        'prange': range(1, int(request.POST['pcount']) + 1)})



def showRecipePost(request, id):
    rec = Recipe.objects.filter(id=id).order_by('-created_at').all()[:10]
    ing = Incredients.objects.filter(recipe_id=id).all()
    pro = Step.objects.filter(recipe_id=id).all()
    return render(request, 'recipepost.html', {'title': 'Recipe|HamroRecipe', 'recipes': rec, 'ings':ing, 'pros':pro})
