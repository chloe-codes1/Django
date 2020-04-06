from django.shortcuts import render, redirect, get_object_or_404
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
    article.title= request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    # return redirect(f'/articles/{article.pk}/')
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article':article
    }
    return render(request,'articles/detail.html', context)


def delete (request, pk):
    article = Article.objects.get(id=pk)
    article.delete()

    # return redirect(f'/articles/')
    return redirect('articles:index')


def edit(request, pk):
    article = get_object_or_404(Article, id = pk)
    context = {
        'article': article
    }

    return render(request, 'articles/edit.html', context)

def update (request,pk):
    article = Article.objects.get(id=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect(f'/articles/{article.pk}/')