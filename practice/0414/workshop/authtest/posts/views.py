from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html',context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
        messages.warning(request, 'Please check the form submitted')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/forms.html', context)

def detail(request,pk):
    post = get_object_or_404(Post, id=pk)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html',context)
    