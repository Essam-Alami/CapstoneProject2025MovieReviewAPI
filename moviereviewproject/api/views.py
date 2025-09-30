# views.py
from django.db.models import Avg, Count
from rest_framework import viewsets, mixins, permissions, filters
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .permissions import IsAuthorOrReadOnly

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().annotate(
        avg_rating=Avg("reviews__rating"),
        reviews_count=Count("reviews")
    )
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title"]
    ordering_fields = ["created_at", "avg_rating", "reviews_count", "title"]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related("movie", "user").all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at", "rating"]

    def get_queryset(self):
        qs = super().get_queryset()
        movie = self.request.query_params.get("movie")
        if movie:
            # allow id or slug
            return qs.filter(models.Q(movie__id__iexact=movie) | models.Q(movie__slug__iexact=movie))
        # nested: /movies/<pk>/reviews/
        movie_pk = self.kwargs.get("movie_pk")
        if movie_pk:
            qs = qs.filter(movie_id=movie_pk)
        return qs

