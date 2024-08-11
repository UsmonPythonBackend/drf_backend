
from django.shortcuts import render
from django.views import View
import requests

class HomeView(View):
    def get(self, request):
        artists = requests.get("http://localhost:8000/api/artists-web").json()
        context = {
            "artists": artists
        }
        return render(request, 'home.html', context)

class ArtistView(View):
    def get(self, request):
        return render(request, 'artist.html')

class AlbomView(View):
    def get(self, request):
        return render(request, 'albom.html')

class SongsView(View):
    def get(self, request):
        return render(request, 'songs.html')