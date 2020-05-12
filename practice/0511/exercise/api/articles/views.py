from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, ArticleDetailSerializer
# Create your views here.

@api_view(['GET','POST'])
def article_list_create(request):
    
    if request.method == 'POST':
        # 글을 생성
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    else:
        # 모든 글을 보여줌
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True) #여러개임을 many option으로 알려줌
    
    return Response(serializer.data) #serializer는 객체이므로 그 안에 있는 data를 넣어줘야함 
    
    
@api_view(['GET','PUT','DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method =='GET':
        # 상세 조회
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    elif request.method =='PUT':
        # 글을 수정 (찾아 바꾼다)
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response( {'message': 'Your post has been updated.', 'data': serializer.data})
        return Response(serializer.data)
    elif request.method =='DELETE':
        # 글을 삭제 (찾아 지운다)
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return Response({'message': 'Your post has been deleted.'})

@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
