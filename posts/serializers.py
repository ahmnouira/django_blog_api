from rest_framework import serializers
from .models import Post
from accounts.serializers import AuthorSerializer


# The serializer not only transforms data into JSON
# It can also specify which fields to include or exclude.


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "body")


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "created_at")
