from django.urls import path
from .views import PostList, PostDetails

urlpatterns = [
    path("<int:pk>", PostDetails.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list")
]
