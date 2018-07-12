import math

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Profile, Song


def index(request):
    return render(request, 'main/index.html',)


def profile(request, profile_token=None):
    if profile_token is None:
        profile_token = request.POST.get("token", "")

    profile = get_object_or_404(Profile, token=profile_token)
    songs = Song.objects.filter(profile=profile)

    n = len(songs)
    if n > 10:
        no_columns = 3
    elif n > 5:
        no_columns = 2
    else:
        no_columns = 1

    songs_arranged = [songs[i * no_columns:i * no_columns + no_columns] for i in range(math.ceil(n / no_columns))]

    context = {'songs_arranged': songs_arranged, 'exceeding': n % no_columns}
    return render(request, 'snapchat/profile.html', context)


def song(request, song_token):
    song = get_object_or_404(Song, token=song_token)

    song.visited = True
    song.save()
    context = {'song': song, 'profile_token': song.profile.token}
    return render(request, 'snapchat/song.html', context)
