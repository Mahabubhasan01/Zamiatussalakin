from django.contrib import admin
from api.models import Blog, Comment
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'info', 'img', 'date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'info', 'date']
