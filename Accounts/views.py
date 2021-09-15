from re import S
from django.core.exceptions import EmptyResultSet
from django.db.models.fields.mixins import FieldCacheMixin
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from Accounts.models import Favourite, Playlist, PlaylistSongs, UserInfo
from django.contrib import messages
from UserApp.views import Home
from django.contrib.auth.hashers import make_password,check_password
from UserApp.models import Song, Album

def signup(request):
    if(request.method=="GET"):
        request.session.clear()
        return render(request,"Accounts/signup.html",{})
    else:
        username=request.POST["uname"]
        password=request.POST["upass"]

        if UserInfo.objects.filter(username=username).exists():
            return render(request,"Accounts/signup.html",{"exist":"username: "+username+" is already exist"})
        else:
            new_user=UserInfo()
            new_user.username = username
            new_user.password=make_password(password)
            new_user.save()
            return redirect(login)

def login(request):
    if(request.method=="GET"):
        request.session.clear()
        return render(request,"Accounts/login.html",{})
    else:
        username=request.POST["uname"]
        password=request.POST["upass"]
        try:
            u = UserInfo.objects.get(username=username)
            d_pass = u.password
            password_c = check_password(password,d_pass)
            if password_c:
                request.session["uname"]=username
        except:
            messages.error(request, 'invalid username or password')
            return render(request,"Accounts/login.html")
        return redirect(Home)

def logout(request):
    request.session.clear()
    return redirect(Home)

def managePlaylist(request):
    if("uname" in request.session):
        playlist = Playlist.objects.filter(user_id = request.session["uname"])
        return render(request,"Accounts/manageplaylist.html",{"playlist":playlist})

def newPlaylist(request):
    if("uname" in request.session):
        if(request.method=="GET"):
            return render(request,"Accounts/newplaylist.html")
        else:
            name = request.POST["name"]
            playlist = Playlist()
            playlist.name = name
            playlist.user = UserInfo.objects.get(username=request.session["uname"])
            playlist.save()
            return redirect(managePlaylist)

def editPlaylist(request,pid):
    if("uname" in request.session):
        if(request.method=="GET"):
            playlist = Playlist.objects.get(id=pid)
            pls = PlaylistSongs.objects.filter(playlist_id=pid)
            return render(request,"Accounts/editplaylist.html",{"playlist":playlist,"pls":pls})

def renamePlaylist(request,pid):
    if("uname" in request.session):
        if request.method=="POST":
            new_name = request.POST["name"]
            u = Playlist.objects.get(id=pid)
            u.name = new_name
            u.save()
            return redirect(managePlaylist)
        else:
            playlist = Playlist.objects.get(id=pid)
            return render(request,"Accounts/renameplaylist.html",{"playlist":playlist})

def deletePlaylist(request,pid):
    if("uname" in request.session):
        if request.method=="GET":
            playlist = Playlist.objects.get(id=pid)
            playlist.delete()
            return redirect(managePlaylist)

def showProfile(request):
    if("uname" in request.session):
        profile=UserInfo.objects.get(username=request.session["uname"])
        return render(request,"Accounts/profile.html",{"profile":profile})

def editProfile(request):
    if(request.method=="GET"):
        if("uname" in request.session):
            profile=UserInfo.objects.get(username=request.session["uname"])
            return render(request,"Accounts/profile-edit.html",{"profile":profile})
        else:
            redirect(login)
    else:
        if(UserInfo.objects.get(username=request.session["uname"])):
            profile1=UserInfo.objects.get(username=request.session["uname"])
            profile1.first_name=request.POST["first_name"]
            profile1.last_name=request.POST["last_name"]
            profile1.email=request.POST["email"]
            profile1.save()
            redirect(showProfile)
        else:
            pass

def addToFav(request):
    if("uname" in request.session):
        if request.method == "POST":
            sid = request.POST["sid"]
            try:
                fav_song = Favourite.objects.get(user_id=request.session["uname"],song_id=sid)
                fav_song.delete()
            except:
                fav = Favourite()
                fav.user = UserInfo.objects.get(username=request.session["uname"]) 
                fav.song = Song.objects.get(id=sid)
                fav.save()
            return redirect(addToFav)
        else:
            songs = Song.objects.all()
            fav = Favourite.objects.filter(user_id=request.session["uname"])
            return render(request,"UserApp/favourites.html",{"fav":fav,"songs":songs})
    else:
        redirect(login)

def allSongs(request,pid):
    songs = Song.objects.all()
    playlist = Playlist.objects.get(id=pid)
    return render(request,"Accounts/addtoplaylist.html",{"songs":songs,"playlist":playlist})

def addToPlaylist(request,sid):
    if("uname" in request.session):
        if request.method == "POST":
            pid = request.POST["pid"]
            pl = Playlist.objects.get(id=pid)
            s = Song.objects.get(id=sid)
            try:
                pls = PlaylistSongs.objects.get(playlist_id=pid,Song_id=sid)
                return redirect(managePlaylist)
            except:
                pls = PlaylistSongs()
                pls.playlist = pl
                pls.Song = s
                pls.save()
                return redirect(managePlaylist)
        else:
            pass
    else:
        redirect(login)

def removeFromPlaylist(request,sid):
    if("uname" in request.session):
        if request.method == "POST":
            pid = request.POST["pid"]
            pls = PlaylistSongs.objects.get(playlist_id=pid,Song_id=sid)
            pls.delete()
            return redirect(managePlaylist)
            
        else:
            pass
    else:
        redirect(login)


def playlistSongs(request,pid):
    if("uname" in request.session):
        playlist = PlaylistSongs.objects.filter(playlist_id=pid)
        return render(request,"UserApp/playlist.html",{"playlist":playlist})


