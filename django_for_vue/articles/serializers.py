from rest_framework import serializers
from .models import Article
from accounts.serializers import UserSerializer

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', ' created_at']

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False) # is_valid() 에서 유무 검증을 pass 한다
    class Meta:
        model = Article
        fields = '__all__'