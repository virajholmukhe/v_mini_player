from django.contrib import admin
from django.db import models
from .models import Song,Album
# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display=('id','name','image','file','album','artist','tags')
admin.site.register(Song,SongAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display=('id','name')
admin.site.register(Album,AlbumAdmin)