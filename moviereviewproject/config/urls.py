from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from api.views import home_view

urlpatterns = [
    path("api/", home_view, name="home"), 
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', RedirectView.as_view(url='/api/', permanent=False)),  # redirect root to /api/
    path("accounts/", include("django.contrib.auth.urls")),  # login/logout
]


