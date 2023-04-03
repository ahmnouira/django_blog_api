from rest_framework import serializers
from .models import CustomUser

# The serializer not only transforms data into JSON
# It can also specify which fields to include or exclude.


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "name", "email")
