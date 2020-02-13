from django.shortcuts import render, redirect
from .models import Recipe
# Create your views here.


def showIndex(request):
    return render(request, 'pages/Indexpage.html', { 'title':'Homepage | HamroRecipe'})


def showContact(request):
    return render(request, 'pages/contact.html', {'title':"Contact | HamroRecipe"})


def showRecipe(request):
    if request.method == 'POST':
        r_name = request.POST['r_name']
        username = request.POST['username']
        description = request.POST['description']
        incredients = request.POST['incredients']
        img = request.FILES['image']
        category = request.POST['category']
        type = request.POST['type']
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
        step12 = request.POST['step12']
        step13 = request.POST['step13']
        step14 = request.POST['step14']
        step15 = request.POST['step15']
        step16 = request.POST['step16']
        recipe = Recipe(r_name=r_name, username=username, img=img, category=category, description=description,
                        type=type, incredients=incredients, step1=step1, step2=step2, step3=step3, step4=step4,
                        step5=step5, step6=step6, step7=step7, step8=step8, step9=step9, step10=step10, step11=step11,
                        step12=step12, step13=step13, step14=step14, step15=step15, step16=step16,)
        recipe.save()
        return redirect("recipe")
    else:
        all_recipe = Recipe.objects.all()
        return render(request, 'recipe.html', {'recipes':all_recipe})