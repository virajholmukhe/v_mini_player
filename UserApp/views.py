from django.shortcuts import render,redirect
from UserApp.models import Song,Album
from Accounts.models import Favourite, Playlist,PlaylistSongs,UserInfo
from django.db.models import Q, query

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
    songs = Song.objects.filter(album_id=song.album_id)
    next_song = get_next_or_prev(songs,song,"next")
    prev_song = get_next_or_prev(songs,song,"prev")

    if("uname" in request.session):
        try:
            fav_song = Favourite.objects.get(user_id=request.session["uname"],song_id=sid)
            flag = "True"
        except:
            flag = "False"
        return render(request,"UserApp/playsong.html",{"song":song,"next_song":next_song,"prev_song":prev_song,"flag":flag})
    else:
        return render(request,"UserApp/playsong.html",{"song":song,"next_song":next_song,"prev_song":prev_song})

def get_next_or_prev(models, item, direction):
    getit = False
    if direction == "prev":
        models = models.order_by("-id")
    for m in models:
        if getit:
            return m
        if item == m:
            getit = True
    if getit:
        return models[0]
    return False

def PlayFavSong(request,sid):
    song = Favourite.objects.get(song_id=sid,user_id=request.session["uname"])
    songs = Favourite.objects.filter(user_id=request.session["uname"])
    next_song = get_next_or_prev(songs,song,"next")
    prev_song = get_next_or_prev(songs,song,"prev")

    try:
        fav_song = Favourite.objects.get(user_id=request.session["uname"],song_id=sid)
        flag = "True"
    except:
        flag = "False"

    if("uname" in request.session):
        return render(request,"UserApp/playfavsong.html",{"song":song,"next_song":next_song,"prev_song":prev_song,"flag":flag})
    else:
        return redirect(Home)

def playPlaylistSong(request,sid):
    if("uname" in request.session):
        song = PlaylistSongs.objects.get(Song_id=sid)
        pl = Playlist.objects.get(user_id=request.session["uname"])
        pid = pl.id
        pls = PlaylistSongs.objects.filter(playlist_id=pid)
        next_song = get_next_or_prev(pls,song,"next")
        prev_song = get_next_or_prev(pls,song,"prev")

        try:
            fav_song = Favourite.objects.get(user_id=request.session["uname"],song_id=sid)
            flag = "True"
        except:
            flag = "False"

        return render(request,"UserApp/playplaylistsong.html",{"song":song,"next_song":next_song,"prev_song":prev_song,"flag":flag})
    else:
        return redirect(Home)
    

def search(request):
    sq = request.GET["sq"]
    query = (Q(name__icontains = sq) | Q(artist__icontains = sq))
    songs = Song.objects.filter(query)
    return render(request,"UserApp/albumsongs.html",{"songs":songs})

def about(request):
    return render(request,'UserApp/about.html')