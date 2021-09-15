from django.contrib import admin
from .models import UserInfo, Favourite

class UserInfoAdmin(admin.ModelAdmin):
    list_display=('username','password','first_name','last_name','email')

admin.site.register(UserInfo,UserInfoAdmin)

class FavouritesAdmin(admin.ModelAdmin):
    list_display=('user_id','song_id')

admin.site.register(Favourite,FavouritesAdmin)