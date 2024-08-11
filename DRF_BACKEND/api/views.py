from django.shortcuts import render
from rest_framework import viewsets

from .models import Artist, Albom, Songs
from .serializers import ArtistSerializerWeb, AlbomSerializerWeb, SongsSerializerWeb, ArtistSerializerTelegram, \
    AlbomSerializerTelegram, SongsSerializerTelegram


# Web
class ArtistViewSetWeb(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerWeb

    def get_queryset(self):
        return Artist.objects.all()


class AlbomViewSetWeb(viewsets.ModelViewSet):
    serializer_class = AlbomSerializerWeb

    def get_queryset(self):
        return Albom.objects.all()


class SongsViewSetWeb(viewsets.ModelViewSet):
    serializer_class = SongsSerializerWeb

    def get_queryset(self):
        return Songs.objects.all()


# Telegram
class ArtistViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerTelegram

    def get_queryset(self):
        return Artist.objects.all()


class AlbomViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = AlbomSerializerTelegram

    def get_queryset(self):
        return Albom.objects.all()


class SongsViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = SongsSerializerTelegram

    def get_queryset(self):
        return Songs.objects.all()