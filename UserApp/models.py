from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Movie"

class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    tags = models.CharField(max_length=50)
    image = models.ImageField(upload_to='songimages')
    file = models.FileField(upload_to='songfiles')
    album = ForeignKey(Album,on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Song"