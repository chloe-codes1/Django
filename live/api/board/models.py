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
            cls.objects.create(
                title= f.name(),
                content= f.text(),
            )