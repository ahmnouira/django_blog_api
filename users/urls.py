from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path("<int:pk>", UserDetail.as_view(), name="user_detail"),
    path("", UserList.as_view(), name="user_list"),
]
