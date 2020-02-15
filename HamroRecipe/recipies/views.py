from django.shortcuts import render, redirect
from .models import Recipe, Incredients, Step
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
       # video = request.FILES['my-video']
        img = request.FILES['image']
        category = request.POST['category']
        type = request.POST['type']
        recipe = Recipe(r_name=r_name, username=username, img=img, category=category,
                        type=type)
        recipe.save()
        inc1 = request.POST['inc1']
        inc2 = request.POST['inc2']
        inc3 = request.POST['inc3']
        inc4 = request.POST['inc4']
        inc5 = request.POST['inc5'] #instance error here
        inc6 = request.POST['inc6']
        inc7 = request.POST['inc7']
        inc8 = request.POST['inc8']
        inc9 = request.POST['inc9']
        inc10 = request.POST['inc10']
        incredient = Incredients(r_name=r_name, inc_1=inc1, inc_2=inc2, inc_3=inc3, inc_4=inc4, inc_5=inc5,
                                 inc_6=inc6, inc_7=inc7, inc_8=inc8, inc_9=inc9, inc_10=inc10)
        incredient.save()
        step1 = request.POST['step1']
        step2 = request.POST['step2']
        step3 = request.POST['step3']
        step4 = request.POST['step4']
        step5 = request.POST['step5']
        step6 = request.POST['step6']
        step7 = request.POST['step7']
        step8 = request.POST['step8']
        step9 = request.POST['step9']
        step10 = request.POST['step10']
        step11 = request.POST['step11']
        step = Step(r_name=r_name, step1=step1, step2=step2, step3=step3, step4=step4, step5=step5, step6=step6,
                    step7=step7, step8=step8, step9=step9, step10=step10, step11=step11)
        step.save()
        return redirect("recipe")
    else:
        all_recipe = Recipe.objects.all()
        return render(request, 'recipe.html', {'recipes':all_recipe})


def showRecipePost(request):
    all_recipe = Recipe.objects.all()
    return render(request, 'recipepost.html',{'title':'Recipe|HamroRecipe', 'recipes':all_recipe})