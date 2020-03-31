from django.shortcuts import render
from .models import Article

# Create your views here.
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return render(request,'articles/create.html')


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)