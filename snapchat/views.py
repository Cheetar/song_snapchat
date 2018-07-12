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

    context = {'song_list': songs}
    return render(request, 'snapchat/profile.html', context)


def song(request, song_token):
    song = get_object_or_404(Song, token=song_token)

    if song.visited:
        return HttpResponse("Song already visited!")

    #song.visited = True
    # song.save()
    context = {'song': song, 'profile_token': song.profile.token}
    return render(request, 'snapchat/song.html', context)
