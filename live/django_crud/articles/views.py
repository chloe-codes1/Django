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
    article.title= request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return redirect(f'articles/{article.pk}/')


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article':article
    }
    return render(request,'articles/detail.html', context)