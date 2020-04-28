from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
# model은 필요없다! Django package에 있는 User를 사용할 것이기 때문!

# 사용자 정의 모델 만들기
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'followings'
    )