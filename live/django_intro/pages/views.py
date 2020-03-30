from django.shortcuts import render

import random

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def hello(request):
    return render(request, 'pages/hello.html')

def lotto(request):

    pick = sorted(random.sample(range(1,46),6))
    context = {'pick':pick,}
    # return render(request, 'lotto.html', context)
    return render(request, 'pages/lotto.html', {'pick':pick})

def cube(request, num):
    return render(request, 'pages/cube.html',{'result':num**3})

def about_me(request):
    return render(request, 'pages/about_me.html')

def lunch(request):
    options = ['Waffle', 'Pizza', 'Fried chicken', 'Sushi', 'Fork chop', 'Grenola & Yogurt']
    menu = random.choice(options)
    context = {
        'menu': menu,
        'options': options
    }

    return render(request, 'pages/lunch.html', context)

def hi(request, name):
    context = {
        'name': name
    }
    return render(request, 'hi.html',context)

def add(request, a, b):
    result = a+ b
    context = {
        'a': a,
        'b':b,
        'result': result
    }
    return render(request,'pages/add.html', context)


def dinner(reqeust, menu, num):
    context = {
        'menu': menu,
        'num' : num,
    }
    return render(reqeust, 'pages/dinner.html', context)

def posts(request, id):
    content = 'Life is short, you need python!'
    replies = [ 'Thumbs up', 'Like your post', 'So informative!']
    no_replies = []
    user = 'admin'
    context = {
        'id':id,
        'content': content,
        'replies' : replies,
        'no_replies': no_replies,
        'user': user,
    }
    return render(request, 'pages/posts.html', context)