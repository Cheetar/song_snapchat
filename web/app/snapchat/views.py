import math
from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render

from .forms import SongAddForm
from .models import Snap, Song
from .utils import generate_token


def index(request):
    return render(request, 'main/index.html',)


def snap(request, snap_token=None):
    if snap_token is None:
        snap_token = request.POST.get("token", "")

    snap = get_object_or_404(Snap, token=snap_token)
    songs = Song.objects.filter(snap=snap).order_by('token')

    n = len(songs)
    # 5 songs per column, at most 3 columns, if 0 songs then 1 column
    nb_columns = min(max(((n - 1) // 5) + 1, 1), 3)

    # Split songs into 2D table, songs_arranged[row][column]
    songs_arranged = [songs[i * nb_columns:(i + 1) * nb_columns]
                      for i in range(math.ceil(n / nb_columns))]

    return render(request, 'snapchat/snap.html',
                  {'songs_arranged': songs_arranged})


def song(request, song_token):
    song = get_object_or_404(Song, token=song_token)
    was_song_visited = song.visited

    if not song.visited:
        song.visited = True
        song.listened_on = datetime.now()
        song.save()

    context = {'song': song,
               'snap_token': song.snap.token,
               'was_song_visited': was_song_visited}
    return render(request, 'snapchat/song.html', context)


def add_snap(request, token=None):
    if token:
        snap = get_object_or_404(Snap, token=token)
    else:
        token = generate_token()
        snap = Snap(token=token)
        snap.save()

    if not snap.finished_editing:
        if 'finished' in request.POST:
            snap.finished_editing = True
            snap.save()

    if snap.finished_editing:
        return redirect('share_snap', token=snap.token)

    songs = Song.objects.filter(snap=snap)
    context = {'snap': snap, 'songs': songs}
    return render(request, 'snapchat/add_snap.html', context)


def add_song(request, token=None):
    snap = get_object_or_404(Snap, token=token)

    if request.method == 'POST':
        form = SongAddForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.snap = snap

            song.save()
            return redirect('add_snap', token=snap.token)

    else:
        form = SongAddForm()

    return render(request, 'snapchat/add_song.html', {'form': form,
                                                      'snap': snap})


def share_snap(request, token=None):
    snap = get_object_or_404(Snap, token=token)
    context = {'snap': snap}
    return render(request, 'snapchat/share_snap.html', context)


def page_not_found(request, exception):
    """ Return custom 404 page.
    """
    response = render(request, '404.html')
    response.status_code = 404
    return response
