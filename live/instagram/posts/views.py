from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden #Forbidden 은 403 code를 class로 만든 것!

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
        form = PostForm(request.POST, request.FILES)
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

@login_required
@require_POST
def delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user == post.user:
        post.delete()
    return redirect('posts:index')

@login_required
def update(request, pk):
    post = get_object_or_404(Post,id=pk)
    #글 작성한 본인인지 확인
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('posts:detail', post.pk)
        else:
            form = PostForm(instance=post)
        context = {
            'form': form
        }
        return render(request, 'posts/forms.html', context)
    #본인이 아니면 목록페이지로 돌아가라!
    else:

        # ver1) 메시지와 함께 index page 반환  
        # messages.warning(request, '본인 글만 수정 가능합니다.')
        # return redirect('posts:index')

        # ver2) 403 status code 반환
        return HttpResponseForbidden()


@require_POST
# @login_required 
# -> request.user.is_authenticated 를 대신 하기 위해 하는 것
def comments_create(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect('posts:detail', post.pk)
    else:
        # ver1) next paraameter 없이 진행하기
        messages.warning(request, '댓글을 작성할 권한이 없습니다')
        return redirect('accounts:login')

        # ver2) 401 page로 보내버리기
        # return HttpResponse(status=401)