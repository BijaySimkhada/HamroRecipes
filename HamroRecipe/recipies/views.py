from django.shortcuts import render

# Create your views here.


def showIndex(request):
    return render(request, 'pages/Indexpage.html',{ 'title':'Homepage'})


def showContact(request):
    return render(request, 'pages/contact.html', {'title':"Contact | HamroRecipe"})