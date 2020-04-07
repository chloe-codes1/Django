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
    if request.method == 'POST':
        # POST /articles/new  -> (구) create() 함수
        form = ArticleForm(request.POST)
        # 검증하기
        if form.is_valid():
            article = form.save()
            # -> article은 Article instance를 return 함
            return redirect('articles:index')
    else:
        # GET /articles/new
        form = ArticleForm()

        # 공용 context
        context = {
            'form': form
        }
        return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request,pk):
    article = get_object_or_404(Article, id=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == 'POST':
        form =ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 수정시에는 해당 article instance를 넘겨줘야 한다!
        form = ArticleForm(instance=article)
    context = {
        'form':form
    }
    return render(request, 'articles/form.html', context)