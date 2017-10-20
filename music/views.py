from django.http import HttpResponse
from django.http import Http404
from .models import Artist , Song
from django.template import loader
from django.shortcuts import render , get_object_or_404

# Create your views here.

def index(request) :
    all_albums = Artist.objects.all()
    # Create a dictionary ..
    context = {"all_albums" : all_albums}
    return render(request , "music/index.html" , context)


def detail(request , album_id) :
    album = get_object_or_404(Artist , pk=album_id)
    album_title = album.album_title
    album_logo = album.album_logo
    all_songs = album.song_set.all()
    context = {"all_songs": all_songs , 'album': album , "album_title" : album_title , "album_logo" : album_logo}
    return render(request , "music/detail.html" , context)

