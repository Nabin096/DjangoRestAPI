from django import forms

class AlbumRegister(forms.Form):
    artist = forms.CharField(max_length=250)
    album_title = forms.CharField(max_length=500)