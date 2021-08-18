from django.shortcuts import render,redirect
from .models import Song,Album
from Accounts.models import Playlist,PlaylistSongs,UserInfo

def Home(request):
    albums = Album.objects.all()
    if "uname" in request.session:
        playlist = Playlist.objects.filter(user_id = request.session["uname"])
        return render(request,"UserApp/home.html",{"albums":albums,"playlist":playlist})
    return render(request,"UserApp/home.html",{"albums":albums})

def AlbumSongs(request,aid):
    songs = Song.objects.filter(album_id=aid)
    return render(request,"UserApp/albumsongs.html",{"songs":songs})

def PlaySong(request,sid):
    song = Song.objects.get(id=sid)
    return render(request,"UserApp/playsong.html",{"song":song})

def PlayFavSong(request,sid):
    song = Song.objects.get(id=sid)
    return render(request,"UserApp/playfavsong.html",{"song":song})