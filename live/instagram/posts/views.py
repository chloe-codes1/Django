from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm, CommentForm


# Create your views here.

def index(request):
    # primary key 역순으로 정렬하긔
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # 추가함
            post.user = request.user
            post.save()
            return redirect('posts:index')
        messages.warning(request, 'Please check the form submitted')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/forms.html', context)

def detail(request,pk):
    post = get_object_or_404(Post, id=pk)
    form = CommentForm()
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/detail.html',context)

@require_POST
def delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('posts:index')

def update(request, pk):
    post = get_object_or_404(Post,id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'posts/forms.html', context)
    