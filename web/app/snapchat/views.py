import math
from datetime import datetime

from django.shortcuts import get_object_or_404, render

from .models import Snap, Song


def index(request):
    return render(request, 'main/index.html',)


def snap(request, snap_token=None):
    if snap_token is None:
        snap_token = request.POST.get("token", "")

    snap = get_object_or_404(Snap, token=snap_token)
    songs = Song.objects.filter(snap=snap)

    n = len(songs)
    if n > 10:
        no_columns = 3
    elif n > 5:
        no_columns = 2
    else:
        no_columns = 1

    songs_arranged = [songs[i * no_columns:i * no_columns + no_columns] for i in range(math.ceil(n / no_columns))]

    context = {'songs_arranged': songs_arranged, 'exceeding': n % no_columns}
    return render(request, 'snapchat/snap.html', context)


def song(request, song_token):
    song = get_object_or_404(Song, token=song_token)

    if not song.visited:
        song.visited = True
        song.listened_on = datetime.now()
        song.save()

    context = {'song': song, 'snap_token': song.snap.token}
    return render(request, 'snapchat/song.html', context)
