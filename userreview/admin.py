from django.contrib import admin
from userreview.models import Review, Memory

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_review', 'ratings')


class MemoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'title', 'image', 'about', 'date')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Memory, MemoryAdmin)