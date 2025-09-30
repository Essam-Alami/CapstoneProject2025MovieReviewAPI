from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from django.http import JsonResponse
from .models import Movie

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


def home(request):
    return render(request, "api/home.html")


def home(request):
    movies = Movie.objects.all()  # fetch all movies from DB
    return render(request, "api/home.html", {"movies": movies})

