from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    @classmethod
    def dummy(cls, n):
        articles = []
        for i in range(n):
            articles.append(cls(title=f'title-{i+1}', content=f'content lorem ipsum'))

        cls.objects.bulk_create(articles)