from rest_framework import serializers
from music.models import Album

class AlbumSerialisers(serializers.ModelSerializer):

    class Meta:
        model=Album
        fields='__all__'