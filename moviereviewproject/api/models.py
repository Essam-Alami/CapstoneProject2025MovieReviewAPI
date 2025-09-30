from django.conf import settings
from django.db import models
from django.utils.text import slugify

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = f"{self.title}-{self.year}" if self.year else self.title
            self.slug = slugify(base)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.year})" if self.year else self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1–5
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("movie", "user")  # each user reviews a movie once
        ordering = ["-created_at"]

