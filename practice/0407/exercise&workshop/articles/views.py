from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # POST /articles/create/
    if request.method == 'POST':
        # Article table에 data를 저장함
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            #detail로 redirect
            return redirect('articles:index')
        print('errors?',form.errors)
        print('cleaned_data?',form.cleaned_data)
        
    # GET /articles/create    
    else:
        # 빈 껍데기 input form 
        form = ArticleForm()
    
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    context ={
        'article':article
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, id=pk)
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form':form
        }
        return render(request, 'articles/form.html', context)