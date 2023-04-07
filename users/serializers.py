from rest_framework import serializers
from .models import CustomUser

# The serializer not only transforms data into JSON
# It can also specify which fields to include or exclude.


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "name", "email")


class UserSerializer(serializers.ModelSerializer):

    """
    ### fields = '__all__':

        ```json
        "id": 11,
        "password": "pbkdf2_sha256$390000$Rm716dqXTeqyBzyfOwVD2V$LHfJldHSymC5eikP8W5gKII09Qz2jmpKh3QXSUOuf28=",
        "last_login": "2023-04-07T17:08:46.127761Z",
        "is_superuser": false,
        "username": "ahmnouira@outlook.com",
        "first_name": "",
        "last_name": "",
        "email": "ahmnouira@outlook.com",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2023-04-07T17:08:40.860774Z",
        "name": null,
        "groups": [],
        "user_permissions": []
        ```
    """

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "name",
            "first_name",
            "last_name",
            # read_only_fields
            "username",  # username is the email used for authentication
            "password",
            "last_login",
            "is_superuser",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
        )
        read_only_fields = (
            "password",
            "last_login",
            "is_superuser",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
        )
