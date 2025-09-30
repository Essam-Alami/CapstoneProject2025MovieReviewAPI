from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls

