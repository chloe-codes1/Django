from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm

# Create your views here.
def index(request):
    User = get_user_model()
    users = User.objects.all()
    content = {
        'users':users
    }
    return render(request,'accounts/index.html', content)

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