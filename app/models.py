from ast import mod
from django.db import models
from django.conf import settings
import uuid


class BlogPost(models.Model):
    category = (('travel', 'travel'), ('fashion', 'fashion'),
                ('food', 'food'), ('science', 'science'),)
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=50, default='Mehjabin chowdhury')
    title = models.CharField(max_length=100)
    info = models.TextField()
    qoutes = models.TextField(blank=True)
    img = models.ImageField(upload_to='images')
    category = models.CharField(
        max_length=10, choices=category, blank=True, default='travel')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def blog_Category(self):
        return self.category


class UserComment(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username


class Notice(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
