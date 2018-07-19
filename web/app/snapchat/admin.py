from django.contrib import admin

from .models import Snap, Song


def unlisten(songs):
    """ Makes all songs from queryset songs unvisited and sets their
        listened_on field to None
    """
    songs.update(visited=False)
    songs.update(listened_on=None)


def unlistenSong(modeladmin, request, queryset):
    unlisten(queryset)


def unlistenSnap(modeladmin, request, queryset):
    for snap in queryset:
        songs = Song.objects.filter(snap=snap)
        unlisten(songs)


unlistenSong.short_description = "Unlisten selected songs"
unlistenSnap.short_description = "Unlisten all songs from seleceted snaps"


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'snap', 'created_on', 'listened_on', 'upload')
    list_filter = ('visited', 'snap')
    search_fields = ('name', 'description')
    ordering = ('-listened_on',)
    actions = [unlistenSong]


class SnapAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    ordering = ('-created_on',)
    actions = [unlistenSnap]


admin.site.register(Snap, SnapAdmin)
admin.site.register(Song, SongAdmin)
