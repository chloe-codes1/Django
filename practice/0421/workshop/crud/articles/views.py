from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm, CommentForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
        'comment_form': CommentForm(),
    }
    return render(request, 'articles/detail.html', context)


def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 댓글 작성하는 POST 요청 핸들링
    if request.method == 'POST':
        #comment 작성
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 아직 article 정보가 들어오지 않음
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('articles:detail')
