from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from django.http import JsonResponse
from .models import Movie, Review
import requests
from .models import Movie, Review
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Assign the logged-in user automatically
        serializer.save(user=self.request.user)


def home(request):
    movies = Movie.objects.all()
    reviews_list = Review.objects.all()
    context = {
        'movies': movies,
        'reviews': reviews_list
    }
    return render(request, 'home.html', context)