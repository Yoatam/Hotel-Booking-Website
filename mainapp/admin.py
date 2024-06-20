from django.contrib import admin
from mainapp.models import Login
from django.contrib import admin

# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')



admin.site.register(Login, LoginAdmin)