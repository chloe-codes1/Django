from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    
    return redirect('/articles/')

def details(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('/articles/')

def update(request,pk):
    article = Article.objects.get(id=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('/articles/') 

def search(request):
    keyword = request.POST.get('keyword')
    results = Article.objects.filter(title__icontains=keyword)
    context = {
        'results': results,
        'keyword': keyword,
    }

    return render(request,'articles/search_result.html',context)