from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import  Blog, Comment
from app.models import BlogPost,UserComment
# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = '__all__'
