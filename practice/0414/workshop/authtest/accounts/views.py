from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, login, logout
# from django.contrib.auth.models import User 
# # -> User class는 내부에 정의되어 있으므로 get_user_model method로 호출한다!
from .forms import CustomUserChangeForm

# Create your views here.
def index(request):
    User = get_user_model()
    users = User.objects.all()
    content = {
        'users':users
    }
    return render(request,'accounts/index.html', content)
    
# create -> new (GET) & create(POST)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, id=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)


def update(request, pk):
    form = CustomUserChangeForm()
    context ={
        'form':form
    }
    return render(request, 'accounts/update.html', context)

def signin(request):
    if request.method == 'POST':
        # 사용자가 보낸 값 -> form
        form = AuthenticationForm(request, request.POST)
        # 검증
        # -> 검증 완료 시 로그인
        if form.is_valid():
            login(request, form.get_user())
            return redirect('accounts:index')
    else:    
        form = AuthenticationForm()
    context = {
        'form':form 
    }
    return render(request, 'accounts/signin.html', context)

def signout(request):
    logout(request)
    return redirect('posts:index')