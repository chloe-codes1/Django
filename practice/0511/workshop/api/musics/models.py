from django.db import models
from faker import Faker
from itertools import islice

f = Faker()

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=20)

    @classmethod
    def dummy(cls, number):
        batch_size = number//10
        objs = (cls(name=f.name()) for _ in range(number))
        while 1:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            cls.objects.bulk_create(batch, batch_size)   

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()
