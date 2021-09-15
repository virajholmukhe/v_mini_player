from typing import Callable
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from UserApp.models import Song, Album


class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=30,blank=True)
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table="Userinfo"

class Playlist(models.Model):
    name = models.CharField(max_length=20)
    user = ForeignKey(UserInfo,on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table="Playlist"

class PlaylistSongs(models.Model):
    playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    Song = models.ForeignKey(Song,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
    
    class Meta:
        db_table="PlaylistSongs"

class Favourite(models.Model):
    song = ForeignKey(Song,on_delete=models.CASCADE)
    user = ForeignKey(UserInfo,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.song)
    
    class Meta:
        db_table="favourite"