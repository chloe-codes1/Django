from django.db import models
from faker import Faker
from itertools import islice

f = Faker('ko_KR') #한국어로 localization

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Article.dummy(10)
    @classmethod
    def dummy(cls, number):
        batch_size = number//10
        objs = (cls(title=f.name(), context=f.text()) for _ in range(number))
        while 1:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            cls.objects.bulk_create(batch, batch_size)

    # [빠르게 create 하고 싶을 때]
    # Article.object.bulk_create()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)