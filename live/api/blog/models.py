from django.db import models
from faker import Faker

f =Faker()

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def dummy (cls, n):
        for _ in range(n):
            # .bulk_create() 로 빠르게 해보기
            cls.objects.create(
                title= f.name(),
                content= f.text(),
            )
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

