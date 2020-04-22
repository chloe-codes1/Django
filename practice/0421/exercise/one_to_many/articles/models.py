from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'#{self.pk} ({self.title} - {self.content})'


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
                                # model 중에 Article을 가리키고 있다
    
    def __str__(self):
        return f'Comment #{self.pk} for Post #{self.article_id}'