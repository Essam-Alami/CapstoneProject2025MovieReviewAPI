from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"reviews", ReviewViewSet, basename="review")

movies_router = NestedSimpleRouter(router, r"movies", lookup="movie")
movies_router.register(r"reviews", ReviewViewSet, basename="movie-reviews")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/", include(movies_router.urls)),
    path("api/auth/", include("rest_framework.urls")),  # browsable login
]
