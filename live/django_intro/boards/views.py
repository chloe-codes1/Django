from django.shortcuts import render

import random

# Create your views here.
def index(request):
    return render(request, 'boards/index.html')

def new(request):
    return render(request, 'boards/new.html')

def complete(request):
    # request는 요청과 관련된 정보들이 담긴 객체이다.
    # print(request.GET)
    # print(request.method)
    # print(request.path)
    # <QueryDict: {'title': ['1111'], 'content': ['1111']}>

    title = request.GET.get('title')
    response = request.GET.get('content')
    context = {
        'title': title,
        'content': response,
    }


    return render(request, 'boards/complete.html', context)