from django.shortcuts import render
from .models import Article

# function generic view

# def index(request):
#     articles = Article.objects.all()
#     return render(request, 'articles/index.html', {'articles': articles})

# class based generic view
from django.views.generic import ListView, DetailView

class ArticleListView(ListView):
    model = Article
    # template_name = 'articles/모델명_list.html' -> 이렇게 하면 자동으로 찾음
    # context_object_name = 'object_list'

class ArticleDetailView(DetailView):
    model = Article

    # def get(request,):

    # @    
    # def put():

    # def delete():
