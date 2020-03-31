from django.shortcuts import render

# Create your views here.

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    ping = request.GET.get('ping')
    context = {
        'ping': ping,
    }
    return render(request, 'pong.html', context)