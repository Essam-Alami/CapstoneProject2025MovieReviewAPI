from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from django.http import JsonResponse
import requests
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]  # only logged-in users can POST

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'api/signup.html', {'form': form})  # 👈 notice api/

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'api/login.html', {'form': form}) 

@login_required
def home_view(request):
    return render(request, 'api/home.html')