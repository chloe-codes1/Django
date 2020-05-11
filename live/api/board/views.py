from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

# 노가다 방법.. 한땀한땀
@require_GET
def article_list_json_1(request):
    articles = Article.objects.all()
    data = []
    for article in articles:
        data.append( {
            'article_id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at' : article.updated_at,
        })
    return JsonResponse(data, safe=False) # safe를 주는 이유: safe=False여야지만 dictionary가 아닌 것을 보낼 수 있다

# django_core serializers ... 한방에
@require_GET
def article_list_json_2(request):
    from django.core import serializers
    
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data,content_type = 'application/json')

# REST framework
@api_view(['GET'])  #어떤  요청을 받겠다
def article_list_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    # rest_framework의 serializer를 return하려면, Response 사용
    return Response(serializer.detail)