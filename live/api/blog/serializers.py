from rest_framework import serializers
from .models import Article, Comment

# GET => Data 전송
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title']

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','content']

# Data 받아서 valid()
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'