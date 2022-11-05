from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import BlogPost, UserComment
# Register your models here.


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'info', 'img', 'date']


@admin.register(UserComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'info', 'date']
