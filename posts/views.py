from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, PostListSerializer
from .permissions import IsAuthorOrReadOnly


# Create your views here.


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostListSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
