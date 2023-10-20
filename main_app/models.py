from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())  # Время публикации поста
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-publish']


