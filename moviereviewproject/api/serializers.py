# serializers.py
from rest_framework import serializers
from .models import Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)
    reviews_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "year", "slug", "created_at", "avg_rating", "reviews_count"]

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # shows username

    class Meta:
        model = Review
        fields = ["id", "movie", "user", "rating", "body", "created_at", "updated_at"]

    def validate_rating(self, v):
        if not 1 <= v <= 5: raise serializers.ValidationError("Rating must be 1–5.")
        return v

    def create(self, validated):
        validated["user"] = self.context["request"].user
        return super().create(validated)
