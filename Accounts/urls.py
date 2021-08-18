from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),
    path('signup',views.signup),
    path('logout',views.logout),

    path('profile',views.showProfile),
    path('editprofile',views.editProfile),

    path('manageplaylist',views.managePlaylist),
    path('newplaylist',views.newPlaylist),
    path('editplaylist/<pid>',views.editPlaylist),
    path('renameplaylist/<pid>',views.renamePlaylist),
    path('deleteplaylist/<pid>',views.deletePlaylist),

    path('addtofavourite',views.addToFav),

]
