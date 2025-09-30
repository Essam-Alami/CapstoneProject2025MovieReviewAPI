from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet, signup_view
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path("", include(router.urls)),

    path('', views.home_view, name='home'),      # 👈 now /api/ shows home.html
    path('signup/', signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
   
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

