from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import hashlib

# Create your models here.
# model은 필요없다! Django package에 있는 User를 사용할 것이기 때문!

# 사용자 정의 모델 만들기
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'followings'
    )

    @property
    def gravatar_url(self):
        return f"https://s.gravatar.com/avatar/{hashlib.md5(self.email.encode('utf-8').strip().lower()).hexdigest()}?s=50&d=mp"