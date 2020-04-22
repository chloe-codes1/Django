from django.db import models

# Create your models here.
class Reporter(models.Model):
    username = models.CharField(max_length=10)

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)