
from rest_framework import serializers
from .models import Post

# The serializer not only transforms data into JSON
# It can also specify which fields to include or exclude.


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at"
        )
