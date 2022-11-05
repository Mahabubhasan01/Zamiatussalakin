from django.db import models
from django.conf import settings


class Blog(models.Model):
    author = models.CharField(max_length=50, default='Mehjabin chowdhury')
    title = models.CharField(max_length=100)
    info = models.TextField()
    img = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username
