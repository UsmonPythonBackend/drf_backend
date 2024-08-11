from django.urls import path, include
from rest_framework import routers
from .views import ArtistViewSetWeb, ArtistViewSetTelegram

router = routers.DefaultRouter()
router.register(r'artist-web', ArtistViewSetWeb, basename='artist-web')

router.register(r'artist-telegram', ArtistViewSetTelegram, basename='artist-telegram')



urlpatterns = [
    path('', include(router.urls))
]