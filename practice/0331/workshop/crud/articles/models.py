from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __repr__(self):
        return f'Title: {self.title} & Content: {self.content}'