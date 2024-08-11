from django.urls import path
from .views import HomeView, ArtistView, AlbomView, SongsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('artist/', ArtistView.as_view(), name='artist'),
    path('albom/', AlbomView.as_view(), name='albom'),
    path('songs/', SongsView.as_view(), name='songs'),
]