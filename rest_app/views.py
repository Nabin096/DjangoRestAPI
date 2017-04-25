from rest_framework.response import Response
from rest_framework.views import APIView

from music.models import Album
from .serializers import AlbumSerialisers


# Create your views here.
class Android(APIView):
    def get(self,request):
        albums=Album.objects.all()
        myjson=AlbumSerialisers(albums,many=True)
        return Response(myjson.data)

    def post(self,request):
        pass