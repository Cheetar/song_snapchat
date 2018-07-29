from __future__ import unicode_literals

from django.conf import settings

import youtube_dl
from youtube_dl.utils import DownloadError

from .utils import generate_token


def download_mp3(url):
    """Download song from given youtube url.

    Downloads the video and converts it to mp3 format. The video file is
    deleted, only mp3 file is preserverd. Audio is saved to MEDIA_ROOT/songs/
    and the filename is '<32-random-hex-token>.mp3'. If download succeeded,
    path to file is returned, otherwise returns None.
    """

    token = generate_token()
    path = settings.MEDIA_ROOT + 'songs/'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': path + token + ".%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            return path + token + ".mp3"
        except DownloadError:
            return None


def is_url_valid(url):
    """Returns True if the given url is correct youtube url video. False
       otherwise.
    """

    with youtube_dl.YoutubeDL() as ydl:
        try:
            ydl.extract_info(url, download=False)
            return True
        except DownloadError:
            return False
