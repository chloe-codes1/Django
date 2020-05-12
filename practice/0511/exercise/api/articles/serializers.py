from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'created_at', 'updated_at']
        # comment_set

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# 상속
class ArticleDetailSerializer(ArticleSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta(ArticleSerializer.Meta):
        fields = ArticleSerializer.Meta.fields + ['comment_set']


