from django.urls import path, include
from rest_framework import routers
from .views import ArtistViewSetWeb, ArtistViewSetTelegram, AlbomViewSetWeb, SongsViewSetWeb, AlbomViewSetTelegram, SongsViewSetTelegram

router = routers.DefaultRouter()
router.register(r'artist-web', ArtistViewSetWeb, basename='artist-web')
router.register(r'albom-web', AlbomViewSetWeb, basename='albom-web')
router.register(r'songs-web', SongsViewSetWeb, basename='songs-web')
router.register(r'artist-telegram', ArtistViewSetTelegram, basename='artist-telegram')
router.register(r'albom-telegram', AlbomViewSetTelegram, basename='albom-telegram')
router.register(r'songs-telegram', SongsViewSetTelegram, basename='songs-telegram')



urlpatterns = [
    path('', include(router.urls))
]
