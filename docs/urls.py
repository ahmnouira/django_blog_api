from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularJSONAPIView,
)

urlpatterns = [
    path("", SpectacularAPIView.as_view(), name="docs"),
    path("redoc/", SpectacularRedocView.as_view(url_name="docs"), name="redoc"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="docs"),
        name="swagger",
    ),
    path(
        "json/",
        SpectacularJSONAPIView.as_view(),
        name="json",
    ),
]
