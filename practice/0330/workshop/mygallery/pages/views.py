from django.shortcuts import render
import requests
import json
from decouple import config

key = config('USPLASH_CLIENT_ID')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):

    category = request.GET.get('category')
    response = requests.get(f'https://api.unsplash.com/search/photos?query={category}&client_id={key}').json()
    photos = []
    length = response['total']
    for i in range(length):
        try:
            photos.append(response['results'][i]['urls']['regular'])
        except IndexError:
            pass

    content = {
        'photos': photos,
        'category': category,
    }

    return render(request, 'gallery.html', content)