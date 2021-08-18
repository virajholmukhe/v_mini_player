from django.contrib import admin
from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display=('username','password','first_name','last_name','email')

admin.site.register(UserInfo,UserInfoAdmin)