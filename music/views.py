from django.http import HttpResponse
from django.shortcuts import render

from .forms import AlbumRegister
from .models import Album


def index(request):
    return HttpResponse("<h1>this is the music homepage</h1>")

def register(request):
    albums=Album.objects.all()
    context={
        'albums':albums
    }
    artist =""
    album_title =""

    if request.method=='POST':
        MyForm=AlbumRegister(request.POST)
        if MyForm.is_valid():
            artist=MyForm.cleaned_data['artist']
            album_title=MyForm.cleaned_data['album_title']
            myAlbum=Album()
            myAlbum.artist=artist
            myAlbum.album_title=album_title
            myAlbum.save()

    else:
        MyForm=AlbumRegister(request.GET)
        return render(request, 'music/index.html', context)

    return render(request,'music/index.html',context)
