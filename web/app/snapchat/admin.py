from django.contrib import admin

from .models import Snap, Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'snap', 'created_on', 'listened_on', 'upload')
    list_filter = ('visited',)
    search_fields = ('name', 'description')
    ordering = ('-listened_on',)


class SnapAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    ordering = ('-created_on',)


admin.site.register(Snap, SnapAdmin)
admin.site.register(Song, SongAdmin)
