from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Home),
    path('albumsongs/<aid>',views.AlbumSongs),
    path('playsong/<sid>',views.PlaySong),
    path('playfavsong/<sid>',views.PlayFavSong),

]
