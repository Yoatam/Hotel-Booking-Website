from django.contrib import admin
from hotellist.models import Hotellist
from django.db import models

# Register your models here.
class HotellistAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'star',
                    'image', 'current_cost', 'delete_cost')


admin.site.register(Hotellist, HotellistAdmin)