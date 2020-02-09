from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.db.models.functions import Cast
from .models import Article
from django.db.models import CharField

# Create your views here.


def showblog(request):
    all_article = Article.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        title = request.POST['title']
        img = request.FILES['image']
        slug = request.POST['slug']
        body = request.POST['body']
        article = Article(user_name=username, title=title, img=img, slug=slug, body=body)
        article.save()
        return redirect('/blog')
    else:
        return render(request, 'blog.html', {'title':'Blog|HamroRecipe', 'articles': all_article})



#def success(request):
#    return HttpResponse('successfully uploaded')
    #    all_article = Article.objects.all()
#    return render(request, 'blog.html', {'title':'Blog|HamroRecipe', 'articles': all_article })

